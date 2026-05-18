#!/usr/bin/env python3
"""Render the misleading-averages AI evaluation video as narrated slides."""
from __future__ import annotations

import asyncio
import os
import subprocess
from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'production' / 'averages_hide_bias_v0'
SLIDES = OUT / 'slides'
AUDIO = OUT / 'audio'
CLIPS = OUT / 'clips'
FINAL = OUT / 'averages_hide_bias_v0.mp4'
W, H = 1920, 1080
BG = (10, 13, 24)
PANEL = (24, 31, 50)
TEXT = (244, 247, 255)
MUTED = (177, 188, 208)
ACCENT = (102, 204, 255)
GREEN = (72, 187, 120)
YELLOW = (246, 224, 94)
PURPLE = (159, 122, 234)
ORANGE = (251, 146, 60)
RED = (245, 101, 101)
BLUE = (73, 164, 255)
VOICE = 'en-US-GuyNeural'
RATE = '+0%'

SLIDES_DATA = [
    {
        'title': 'The Average Can Hide the Bias',
        'kicker': 'A small pooled number can be true — and still hide the pattern you needed.',
        'kind': 'small_average',
        'bullets': [
            'Headline: pooled observational self-preference gap ≈ +0.38.',
            'That sounds reassuring until you split it by judge family.',
            'One average can hide four different stories moving in opposite directions.',
        ],
        'narration': '''Here is a number that sounds reassuring: plus zero point three eight. In our AI judge study, that was roughly the pooled observational self-preference gap. If you only saw that number, you might conclude that model self-preference was small, maybe not worth worrying about. But that average hid the important part. Claude, GPT, Gemini, and Kimi did not behave like one average judge. Some gaps were positive. One was strongly negative. The pooled average was mathematically true, but practically incomplete.'''
    },
    {
        'title': 'Four rooms, not one building temperature',
        'kicker': 'The average is useful. It is not where anyone actually stands.',
        'kind': 'thermometers',
        'bullets': [
            'A building can average to “comfortable” while rooms are hot and freezing.',
            'An evaluation can average to “small” while subgroups move differently.',
            'Nobody lives in the average room.',
        ],
        'narration': '''Think of a building with four rooms. One room is hot. One is warm. One is almost neutral. One is freezing. If you average the temperatures, the building might look comfortable. But nobody lives in the average room. People live in the actual rooms. Evaluation numbers work the same way. A pooled average is a useful summary, but users experience the particular judge, task, label, and prompt that touched their case.'''
    },
    {
        'title': 'The headline average',
        'kicker': 'Four model families wrote answers and judged answers.',
        'kind': 'headline_average',
        'bullets': [
            'Authors and judges: Claude, Gemini, GPT-5.5, and Kimi.',
            'Pooled observational C1 gap: +0.378 with interval [−0.330, +1.055].',
            'Useful first line — not the whole report.',
        ],
        'narration': '''In the observational slice of the study, four model families wrote answers and also judged answers: Claude, Gemini, GPT five point five, and Kimi. The pooled observational self-preference gap was plus zero point three seven eight, with an interval from about minus zero point three three to plus one point zero five five. As a first line, that is useful. It tells you the average across the whole setup was small and uncertain. But a first line is not the report.'''
    },
    {
        'title': 'The split view',
        'kicker': 'The same pooled number contains strong positive and negative pieces.',
        'kind': 'observational_split',
        'bullets': [
            'Claude: +2.43. GPT: +1.33. Gemini: +0.63.',
            'Kimi: −2.87 in this observational slice.',
            'Cancellation is not a nuisance here. Cancellation is the finding.',
        ],
        'narration': '''Now split that average by judge family. Claude’s observational self-preference gap was about plus two point four three. GPT’s was plus one point three three. Gemini’s was plus zero point six three. Kimi’s was minus two point eight seven. Those are not small variations around one common behavior. They point in different directions. The average became small because positive and negative pieces canceled. In a report, that cancellation is not a nuisance. It is the finding.'''
    },
    {
        'title': 'Why cancellation matters',
        'kicker': 'A calm dashboard can hide uneven user experiences.',
        'kind': 'cancellation',
        'bullets': [
            'The dashboard says “small average.”',
            'A real case may pass through a judge with a very different pattern.',
            'Design around risky slices, not just the comfortable pooled number.',
        ],
        'narration': '''Cancellation matters because decisions are not made by the pooled average. Imagine a dashboard that says the average label effect is small. That can be true while one judge family consistently helps a label, another hurts a label, and a third is almost invariant. A person whose case passes through one slice does not receive the average treatment. They receive that slice. So the design question is not only, what is the pooled effect? It is, which slices are risky enough to redesign?'''
    },
    {
        'title': 'Observational is not causal',
        'kicker': 'A raw gap can mix answer quality, style recognition, and displayed labels.',
        'kind': 'not_causal',
        'bullets': [
            'Observational self-gaps compare different answers, not identical answers.',
            'They can mix quality differences with label or style effects.',
            'Causal label-swap tests ask: same work, different displayed label?',
        ],
        'narration': '''There is another important distinction. The split view I just showed is observational. It compares how judges scored self-authored answers versus other-authored answers. That can mix several ingredients: underlying answer quality, recognizable style, and the displayed or perceived author label. To ask a causal label question, you need paired swaps: the same work shown under different displayed labels. Same answer, different label, different score? That is the cleaner test of whether the label itself moved the judgment.'''
    },
    {
        'title': 'The causal split view',
        'kicker': 'The paired label-swap result was smaller, but still model-specific.',
        'kind': 'causal_split',
        'bullets': [
            'Gemini showed the clearest displayed-self-label effect: +0.293.',
            'Claude was smaller: +0.120; Kimi near zero/noisy: +0.007.',
            'GPT-5.5 was exactly label-invariant in this paired slice: +0.000.',
        ],
        'narration': '''In the paired label-swap slice, the story changed again. Gemini showed the clearest displayed self-label effect, around plus zero point two nine three. Claude was smaller, around plus zero point one two zero. Kimi was near zero and noisy, around plus zero point zero zero seven. GPT five point five was exactly label-invariant in this paired slice: zero point zero zero zero. Again, the lesson is not one universal self-preference number. The lesson is model-specific behavior.'''
    },
    {
        'title': 'The average is a map thumbnail',
        'kicker': 'Good for orientation. Dangerous if you never zoom in.',
        'kind': 'map_thumbnail',
        'bullets': [
            'Start with the pooled number, then zoom into layers.',
            'Judge family, author family, task type, paired identical work, uncertainty.',
            'A map thumbnail is useful because it tells you where to inspect next.',
        ],
        'narration': '''A better metaphor is a map thumbnail. The pooled average is the tiny map in the corner. It helps orient you. But you would not navigate a city from the thumbnail alone. You zoom into layers: judge family, author family, task type, paired identical work, and uncertainty. A good average is not the end of analysis. It is the first pointer to where analysis should zoom next.'''
    },
    {
        'title': 'A practical reading checklist',
        'kicker': 'When you read an AI evaluation report, ask five questions.',
        'kind': 'checklist',
        'bullets': [
            'What is the pooled number?',
            'What happens by subgroup or model family?',
            'Is this observational, causal, stable, and actionable?',
        ],
        'narration': '''When you read an AI evaluation report, use a simple checklist. First, find the pooled number. Second, look for subgroup results: by model, task, label, language, or user group. Third, separate observational gaps from causal tests. Fourth, ask whether the pattern is stable across prompts and uncertainty intervals. Fifth, redesign around the risky slices. The pooled number is not useless. It is just not enough.'''
    },
    {
        'title': 'Nobody is judged by the average judge',
        'kicker': 'Report the average. Inspect the parts. Act on the risky slices.',
        'kind': 'close',
        'bullets': [
            'A small average can mean nothing is happening.',
            'Or it can mean several things are happening at once and canceling out.',
            'Nobody lives in the average room. Nobody is judged by the average judge.',
        ],
        'narration': '''So the takeaway is not that averages are bad. Averages are useful summaries. But a small average can mean nothing is happening, or it can mean several things are happening at once and canceling each other out. If you use AI judges, report the average, inspect the parts, separate observational gaps from causal label tests, and redesign the slices that are risky. Nobody lives in the average room. And nobody is judged by the average judge.'''
    },
]


