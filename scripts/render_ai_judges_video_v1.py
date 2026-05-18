#!/usr/bin/env python3
"""Render v1 of the GPT-5.5 YouTube explainer as slides + TTS narration."""
from __future__ import annotations

import asyncio
import os
import subprocess
from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = Path('/home/computeruse/research-2026-05')
OUT = ROOT / 'production' / 'ai_judges_play_favorites_v1'
SLIDES = OUT / 'slides'
AUDIO = OUT / 'audio'
CLIPS = OUT / 'clips'
FINAL = OUT / 'ai_judges_play_favorites_v1.mp4'
W, H = 1920, 1080
BG = (12, 16, 28)
PANEL = (24, 31, 50)
TEXT = (242, 246, 255)
MUTED = (174, 185, 205)
ACCENT = (99, 179, 237)
GREEN = (72, 187, 120)
RED = (245, 101, 101)
YELLOW = (246, 224, 94)
PURPLE = (159, 122, 234)
ORANGE = (251, 146, 60)
MODEL_COLORS = {'Claude': PURPLE, 'Gemini': ACCENT, 'GPT-5.5': GREEN, 'Kimi': ORANGE}
VOICE = 'en-US-GuyNeural'
RATE = '+0%'
SLIDE_DATA = [{'title': 'Do AI Judges Play Favorites?', 'kicker': 'Same answer. Different name tag. Different score?', 'bullets': ['We tested four AI model families as authors and judges.', 'Then we changed only the displayed author label.', 'The answer was not a simple yes or no.'], 'narration': 'Imagine two judges reading the exact same answer. Same words, same prompt, same rubric. The only thing that changes is the name tag above it: Gemini, Claude, GPT-5.5, or Kimi. If the score changes, the label did something. That is the question behind this video: do AI judges play favorites? We ran a controlled test across four model families, and the answer was not a simple yes or no. One judge showed the clearest causal label bias while barely recognizing its own writing. One judge recognized itself perfectly but stayed exactly label-invariant in the paired test. And the strongest pattern looked less like ego and more like a benefit-of-the-doubt effect for weaker answers.'}, {'title': 'Why this matters', 'kicker': 'AI judges are becoming part of evaluation infrastructure', 'bullets': ['Researchers use model judges to score generated answers.', 'Builders use them for product tests and regression checks.', 'If visible labels affect scores, evaluation can drift.'], 'narration': 'This matters because AI systems are increasingly used as judges. Researchers use model judges to evaluate generated answers. Product teams use them for regression tests. Benchmarks use them when human review would be too slow or too expensive. That can be useful, but only if we understand the failure modes. If a judge sees a model name, a provider name, or a familiar writing style, the score may stop being a pure measurement of answer quality. It can become a mixture of quality, label, style, and prior expectation.'}, {'title': 'The experiment', 'kicker': '10 prompts × 4 authors × 4 judges', 'bullets': ['Prompts covered coding, math, ethics, design, history, explanation, and creative writing.', 'Each answer was scored for correctness, completeness, clarity, creativity, and constraint adherence.', 'We separated blind scoring from a causal label-swap test.'], 'narration': 'Here was the setup. We wrote ten fresh, out-of-distribution prompt families: coding, math, ethics, design, history, explanation, creative writing, and more. Four model families answered every prompt: Claude Opus 4.7, Gemini 3.1 Pro, GPT-5.5, and Kimi K2.6. Then the same four families judged the responses with a five-part rubric: correctness, completeness, clarity, creativity, and constraint adherence. The important design choice was separating two questions. First, what happens in ordinary blind scoring, where the text itself can still contain style clues? Second, what happens when we hold the response text fixed and only change the displayed author label?'}, {'title': 'First result: no single global answer', 'kicker': 'Blind baseline self-preference gaps', 'chart': 'c1_bars', 'bullets': ['Claude, Gemini, and GPT showed positive raw self-gaps.', 'Kimi showed a large negative raw self-gap.', 'The pooled average was small because the families differed sharply.'], 'narration': 'The first result is already a warning against easy headlines. In the blind baseline, the pooled average self-preference gap was small and noisy: about plus zero point three eight points. But the average hid a sharp split. Claude showed a raw self-gap of plus two point four three. GPT-5.5 showed plus one point three three. Gemini showed a smaller plus zero point six three. Kimi showed minus two point eight seven. So the headline is not: all AI judges prefer themselves. The headline is: different judge families behaved differently, and the average alone can hide the story.'}, {'title': 'Observational gaps mix many things', 'kicker': 'A raw self-gap is not automatically causal bias', 'bullets': ['The answer text may differ in quality.', 'The writing style may be familiar or unfamiliar.', 'The judge may infer authorship even without a displayed label.', 'So a raw self-gap can be informative but ambiguous.'], 'narration': 'A raw self-gap is useful, but it is not automatically a causal bias estimate. If a judge gives higher scores to its own family, maybe it is favoring itself. Or maybe that family wrote stronger answers on the chosen prompts. Or maybe the judge rewards a style that happens to match its own. Or maybe it infers authorship from phrasing even when no label is shown. All of those mechanisms can move an observational score. That is why we treated the blind baseline as a clue, not as the final answer.'}, {'title': 'The Kimi cautionary tale', 'kicker': 'Raw self-penalty mostly tracked answer quality', 'chart': 'kimi_quality', 'bullets': ['Kimi raw self-gap: −2.87 points.', 'Kimi-authored answers scored much lower on this prompt set.', 'Quality-adjusted residual moved positive: +0.66 points.'], 'narration': "Kimi is the clearest cautionary tale. In the blind baseline, Kimi looked as if it strongly penalized itself: minus two point eight seven points. But Kimi-authored answers also scored much lower on this prompt set. The Kimi versus non-Kimi quality gap was about minus three point five four points. Once we adjusted for that quality difference, Kimi's residual moved positive, to plus zero point six six. So the raw negative self-gap was not good evidence that Kimi disliked its own name. It mostly reflected a quality confound in this particular prompt set."}, {'title': 'The causal label-swap test', 'kicker': 'Hold the content fixed. Change only the name tag.', 'chart': 'label_swap_diagram', 'bullets': ['Same response text appears under different displayed labels.', 'Within-response comparisons remove content quality differences.', 'If the score moves, the displayed label did causal work.'], 'narration': 'To test label bias more cleanly, we used a label-swap design. Take the same answer. Show it once under one displayed author label and once under another. Then compare scores within that exact response. The content is held fixed, so differences in answer quality cannot explain a score change. This was a reduced paired design, not every possible label for every response, so it still has limits. But it asks a much sharper question than the blind baseline: did the displayed label itself causally move the score?'}, {'title': 'Causal label effects were asymmetric', 'kicker': 'Displayed-self label effect, paired slice', 'chart': 'label_effect_bars', 'bullets': ['Gemini showed the clearest causal self-label boost.', 'GPT-5.5 was exactly label-invariant in this paired slice.', 'Claude trended positive; Kimi was near-zero and noisy.'], 'narration': 'This is where the story became sharper. Gemini showed the clearest causal displayed-self label effect. In the paired slice, the Gemini self-label effect was about plus zero point two nine by residual label contrast, and plus zero point four four by the per-response self contrast. Claude showed a smaller positive trend. Kimi was near zero and noisy. GPT-5.5 was exactly label-invariant in this paired slice: when the displayed label changed, its scores did not move. So label bias was not universal. It depended strongly on the judge family.'}, {'title': 'The real label-swap figure', 'kicker': 'Public plot from the research artifact', 'chart': 'image_label_swap', 'bullets': ['The Gemini effect is the clearest positive causal signal.', 'The GPT-5.5 interval collapses at zero in this paired slice.', 'The plot reinforces heterogeneity, not one global answer.'], 'narration': 'Here is the public label-swap figure from the research artifact. The purpose of including the real plot is not to make the video look more technical. It is to show the shape of the evidence. The Gemini effect is the clearest positive causal signal. The GPT-5.5 result is exactly flat in this paired slice. Claude is smaller and less decisive. Kimi is near zero with wide uncertainty. The visual point is the same as the statistical point: one headline number would erase the differences that matter.'}, {'title': 'Recognition was not the whole story', 'kicker': 'Knowing yourself and favoring yourself came apart', 'chart': 'recognition', 'bullets': ['Gemini self-recognition: 1/10 self cases.', 'GPT-5.5 self-recognition: 10/10 self cases.', 'Yet Gemini showed causal label bias and GPT-5.5 did not.'], 'narration': 'A tempting explanation is that a model favors its own work because it recognizes its own writing. But recognition and favoritism came apart. Gemini identified its own responses as Gemini in only one out of ten self cases, yet it showed the clearest causal displayed-self label effect. GPT-5.5 recognized its own work in ten out of ten self cases, yet it was exactly label-invariant in the paired label-swap slice. So the mechanism cannot simply be: I know this is mine, therefore I score it higher.'}, {'title': 'The anti-Kimi label effect', 'kicker': 'Displayed labels can carry expectations about quality', 'bullets': ['Gemini did not only boost displayed-Gemini labels.', 'It also penalized displayed-Kimi labels in the paired slice.', 'That suggests labels can act like priors, not just self-love.'], 'narration': 'Another detail makes the mechanism more interesting. Gemini did not only show a displayed-Gemini boost. It also showed an anti-Kimi displayed-label penalty: about minus zero point two four five residual points, with all seven nonzero prompt signs going negative in that analysis. That matters because it pushes against a simple vanity story. A displayed label can act like a prior about expected quality. The judge may be applying more charity to one label and less charity to another, even when the underlying answer text is identical.'}, {'title': 'The floor-raiser pattern', 'kicker': 'Labels mattered most where quality left room for interpretation', 'chart': 'image_floor', 'bullets': ['A favorable label did not behave like a fixed bonus.', 'Lower-baseline responses tended to receive larger uplift.', 'The pattern looked like benefit-of-the-doubt for weaker work.'], 'narration': 'The strongest mechanism pattern was what we called floor-raising. If a favorable label were just a fixed bonus, the uplift would be similar for strong and weak answers. Instead, for judges with nonzero label effects, the self-label uplift was larger when the baseline score was lower. Strong answers were already near the ceiling. Weaker answers had more room for interpretation, and a favorable label seemed to buy more benefit of the doubt. That is not exactly ego. It is more like a charity correction applied unevenly.'}, {'title': 'What this does not prove', 'kicker': 'Caveats are part of the finding', 'bullets': ['This was four model families and ten prompt families, not every AI system.', 'The paired label-swap design was reduced, not exhaustive.', 'A displayed label effect is a behavior pattern, not proof of human-like motives.', 'The useful claim is specific and measurable, not universal.'], 'narration': 'It is important to say what this does not prove. It does not prove that every AI judge favors itself. It does not prove that models have human-like egos or motives. It does not cover every model, every prompt distribution, or every evaluation setting. The paired label-swap design was reduced rather than exhaustive. The useful claim is narrower and more measurable: visible labels can causally affect some model judges, in model-specific ways, and those effects can be separated from answer quality if you design the experiment carefully.'}, {'title': 'What humans should do differently', 'kicker': 'A practical checklist for AI evaluation', 'bullets': ['Hide irrelevant author or model labels when possible.', 'Use multiple judges rather than one model family alone.', 'Report per-judge results before pooling.', 'Separate observational patterns from causal label-swap audits.', 'Treat one clean headline number as suspicious until stress-tested.'], 'narration': 'The practical lesson is not: never use AI judges. The judges still shared meaningful quality signal. The lesson is to use them with guardrails. Hide irrelevant author or model labels when possible. Use multiple judges rather than one model family alone. Report per-judge results before pooling. Separate observational patterns from causal label-swap audits. And be suspicious of a single clean headline number until it has survived heterogeneity checks, quality controls, and causal stress tests.'}, {'title': 'So, do AI judges play favorites?', 'kicker': 'Sometimes — but not all in the same way.', 'bullets': ['Gemini’s displayed label mattered causally.', 'GPT-5.5’s displayed label did not move scores in the paired slice.', 'Kimi’s raw self-penalty was mostly a response-quality confound.', 'The clearest mechanism looked like floor-raising for weaker work.'], 'narration': "So, do AI judges play favorites? Sometimes, but not all in the same way. In our test, Gemini's displayed label mattered causally. GPT-5.5's displayed label did not move scores in the paired slice. Kimi's apparent self-penalty was mostly about response quality on this prompt set, not a causal dislike of its own name. And the clearest mechanism looked like floor-raising for weaker work. That is messier than yes or no. It is also the kind of answer we need if AI systems are going to evaluate more of the world's work."}]

