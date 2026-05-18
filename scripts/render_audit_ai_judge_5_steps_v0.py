#!/usr/bin/env python3
"""Render the practical AI judge audit video as narrated slides."""
from __future__ import annotations

import asyncio
import os
import subprocess
from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'production' / 'audit_ai_judge_5_steps_v0'
SLIDES = OUT / 'slides'
AUDIO = OUT / 'audio'
CLIPS = OUT / 'clips'
FINAL = OUT / 'audit_ai_judge_5_steps_v0.mp4'
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
VOICE = 'en-US-GuyNeural'
RATE = '+0%'

SLIDES_DATA = [
    {
        'title': 'How to Audit an AI Judge in 5 Steps',
        'kicker': 'The practical question: same work, different label, different score?',
        'kind': 'hook',
        'bullets': [
            '“Is the judge fair?” is too vague.',
            'Test one causal question: did an irrelevant label move the score?',
            'This is a lightweight workflow, not a fairness certificate.',
        ],
        'narration': '''Suppose you use an AI system to grade essays, rank job applications, review code, or choose the best answer from several models. The dangerous question is: is the judge fair? That question is too big. It invites a vague answer, and vague answers are where bias hides. A better question is smaller and testable: if the same work appears under a different irrelevant label, does the AI judge change its score? In a previous video, I explained a controlled AI Village study where the same answer was shown under different displayed author labels. Some judges changed. One did not. This video is the practical version: a five-step audit you can run before you trust an AI judge.'''
    },
    {
        'title': 'Step 1 — Write the decision down',
        'kicker': 'Define what should matter, and what should not.',
        'kind': 'decision',
        'bullets': [
            'Not “evaluate quality”; name the actual decision.',
            'Examples: rank support answers, review code patches, score proposals.',
            'Mark irrelevant labels: model name, vendor, team, applicant, reputation.',
        ],
        'narration': '''Step one is to write down the decision the judge is helping with. Not a generic goal like evaluate quality. A concrete decision. For example: choose the strongest customer-support answer. Or score whether this code patch follows the requested constraints. Or rank grant proposals for clarity and feasibility. Then write down what information should matter and what information should not matter. The answer text might matter. Evidence, correctness, safety, and constraint-following might matter. But the model name, applicant name, team name, vendor name, or previous reputation might not matter for this scoring task. That boundary is the audit target. If a label should not matter, you can test whether it does.'''
    },
    {
        'title': 'Step 2 — Make the rubric boring',
        'kicker': 'Few dimensions. Fixed scale. Defined endpoints.',
        'kind': 'rubric',
        'bullets': [
            'A poetic rubric gives the judge room to improvise.',
            'Use 3–5 concrete dimensions and a fixed score scale.',
            'Define what low and high scores mean before scoring begins.',
        ],
        'narration': '''Step two is to make the rubric boring. A good audit rubric is not poetic. It is specific enough that two reasonable graders could understand it the same way. Use a small number of dimensions. For a text answer, maybe correctness, completeness, clarity, and constraint adherence. For a code review, maybe functional correctness, minimality, test coverage, and risk. Use a fixed scale. One to five is often enough. Most importantly, define the endpoints. A score of one means what? A score of five means what? If you cannot say, the model will invent its own scale. The boring rubric is not just paperwork. It reduces the space where a judge can smuggle in a feeling about a label.'''
    },
    {
        'title': 'Step 3 — Create paired examples',
        'kicker': 'Clone the item. Change one thing: the label.',
        'kind': 'pairs',
        'bullets': [
            'Same essay, answer, patch, or proposal.',
            'Different displayed label: model, vendor, applicant, team, institution.',
            'Shuffle pairs apart; mix in normal examples; do not announce the duplicates.',
        ],
        'narration': '''Step three is the heart of the audit: create pairs. Take the exact same item and show it to the judge twice, but change only the label you want to test. Same essay, different applicant name. Same answer, different model name. Same patch, different team label. Same proposal, different institution label. If the label is irrelevant, the score should stay the same or move only by ordinary noise. Keep the pair far enough apart that the judge does not simply notice the duplicate and refuse to score it. Shuffle the order. Mix in normal examples. Do not tell the judge which items are paired. For a quick audit, ten to twenty paired items can already be revealing. The key is discipline: change one thing at a time.'''
    },
    {
        'title': 'Step 4 — Compare paired differences',
        'kicker': 'Do not start with group averages.',
        'kind': 'differences',
        'bullets': [
            'Compute score with label A minus score with label B inside each pair.',
            'Then summarize mean difference, sign counts, and dimensions affected.',
            'This separates label movement from underlying answer quality.',
        ],
        'narration': '''Step four is to score blind, then compare the paired differences. Do not start with the average score for each group. Averages can be misleading because one group’s underlying answers may be better. Instead, compute the difference inside each pair: score with label A, minus score with label B. If the same item gets a higher score when labeled trusted vendor, that pair has a positive trusted-label effect. If it gets a lower score, the effect is negative. If it is identical, the effect is zero. Then summarize the paired differences. Look at the mean. Look at how many differences point the same way. Look at whether effects are concentrated on weak items, ambiguous items, or specific rubric dimensions.'''
    },
    {
        'title': 'Step 5 — Act on the result',
        'kicker': 'Finding bias is a design input, not just a diagnosis.',
        'kind': 'actions',
        'bullets': [
            'Hide irrelevant labels with neutral IDs.',
            'Use multiple judges and keep human review for borderline cases.',
            'Re-audit when the model, prompt, rubric, or domain changes.',
        ],
        'narration': '''Step five is to act on what you find. If label effects are near zero, do not declare the judge permanently fair. Say something narrower: in this audit, for these labels, on these examples, we did not find a meaningful label effect. If label effects are large or one-directional, do not just average them away. Change the evaluation process. Hide irrelevant labels by default. Use neutral IDs. Separate content review from identity review. Run multiple judges. Keep human review for borderline or high-impact cases. Re-audit when the model, prompt, rubric, or domain changes. And if you discover a floor-raising pattern, where a favorable label mostly helps weaker work, pay special attention.'''
    },
    {
        'title': 'A tiny spreadsheet version',
        'kicker': 'One sheet can turn a vague concern into evidence.',
        'kind': 'sheet',
        'bullets': [
            'Columns: item ID, text, label condition, score, pair ID, difference.',
            'Summary: average difference, positive count, negative count, notes by dimension.',
            'You do not need a giant benchmark to begin.',
        ],
        'narration': '''Here is the whole audit in spreadsheet form. Column one: item ID. Column two: original text. Column three: label condition, such as A or B. Column four: judge score. Column five: paired item ID. Column six: paired difference. Then add a small summary: average paired difference, number of positive differences, number of negative differences, and notes by rubric dimension. That is enough to turn a vague fairness concern into evidence. You do not need a giant benchmark to begin. You need paired examples, a stable rubric, and the humility to check whether your judge responds to things it should ignore.'''
    },
    {
        'title': 'What this audit cannot prove',
        'kicker': 'Useful diagnostic, not a certificate of fairness.',
        'kind': 'limits',
        'bullets': [
            'It only tests the labels you swap and the examples you include.',
            'It can miss content, dialect, topic, format, or hidden-correlation bias.',
            'Noisy judges need repeats; high-stakes systems need deeper review.',
        ],
        'narration': '''A label-swap audit is useful, but it is not magic. It only tests the labels you swap. It only covers the examples you include. It can miss biases that come from content, dialect, topic, format, or hidden correlations. It can also be noisy if the judge is inconsistent from run to run. So treat it as one diagnostic, not a certificate of fairness. Still, it is a powerful diagnostic because it asks a causal question in a simple way: same work, different label, different score? That is much better than arguing about whether the judge seems objective.'''
    },
    {
        'title': 'Make the irrelevant invisible',
        'kicker': 'Then test whether invisible would have mattered.',
        'kind': 'close',
        'bullets': [
            'If a label should not matter, hide it.',
            'If it might matter anyway, run paired label swaps.',
            'If it moves scores, redesign before scores change outcomes.',
        ],
        'narration': '''If you use AI judges, the practical rule is simple. Make the irrelevant invisible. Test whether invisible would have mattered. And when a label changes the score, redesign the process before the score changes someone’s outcome. A small audit will not solve every evaluation problem. But it can catch a failure mode that ordinary dashboards hide. Same work. Different label. Different score. That is the signal to look for.'''
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


def draw_kind(draw, kind):
    if kind == 'hook':
        rr(draw, (680, 330, 1240, 620), 36, (20, 26, 45), ACCENT, 5)
        draw.text((960, 425), 'Same work', font=font(56, True), fill=TEXT, anchor='mm')
        draw.text((960, 500), 'Different label', font=font(56, True), fill=ACCENT, anchor='mm')
        draw.text((960, 575), 'Different score?', font=font(56, True), fill=YELLOW, anchor='mm')
    elif kind == 'decision':
        labels = [('Answer text', GREEN), ('Rubric', GREEN), ('Evidence', GREEN), ('Model name', RED), ('Vendor', RED), ('Reputation', RED)]
        for i, (txt, color) in enumerate(labels):
            x = 250 + (i % 3) * 480
            y = 350 + (i // 3) * 130
            rr(draw, (x, y, x+390, y+82), 20, (22, 29, 48), color, 3)
            draw.text((x+195, y+41), txt, font=font(34, True), fill=color, anchor='mm')
        draw.text((960, 670), 'Green: should matter   Red: should not matter', font=font(32, True), fill=MUTED, anchor='mm')
    elif kind == 'rubric':
        x, y = 260, 330
        colw = [480, 280, 620]
        rows = [('Dimension', 'Scale', 'Endpoint definition'), ('Correctness', '1–5', '5 = fully correct; 1 = wrong or unsupported'), ('Clarity', '1–5', '5 = easy to follow; 1 = confusing'), ('Constraints', '1–5', '5 = follows all instructions; 1 = ignores them')]
        for r, row in enumerate(rows):
            yy = y + r*90
            fill = (35, 45, 68) if r == 0 else (20, 27, 45)
            rr(draw, (x, yy, x+sum(colw), yy+72), 12, fill, (67, 82, 120), 1)
            xx = x+22
            for c, val in enumerate(row):
                draw.text((xx, yy+36), val, font=font(28, r == 0), fill=TEXT if r == 0 else MUTED, anchor='lm')
                xx += colw[c]
    elif kind == 'pairs':
        for x, lab, color in [(280, 'Label A\nTrusted vendor', PURPLE), (1080, 'Label B\nNew vendor', ORANGE)]:
            rr(draw, (x, 340, x+560, 600), 30, (246, 248, 255), color, 5)
            draw.text((x+280, 420), 'Exact same work', font=font(42, True), fill=(20, 24, 40), anchor='mm')
            draw_wrapped(draw, lab, (x+90, 492), font(35, True), color, 18, line_gap=6)
        draw.line((860, 470, 1060, 470), fill=YELLOW, width=8)
        draw.polygon([(1060,470),(1015,443),(1015,497)], fill=YELLOW)
        draw.text((960, 675), 'Only one thing changes.', font=font(42, True), fill=YELLOW, anchor='mm')
    elif kind == 'differences':
        draw.text((960, 335), 'difference = score(label A) − score(label B)', font=font(50, True), fill=YELLOW, anchor='mm')
        vals = [0.0, 0.4, -0.2, 0.8, 0.1, 0.6, -0.1, 0.5]
        base_y = 640
        draw.line((360, base_y, 1560, base_y), fill=(130, 140, 160), width=3)
        for i, v in enumerate(vals):
            cx = 420 + i*155
            h = int(v*260)
            color = GREEN if v > 0 else RED if v < 0 else MUTED
            y0, y1 = (base_y-h, base_y) if h >= 0 else (base_y, base_y-h)
            rr(draw, (cx-35, y0, cx+35, y1), 8, color, None, 1)
        draw.text((960, 705), 'paired differences reveal label movement', font=font(34, True), fill=MUTED, anchor='mm')
    elif kind == 'actions':
        items = [('Hide labels', ACCENT), ('Neutral IDs', PURPLE), ('Multiple judges', GREEN), ('Human review', YELLOW), ('Re-audit', ORANGE)]
        for i, (txt, color) in enumerate(items):
            x = 250 + (i % 3) * 470
            y = 345 + (i // 3) * 140
            rr(draw, (x, y, x+360, y+90), 24, (22, 29, 48), color, 3)
            draw.text((x+60, y+45), '✓', font=font(48, True), fill=color, anchor='mm')
            draw.text((x+205, y+45), txt, font=font(32, True), fill=TEXT, anchor='mm')
    elif kind == 'sheet':
        x, y = 145, 335
        cols = ['item', 'label', 'score', 'pair', 'diff']
        widths = [300, 300, 250, 300, 250]
        rows = [['17A','A: trusted','4.6','17','+0.7'], ['17B','B: new','3.9','17','+0.7'], ['22A','A: trusted','3.2','22','−0.1'], ['22B','B: new','3.3','22','−0.1']]
        xx = x
        for c, w in zip(cols, widths):
            rr(draw, (xx, y, xx+w, y+70), 8, (35,45,68), (70,85,120), 1)
            draw.text((xx+20, y+35), c, font=font(30, True), fill=TEXT, anchor='lm')
            xx += w
        for r, row in enumerate(rows):
            xx = x; yy = y + 78 + r*68
            for val, w in zip(row, widths):
                rr(draw, (xx, yy, xx+w, yy+58), 6, (18,24,40), (45,58,88), 1)
                fill = GREEN if val.startswith('+') else RED if val.startswith('−') else MUTED
                draw.text((xx+20, yy+29), val, font=font(28, True if val.startswith(('+','−')) else False), fill=fill, anchor='lm')
                xx += w
    elif kind == 'limits':
        rr(draw, (260, 330, 1660, 630), 36, (35, 30, 42), YELLOW, 5)
        draw.text((960, 420), 'Not a certificate', font=font(68, True), fill=YELLOW, anchor='mm')
        draw.text((960, 510), 'A focused diagnostic for labels, examples, prompts, and rubrics you test.', font=font(36, True), fill=TEXT, anchor='mm')
    elif kind == 'close':
        rr(draw, (360, 350, 1560, 590), 38, (20, 26, 45), ACCENT, 4)
        draw.text((960, 430), 'Make the irrelevant invisible.', font=font(60, True), fill=TEXT, anchor='mm')
        draw.text((960, 520), 'Then test whether invisible would have mattered.', font=font(42, True), fill=ACCENT, anchor='mm')


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
    draw.text((960, 1038), 'Practical AI evaluation checklist — same work, different label, different score?', font=font(24), fill=(125, 136, 158), anchor='mm')
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
            run(['ffmpeg','-y','-loop','1','-framerate','1','-i',slide,'-i',aud,'-t',f'{dur:.3f}','-c:v','libx264','-preset','ultrafast','-tune','stillimage','-pix_fmt','yuv420p','-r','24','-vf','scale=1920:1080','-c:a','aac','-b:a','192k','-shortest',clip])
            f.write(f"file '{clip.resolve()}'\n")
    run(['ffmpeg','-y','-f','concat','-safe','0','-i',concat,'-c','copy',FINAL])
    print(FINAL)
    print(f'{duration(FINAL):.3f}')


if __name__ == '__main__':
    os.chdir(ROOT)
    asyncio.run(main())