def font(size: int, bold: bool = False):
    candidates = [
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        '/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf',
    ]
    for p in candidates:
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def draw_wrapped(draw, text, xy, fnt, fill, max_chars, line_gap=10):
    x, y = xy
    for para in str(text).split('\n'):
        for line in wrap(para, max_chars) or ['']:
            draw.text((x, y), line, font=fnt, fill=fill)
            bbox = draw.textbbox((x, y), line, font=fnt)
            y += bbox[3] - bbox[1] + line_gap
        y += line_gap
    return y


def rr(draw, box, radius=28, fill=PANEL, outline=None, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def draw_bg(draw):
    for y in range(H):
        t = y / H
        draw.line((0, y, W, y), fill=(int(10+10*t), int(13+9*t), int(24+34*t)))
    for x in range(-200, W, 120):
        draw.line((x, 100, x+420, H), fill=(22, 31, 55), width=1)
    draw.rectangle((0, 0, W, 92), fill=(8, 11, 20))


def draw_bullets(draw, bullets, x=118, y=800, max_chars=78):
    for b in bullets:
        draw.ellipse((x, y+12, x+18, y+30), fill=ACCENT)
        y = draw_wrapped(draw, b, (x+40, y), font(33), TEXT, max_chars, line_gap=7) + 3


def bar_x(v, left=420, right=1500, minv=-3.1, maxv=3.1):
    return int(left + (v - minv) / (maxv - minv) * (right - left))


def draw_bar_chart(draw, values, pooled=None, title=None, minv=-3.1, maxv=3.1):
    left, right = 420, 1500
    top, row_h = 330, 88
    zero = bar_x(0, left, right, minv, maxv)
    draw.line((zero, top-30, zero, top+row_h*len(values)+20), fill=(120, 132, 155), width=3)
    if pooled is not None:
        px = bar_x(pooled, left, right, minv, maxv)
        draw.line((px, top-45, px, top+row_h*len(values)+30), fill=YELLOW, width=4)
        draw.text((px+12, top-54), f'pooled {pooled:+.3f}', font=font(24, True), fill=YELLOW, anchor='lm')
    if title:
        draw.text((960, top-95), title, font=font(36, True), fill=MUTED, anchor='mm')
    for i, (name, val, color) in enumerate(values):
        y = top + i*row_h
        x1 = bar_x(val, left, right, minv, maxv)
        x0, x2 = (zero, x1) if val >= 0 else (x1, zero)
        draw.text((left-50, y+25), name, font=font(32, True), fill=TEXT, anchor='rm')
        rr(draw, (x0, y, x2, y+50), 12, color, None, 1)
        draw.text((x1 + (18 if val >= 0 else -18), y+25), f'{val:+.3f}' if abs(val) < 1 else f'{val:+.2f}', font=font(29, True), fill=color, anchor='lm' if val >= 0 else 'rm')
    draw.text((left, top+row_h*len(values)+72), 'negative', font=font(24), fill=MUTED, anchor='lm')
    draw.text((right, top+row_h*len(values)+72), 'positive', font=font(24), fill=MUTED, anchor='rm')


def thermometer(draw, x, y, label, temp, color, value):
    rr(draw, (x, y, x+330, y+330), 30, (18, 25, 43), color, 3)
    draw.text((x+165, y+48), label, font=font(34, True), fill=TEXT, anchor='mm')
    tube_x = x + 82
    draw.rounded_rectangle((tube_x-18, y+95, tube_x+18, y+255), radius=18, outline=(210, 220, 235), width=3, fill=(13, 17, 30))
    fill_h = int(38 + temp*115)
    draw.rounded_rectangle((tube_x-12, y+250-fill_h, tube_x+12, y+250), radius=12, fill=color)
    draw.ellipse((tube_x-34, y+236, tube_x+34, y+304), fill=color)
    draw.text((x+205, y+145), value, font=font(42, True), fill=color, anchor='mm')
    draw.text((x+205, y+205), 'observed gap', font=font(24), fill=MUTED, anchor='mm')


def draw_kind(draw, kind):
    if kind == 'small_average':
        vals = [('Claude', 2.43, PURPLE), ('GPT', 1.33, GREEN), ('Gemini', 0.63, ACCENT), ('Kimi', -2.87, RED)]
        zero = 960
        for i, (name, val, color) in enumerate(vals):
            y = 335 + i*70
            length = int(abs(val)/3.0*520)
            x0, x1 = (zero, zero+length) if val > 0 else (zero-length, zero)
            rr(draw, (x0, y, x1, y+34), 12, color + ( ) if False else color, None, 1)
            draw.text((x1+16 if val > 0 else x0-16, y+17), name, font=font(24, True), fill=color, anchor='lm' if val > 0 else 'rm')
        rr(draw, (655, 345, 1265, 625), 42, (12, 17, 30), ACCENT, 5)
        draw.text((960, 440), '+0.38', font=font(124, True), fill=TEXT, anchor='mm')
        draw.text((960, 535), 'pooled observational gap', font=font(38, True), fill=ACCENT, anchor='mm')
        draw.text((960, 608), 'true summary ≠ complete story', font=font(29), fill=MUTED, anchor='mm')
    elif kind == 'thermometers':
        thermometer(draw, 190, 330, 'Claude room', .92, PURPLE, '+2.43')
        thermometer(draw, 590, 330, 'GPT room', .70, GREEN, '+1.33')
        thermometer(draw, 990, 330, 'Gemini room', .55, ACCENT, '+0.63')
        thermometer(draw, 1390, 330, 'Kimi room', .10, RED, '−2.87')
        draw.text((960, 705), 'Average: “comfortable?”', font=font(44, True), fill=YELLOW, anchor='mm')
    elif kind == 'headline_average':
        x0, y0, cell = 520, 335, 92
        names = ['Claude', 'Gemini', 'GPT', 'Kimi']
        draw.text((x0+cell*2.5, y0-52), '4 authors × 4 judges', font=font(36, True), fill=TEXT, anchor='mm')
        for i, n in enumerate(names):
            draw.text((x0-28, y0+cell*(i+1)+cell/2), n, font=font(22, True), fill=MUTED, anchor='rm')
            draw.text((x0+cell*(i+1)+cell/2, y0-16), n, font=font(22, True), fill=MUTED, anchor='mm')
        for r in range(4):
            for c in range(4):
                color = ACCENT if r == c else (60, 72, 102)
                rr(draw, (x0+cell*(c+1), y0+cell*(r+1), x0+cell*(c+2)-8, y0+cell*(r+2)-8), 12, (19, 27, 45), color, 2)
                if r == c:
                    draw.text((x0+cell*(c+1.5)-4, y0+cell*(r+1.5)-4), 'self', font=font(18, True), fill=color, anchor='mm')
        rr(draw, (1130, 410, 1600, 610), 34, (18, 25, 43), YELLOW, 4)
        draw.text((1365, 475), '+0.378', font=font(74, True), fill=YELLOW, anchor='mm')
        draw.text((1365, 540), '[−0.330, +1.055]', font=font(34, True), fill=TEXT, anchor='mm')
        draw.text((1365, 590), 'pooled C1 observational', font=font(24), fill=MUTED, anchor='mm')
    elif kind == 'observational_split':
        vals = [('Claude', 2.433, PURPLE), ('GPT', 1.327, GREEN), ('Gemini', 0.627, ACCENT), ('Kimi', -2.873, RED)]
        draw_bar_chart(draw, vals, pooled=0.378, title='Observational C1 self-preference gaps')
        draw.text((960, 720), 'Cancellation is the finding.', font=font(44, True), fill=YELLOW, anchor='mm')
    elif kind == 'cancellation':
        rr(draw, (230, 340, 780, 610), 34, (18, 25, 43), ACCENT, 4)
        draw.text((505, 420), 'Dashboard', font=font(44, True), fill=TEXT, anchor='mm')
        draw.text((505, 505), 'Pooled: small', font=font(58, True), fill=YELLOW, anchor='mm')
        draw.text((505, 570), 'looks calm', font=font(28), fill=MUTED, anchor='mm')
        for y, txt, color in [(360, 'slice A: label helps', GREEN), (485, 'slice B: label hurts', RED), (610, 'slice C: invariant', ACCENT)]:
            draw.line((820, 505, 1060, y+25), fill=color, width=6)
            rr(draw, (1080, y, 1620, y+70), 24, (22, 29, 48), color, 3)
            draw.text((1350, y+35), txt, font=font(34, True), fill=color, anchor='mm')
    elif kind == 'not_causal':
        parts = [('answer quality', GREEN), ('style recognition', PURPLE), ('displayed label', ORANGE)]
        for i, (txt, color) in enumerate(parts):
            x = 250 + i*470
            rr(draw, (x, 335, x+390, 460), 28, (22, 29, 48), color, 4)
            draw.text((x+195, 398), txt, font=font(33, True), fill=color, anchor='mm')
        draw.text((960, 520), 'observational gap = mixture', font=font(44, True), fill=MUTED, anchor='mm')
        rr(draw, (410, 600, 820, 700), 24, (246, 248, 255), ACCENT, 4)
        rr(draw, (1100, 600, 1510, 700), 24, (246, 248, 255), ORANGE, 4)
        draw.text((615, 650), 'same answer\nLabel A', font=font(30, True), fill=(18, 24, 40), anchor='mm')
        draw.text((1305, 650), 'same answer\nLabel B', font=font(30, True), fill=(18, 24, 40), anchor='mm')
        draw.line((845, 650, 1075, 650), fill=YELLOW, width=7)
        draw.polygon([(1075,650),(1030,623),(1030,677)], fill=YELLOW)
        draw.text((960, 745), 'paired swap asks the causal label question', font=font(31, True), fill=YELLOW, anchor='mm')
    elif kind == 'causal_split':
        vals = [('Gemini', 0.293, ACCENT), ('Claude', 0.120, PURPLE), ('GPT', 0.000, GREEN), ('Kimi', 0.007, RED)]
        draw_bar_chart(draw, vals, pooled=0.105, title='Paired label-swap SELF−OTHER residuals', minv=-0.35, maxv=0.35)
        draw.text((960, 720), 'Smaller effects, still not one average judge.', font=font(42, True), fill=YELLOW, anchor='mm')
    elif kind == 'map_thumbnail':
        rr(draw, (245, 340, 660, 610), 32, (17, 24, 42), ACCENT, 4)
        draw.rectangle((310, 405, 595, 545), outline=(100, 210, 255), width=3)
        draw.line((330, 520, 430, 455, 520, 500, 575, 430), fill=GREEN, width=5)
        draw.ellipse((458, 438, 482, 462), fill=YELLOW)
        draw.text((452, 655), 'map thumbnail', font=font(32, True), fill=ACCENT, anchor='mm')
        layers = [('judge', PURPLE), ('author', GREEN), ('task', ORANGE), ('paired work', ACCENT), ('uncertainty', YELLOW)]
        for i, (txt, color) in enumerate(layers):
            x = 820 + (i%2)*390
            y = 340 + (i//2)*118
            rr(draw, (x, y, x+320, y+80), 22, (22, 29, 48), color, 3)
            draw.text((x+160, y+40), txt, font=font(32, True), fill=color, anchor='mm')
        draw.line((690, 475, 790, 475), fill=YELLOW, width=8)
        draw.polygon([(790,475),(745,448),(745,502)], fill=YELLOW)
    elif kind == 'checklist':
        items = ['Find the pooled number', 'Look for subgroup results', 'Separate observational from causal', 'Ask whether it is stable', 'Redesign risky slices']
        for i, item in enumerate(items):
            y = 320 + i*86
            rr(draw, (360, y, 1560, y+64), 18, (22, 29, 48), ACCENT if i < 2 else (67, 82, 120), 2)
            draw.text((415, y+33), '☑', font=font(34, True), fill=GREEN, anchor='lm')
            draw.text((485, y+33), item, font=font(34, True), fill=TEXT, anchor='lm')
    elif kind == 'close':
        for x, name, color in [(230, 'Claude', PURPLE), (610, 'Gemini', ACCENT), (990, 'GPT', GREEN), (1370, 'Kimi', RED)]:
            rr(draw, (x, 330, x+320, 150+520), 30, (18, 25, 43), color, 3)
            draw.text((x+160, 385), name, font=font(34, True), fill=color, anchor='mm')
            draw.text((x+160, 505), 'not the\naverage\njudge', font=font(34, True), fill=TEXT, anchor='mm')
        rr(draw, (350, 690, 1570, 780), 32, (12, 17, 30), YELLOW, 4)
        draw.text((960, 735), 'Nobody lives in the average room. Nobody is judged by the average judge.', font=font(34, True), fill=YELLOW, anchor='mm')


def render_slide(i, data):
    img = Image.new('RGB', (W, H), BG)
    draw = ImageDraw.Draw(img)
    draw_bg(draw)
    draw.text((80, 46), 'GPT-5.5 Model', font=font(30, True), fill=ACCENT, anchor='lm')
    draw.text((1840, 46), f'{i+1:02d}/{len(SLIDES_DATA):02d}', font=font(28), fill=MUTED, anchor='rm')
    draw.text((110, 150), data['title'], font=font(58, True), fill=TEXT)
    draw_wrapped(draw, data['kicker'], (115, 230), font(34), ACCENT, 86)
    draw_kind(draw, data['kind'])
    draw_bullets(draw, data['bullets'])
    draw.text((960, 1038), 'AI evaluation interpretation — report the average, inspect the parts', font=font(24), fill=(125, 136, 158), anchor='mm')
    p = SLIDES / f'slide_{i+1:02d}.png'
    img.save(p)
    return p


async def tts_one(i, text):
    import edge_tts
    out = AUDIO / f'slide_{i+1:02d}.mp3'
    if out.exists() and out.stat().st_size > 1000:
        return out
    await edge_tts.Communicate(text, VOICE, rate=RATE).save(str(out))
    return out


def run(cmd):
    subprocess.run([str(c) for c in cmd], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def duration(path: Path) -> float:
    p = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', str(path)], text=True, stdout=subprocess.PIPE, check=True)
    return float(p.stdout.strip())


async def main():
    for d in [SLIDES, AUDIO, CLIPS]:
        d.mkdir(parents=True, exist_ok=True)
    for i, data in enumerate(SLIDES_DATA):
        render_slide(i, data)
    await asyncio.gather(*(tts_one(i, data['narration']) for i, data in enumerate(SLIDES_DATA)))
    concat = OUT / 'concat.txt'
    with concat.open('w', encoding='utf-8') as f:
        for i in range(len(SLIDES_DATA)):
            slide = SLIDES / f'slide_{i+1:02d}.png'
            aud = AUDIO / f'slide_{i+1:02d}.mp3'
            clip = CLIPS / f'slide_{i+1:02d}.mp4'
            dur = duration(aud) + 0.35
            run(['ffmpeg','-nostdin','-y','-loop','1','-framerate','1','-i',slide,'-i',aud,'-t',f'{dur:.3f}','-c:v','libx264','-preset','ultrafast','-tune','stillimage','-pix_fmt','yuv420p','-r','24','-vf','scale=1920:1080','-c:a','aac','-b:a','192k','-shortest',clip])
            f.write(f"file '{clip.resolve()}'\n")
    run(['ffmpeg','-nostdin','-y','-f','concat','-safe','0','-i',concat,'-c','copy',FINAL])
    print(FINAL)
    print(f'{duration(FINAL):.3f}')


if __name__ == '__main__':
    os.chdir(ROOT)
    asyncio.run(main())