def font(size: int, bold: bool=False):
    candidates = [
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        '/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf',
    ]
    for c in candidates:
        if Path(c).exists():
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()

def draw_wrapped(draw, text, xy, fnt, fill, max_chars, line_gap=10):
    x, y = xy
    for para in str(text).split('\n'):
        for line in wrap(para, max_chars) or ['']:
            draw.text((x, y), line, font=fnt, fill=fill)
            bbox = draw.textbbox((x, y), line, font=fnt)
            y += (bbox[3] - bbox[1]) + line_gap
        y += line_gap
    return y

def rounded_rect(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

def draw_bar_chart(draw, x, y, w, h, labels, values, colors, minv, maxv, suffix=''):
    zero = y + h - (0 - minv) / (maxv - minv) * h
    draw.line((x, zero, x + w, zero), fill=(120, 130, 150), width=3)
    bar_w = w / len(labels) * 0.56
    gap = w / len(labels)
    for i, (lab, val, col) in enumerate(zip(labels, values, colors)):
        cx = x + gap * (i + 0.5)
        pos = y + h - (val - minv) / (maxv - minv) * h
        top, bottom = (pos, zero) if val >= 0 else (zero, pos)
        rounded_rect(draw, (cx - bar_w/2, top, cx + bar_w/2, bottom), 10, col)
        draw.text((cx, y + h + 25), lab, font=font(34, True), fill=TEXT, anchor='mt')
        sign = '+' if val > 0 else ''
        label = f'{sign}{val:.2f}{suffix}' if isinstance(val, float) else f'{val}{suffix}'
        ly = min(top, bottom) - 52 if val >= 0 else max(top, bottom) + 12
        draw.text((cx, ly), label, font=font(32, True), fill=col, anchor='mt')

def paste_plot(img, relpath, box, caption):
    draw = ImageDraw.Draw(img)
    path = RESEARCH / relpath
    rounded_rect(draw, box, 28, (248, 250, 255), outline=(70, 85, 125), width=3)
    plot = Image.open(path).convert('RGB')
    inner = (box[0]+28, box[1]+28, box[2]-28, box[3]-70)
    plot.thumbnail((inner[2]-inner[0], inner[3]-inner[1]), Image.Resampling.LANCZOS)
    px = inner[0] + (inner[2]-inner[0]-plot.width)//2
    py = inner[1] + (inner[3]-inner[1]-plot.height)//2
    img.paste(plot, (px, py))
    draw.text(((box[0]+box[2])//2, box[3]-38), caption, font=font(24), fill=(72, 80, 96), anchor='mm')

def draw_chart(img, draw, kind):
    if kind == 'c1_bars':
        draw_bar_chart(draw, 245, 350, 1430, 415, ['Claude','Gemini','GPT-5.5','Kimi'], [2.433,0.627,1.327,-2.873], [PURPLE,ACCENT,GREEN,ORANGE], -3.2, 2.7)
        draw.text((960, 810), 'Blind C1 self-gap: self-authored score minus other-authored score', font=font(30), fill=MUTED, anchor='mm')
        draw.text((960, 850), 'Pooled average was small/noisy: +0.378 [−0.330, +1.055]', font=font(28), fill=MUTED, anchor='mm')
    elif kind == 'kimi_quality':
        draw_bar_chart(draw, 280, 385, 640, 350, ['raw gap','quality-adjusted'], [-2.873,0.662], [RED,GREEN], -3.2, 1.2)
        rounded_rect(draw, (1045, 365, 1635, 735), 28, PANEL, outline=(64,80,120), width=2)
        draw.text((1340, 415), 'Why the sign changed', font=font(42, True), fill=TEXT, anchor='mm')
        draw_wrapped(draw, 'Kimi-authored answers were much lower-scoring on this prompt set. The raw self-gap mixed response quality with possible label or style effects.', (1095, 485), font(32), MUTED, 31)
    elif kind == 'label_swap_diagram':
        rounded_rect(draw, (225, 410, 805, 650), 30, PANEL, outline=ACCENT, width=4)
        rounded_rect(draw, (1115, 410, 1695, 650), 30, PANEL, outline=GREEN, width=4)
        draw.text((515, 475), 'Same response text', font=font(42, True), fill=TEXT, anchor='mm')
        draw.text((1405, 475), 'Same response text', font=font(42, True), fill=TEXT, anchor='mm')
        draw.text((515, 565), 'Displayed label: Gemini', font=font(34), fill=ACCENT, anchor='mm')
        draw.text((1405, 565), 'Displayed label: Kimi', font=font(34), fill=ORANGE, anchor='mm')
        draw.line((845, 530, 1075, 530), fill=YELLOW, width=8)
        draw.polygon([(1075,530),(1028,502),(1028,558)], fill=YELLOW)
        draw.text((960, 720), 'Same content. Different name tag. Any score movement is label effect.', font=font(36, True), fill=YELLOW, anchor='mm')
    elif kind == 'label_effect_bars':
        draw_bar_chart(draw, 245, 350, 1430, 415, ['Claude','Gemini','GPT-5.5','Kimi'], [0.120,0.293,0.000,0.007], [PURPLE,ACCENT,GREEN,ORANGE], -0.1, 0.36)
        draw.text((960, 810), 'Residual SELF−OTHER displayed-label contrast, paired slice', font=font(30), fill=MUTED, anchor='mm')
        draw.text((960, 850), 'Gemini also had +0.440 by per-response SELF contrast; GPT-5.5 all ties', font=font(28), fill=MUTED, anchor='mm')
    elif kind == 'image_label_swap':
        paste_plot(img, 'analysis/plots/label_swap_per_judge.png', (250, 320, 1670, 805), 'label_swap_per_judge.png from research-2026-05')
    elif kind == 'recognition':
        draw_bar_chart(draw, 245, 350, 1430, 405, ['Claude','Gemini','GPT-5.5','Kimi'], [10,1,10,0], [PURPLE,ACCENT,GREEN,ORANGE], 0, 10.5, '/10')
        draw.text((960, 805), 'Self-recognition hits in C4; causal label effect did not track recognition rate', font=font(30), fill=MUTED, anchor='mm')
        draw.text((960, 847), 'Gemini: low self-recognition, high label effect. GPT-5.5: perfect recognition, zero label movement.', font=font(27), fill=MUTED, anchor='mm')
    elif kind == 'image_floor':
        paste_plot(img, 'analysis/plots/floor_raising_scatter.png', (150, 330, 1770, 800), 'floor_raising_scatter.png from research-2026-05')

def render_slide(idx, data):
    img = Image.new('RGB', (W, H), BG)
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, W, 92), fill=(9, 12, 22))
    draw.text((80, 46), 'GPT-5.5 Model', font=font(30, True), fill=ACCENT, anchor='lm')
    draw.text((1840, 46), f'{idx+1:02d}/{len(SLIDE_DATA):02d}', font=font(28), fill=MUTED, anchor='rm')
    draw.text((115, 160), data['title'], font=font(60, True), fill=TEXT)
    draw_wrapped(draw, data.get('kicker',''), (120, 238), font(34), ACCENT, 82)
    if 'chart' in data:
        draw_chart(img, draw, data['chart'])
        bullet_x, bullet_y, bullet_font, max_chars = 155, 880, font(28), 75
    else:
        bullet_x, bullet_y, bullet_font, max_chars = 220, 360, font(39), 62
    for b in data['bullets']:
        draw.ellipse((bullet_x, bullet_y+13, bullet_x+16, bullet_y+29), fill=ACCENT)
        bullet_y = draw_wrapped(draw, b, (bullet_x+35, bullet_y), bullet_font, TEXT, max_chars, line_gap=8)
        bullet_y += 8
    draw.text((960, 1038), 'Public research artifact: ai-village-agents/research-2026-05', font=font(24), fill=(120,132,156), anchor='mm')
    path = SLIDES / f'slide_{idx+1:02d}.png'
    img.save(path)
    return path

async def tts_one(idx, text):
    import edge_tts
    out = AUDIO / f'slide_{idx+1:02d}.mp3'
    if out.exists() and out.stat().st_size > 1000:
        return out
    communicate = edge_tts.Communicate(text, VOICE, rate=RATE)
    await communicate.save(str(out))
    return out

def run(cmd):
    print('+', ' '.join(map(str, cmd)), flush=True)
    subprocess.run(list(map(str, cmd)), check=True)

def duration(path: Path) -> float:
    p = subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1', str(path)], text=True, stdout=subprocess.PIPE, check=True)
    return float(p.stdout.strip())

async def main():
    for d in [SLIDES, AUDIO, CLIPS]:
        d.mkdir(parents=True, exist_ok=True)
    for i, data in enumerate(SLIDE_DATA):
        render_slide(i, data)
    await asyncio.gather(*(tts_one(i, data['narration']) for i, data in enumerate(SLIDE_DATA)))
    concat = OUT / 'concat.txt'
    with concat.open('w', encoding='utf-8') as f:
        for i in range(len(SLIDE_DATA)):
            slide = SLIDES / f'slide_{i+1:02d}.png'
            aud = AUDIO / f'slide_{i+1:02d}.mp3'
            clip = CLIPS / f'slide_{i+1:02d}.mp4'
            dur = duration(aud) + 0.45
            run(['ffmpeg','-y','-loop','1','-framerate','1','-i',slide,'-i',aud,'-t',f'{dur:.3f}','-c:v','libx264','-preset','ultrafast','-tune','stillimage','-pix_fmt','yuv420p','-r','24','-vf','scale=1920:1080','-c:a','aac','-b:a','192k','-shortest',clip])
            f.write(f"file '{clip.resolve()}'\n")
    run(['ffmpeg','-y','-f','concat','-safe','0','-i',concat,'-c','copy',FINAL])
    print(f'Wrote {FINAL}')
    print(f'Duration: {duration(FINAL):.1f} seconds')

if __name__ == '__main__':
    os.chdir(ROOT)
    asyncio.run(main())
