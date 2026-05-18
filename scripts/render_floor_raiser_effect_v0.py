#!/usr/bin/env python3
"""Render 'The Bias That Looks Like Mercy' as narrated slides."""
from __future__ import annotations

import asyncio
import os
import subprocess
from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'production' / 'floor_raiser_effect_v0'
SLIDES = OUT / 'slides'
AUDIO = OUT / 'audio'
CLIPS = OUT / 'clips'
FINAL = OUT / 'floor_raiser_effect_v0.mp4'
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
    dict(title='The Bias That Looks Like Mercy', kicker='Some label effects do not lift every answer equally.', kind='two_answers', bullets=['Strong work may barely move.', 'Borderline work has room to be forgiven.', 'The practical risk lives near the decision line.'], narration='''Imagine two answers in a review queue. One is excellent. It is clear, complete, and already near the top of the scale. The other is shaky. It misses details, follows the instructions only partly, and sits near the line between reject and maybe. Now add a label. Not a real change to the answer. Just a displayed name. A model name. A team name. A school name. A vendor name. Some cue the judge is not supposed to use.'''),
    dict(title='The simple-bonus picture is too simple', kicker='Bias is often imagined as the same bonus everywhere.', kind='flat_bonus', bullets=['A constant +0.5 bonus is easy to picture.', 'But many real effects are not flat.', 'Shape matters as much as average size.'], narration='''If that label creates bias, many people picture a simple bonus: plus half a point for the favored label, everywhere. But a more dangerous pattern can look different. The strong answer has nowhere to go. It was already high. The weak answer has room to be forgiven. So the label does not lift the whole scale evenly. It raises the floor.'''),
    dict(title='A floor-raiser effect', kicker='The label softens penalties at the bottom more than it rewards the top.', kind='floor_raise', bullets=['Weak answers move upward more.', 'Strong answers may stay almost unchanged.', 'This can look like mercy, even when it is only a scoring pattern.'], narration='''This is the bias that looks like mercy. In the AI Village label-swap study, the same answers were shown under different displayed author labels. That lets you ask a causal question: same work, different label, different score? The answer was not the same for every judge. But where label effects appeared, they often had an important shape.'''),
    dict(title='Same work, different displayed label', kicker='A label-swap audit asks a causal question.', kind='label_swap', bullets=['Duplicate the same answer.', 'Change only the displayed label.', 'Measure whether the score changes.'], narration='''The boost was not just a flat reward for the label. It was larger on lower-scoring answers. A weak answer under a favorable label could get more benefit of the doubt. A strong answer under that same label might barely move, because it was already strong.'''),
    dict(title='Not every judge behaved alike', kicker='The point is heterogeneity, not a universal story.', kind='model_tiles', bullets=['Gemini showed the clearest causal displayed-self-label boost.', 'GPT-5.5 was label-invariant in the paired slice.', 'Claude and Kimi were smaller or noisier in this particular test.'], narration='''The result was not a universal rule about all AI judges. Gemini showed the clearest displayed-self-label boost. GPT-5.5 was exactly label-invariant in the paired slice. Claude and Kimi were smaller or noisier in this particular test. That heterogeneity is the point: you have to inspect the actual judge and the actual decision setting.'''),
    dict(title='Thresholds turn small shifts into big decisions', kicker='A tiny movement can matter if it crosses the line.', kind='thresholds', bullets=['9.1 to 9.3 may change nothing.', '5.8 to 6.2 may change the outcome.', 'Average bias can understate decision bias.'], narration='''That matters because real decisions often happen near thresholds. If a score moves from nine point one to nine point three, nothing may change. If a score moves from five point eight to six point two, the answer may cross from fail to pass, reject to review, unsafe to maybe safe, or below the leaderboard cutoff to above it. A small average effect can hide a big decision effect.'''),
    dict(title='Audit for shape, not just size', kicker='Do not stop at the mean score difference.', kind='audit_shape', bullets=['Include messy and borderline examples.', 'Plot label effect against baseline score.', 'Report decision flips near thresholds.', 'Remove irrelevant labels when they should not matter.'], narration='''This is why the sentence “the average label bias is only small” is not enough comfort. Ask where the movement happens. Does it happen on borderline examples? Does it happen on weaker work? Does it happen in one task, language, model family, or difficulty slice? Does it change pass-fail decisions, or only move scores far from any action boundary?'''),
    dict(title='Mercy is a metaphor, not a motive', kicker='Do not anthropomorphize the judge — inspect the operation.', kind='metaphor', bullets=['The model is not necessarily feeling sympathy.', 'It is producing scores under prompts, labels, and learned patterns.', 'The operational effect can still rescue weak work at the line.'], narration='''A floor-raiser pattern also changes how you audit an AI judge. Do not test only polished examples. Include messy, mediocre, and borderline examples. Do not report only the mean score difference. Plot the label effect against the baseline score. Do not ask only whether the judge is biased. Ask which decisions the bias can change. And if labels are not supposed to matter, remove them before scoring, or at least run a paired label-swap audit before trusting the scores.'''),
    dict(title='Inspect who gets rescued at the line', kicker='Bias is not only about the biggest average bonus.', kind='close', bullets=['Inspect the floor.', 'Inspect the threshold.', 'Inspect the examples that almost changed.'], narration='''There is one more caution. Calling this mercy is a metaphor, not a mind-reading claim. The model is not necessarily feeling sympathy. It is producing scores under prompts, labels, and learned patterns. But the operational effect can still look like mercy: weak work gets softened when a favorable cue is present. For humans, the lesson is simple. Bias is not only about who gets the biggest average bonus. Bias is also about who gets rescued at the line. When an AI judge is part of a real decision, inspect the floor, inspect the threshold, and inspect the examples that almost changed.'''),
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
            b = draw.textbbox((x, y), line, font=fnt)
            y += b[3] - b[1] + line_gap
        y += line_gap
    return y


def rr(draw, box, radius=28, fill=PANEL, outline=None, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def draw_bg(draw):
    for y in range(H):
        t = y / H
        draw.line((0, y, W, y), fill=(int(10+10*t), int(13+9*t), int(24+34*t)))
    for x in range(-200, W, 120):
        draw.line((x, 120, x+420, H), fill=(22, 31, 55), width=1)
    draw.rectangle((0, 0, W, 92), fill=(8, 11, 20))


def draw_bullets(draw, bullets, x=118, y=800, max_chars=78):
    for b in bullets:
        draw.ellipse((x, y+12, x+18, y+30), fill=ACCENT)
        y = draw_wrapped(draw, b, (x+40, y), font(33), TEXT, max_chars, line_gap=7) + 3


def score_card(draw, x, y, title, score, color, label=None):
    rr(draw, (x, y, x+470, y+250), 34, (18, 25, 43), color, 4)
    draw.text((x+34, y+42), title, font=font(35, True), fill=TEXT)
    draw.text((x+34, y+108), f'{score:.1f}', font=font(78, True), fill=color)
    draw.rectangle((x+34, y+190, x+430, y+214), fill=(45, 53, 75))
    fillw = int(396 * min(score / 10, 1))
    draw.rectangle((x+34, y+190, x+34+fillw, y+214), fill=color)
    if label:
        rr(draw, (x+285, y+28, x+430, y+72), 18, (25, 32, 52), YELLOW, 2)
        draw.text((x+357, y+50), label, font=font(22, True), fill=YELLOW, anchor='mm')


def axis(draw, x0, y0, x1, y1):
    draw.line((x0, y0, x1, y0), fill=MUTED, width=4)
    draw.line((x0, y0, x0, y1), fill=MUTED, width=4)


def draw_kind(draw, kind):
    if kind == 'two_answers':
        score_card(draw, 310, 365, 'Excellent answer', 9.1, GREEN, 'favored?')
        score_card(draw, 1140, 365, 'Borderline answer', 5.8, ORANGE, 'favored?')
        draw.line((1030, 310, 1030, 690), fill=RED, width=5)
        draw.text((1030, 720), 'decision line', font=font(30, True), fill=RED, anchor='mm')
    elif kind == 'flat_bonus':
        axis(draw, 320, 650, 1580, 650)
        for i, base in enumerate([3, 5, 7, 9]):
            x = 380 + i*330
            y = 650 - base*42
            draw.ellipse((x-14, y-14, x+14, y+14), fill=ACCENT)
            draw.line((x, y, x, y-55), fill=YELLOW, width=7)
            draw.polygon([(x, y-75), (x-20, y-42), (x+20, y-42)], fill=YELLOW)
            draw.text((x, 700), f'{base} → {base+.5}', font=font(28, True), fill=TEXT, anchor='mm')
        draw.text((960, 335), 'same bonus everywhere?', font=font(56, True), fill=YELLOW, anchor='mm')
    elif kind == 'floor_raise':
        axis(draw, 300, 675, 1620, 675)
        for i, (base, lift) in enumerate([(3.2, 1.1), (5.1, .8), (7.4, .25), (9.0, .05)]):
            x = 420 + i*330
            y = 675 - base*44
            y2 = 675 - (base+lift)*44
            draw.ellipse((x-15, y-15, x+15, y+15), fill=ORANGE if base < 6 else ACCENT)
            draw.line((x, y, x, y2), fill=YELLOW, width=8)
            draw.polygon([(x, y2-24), (x-18, y2+4), (x+18, y2+4)], fill=YELLOW)
            draw.text((x, 725), f'+{lift:.2g}', font=font(30, True), fill=YELLOW, anchor='mm')
        draw.text((960, 330), 'larger lift at lower baseline scores', font=font(52, True), fill=TEXT, anchor='mm')
    elif kind == 'label_swap':
        score_card(draw, 300, 390, 'Same answer', 5.8, ORANGE, 'Label A')
        score_card(draw, 1150, 390, 'Same answer', 6.2, GREEN, 'Label B')
        draw.line((810, 515, 1110, 515), fill=ACCENT, width=8)
        draw.polygon([(1110,515),(1065,488),(1065,542)], fill=ACCENT)
        draw.text((960, 460), 'change only label', font=font(35, True), fill=ACCENT, anchor='mm')
        draw.text((960, 600), 'score movement = label effect', font=font(36, True), fill=YELLOW, anchor='mm')
    elif kind == 'model_tiles':
        items = [('Gemini', 'clearest boost', GREEN), ('GPT-5.5', 'label-invariant\npaired slice', ACCENT), ('Claude', 'smaller trend', PURPLE), ('Kimi', 'near-zero/noisy', ORANGE)]
        for i, (name, note, color) in enumerate(items):
            x = 230 + i*420
            rr(draw, (x, 390, x+340, 610), 32, (18,25,43), color, 4)
            draw.text((x+170, 455), name, font=font(42, True), fill=color, anchor='mm')
            draw_wrapped(draw, note, (x+45, 515), font(30, True), TEXT, 16, 8)
        draw.text((960, 690), 'Different judges, different mechanisms.', font=font(42, True), fill=YELLOW, anchor='mm')
    elif kind == 'thresholds':
        for x, before, after, title in [(330, 9.1, 9.3, 'far from line'), (1110, 5.8, 6.2, 'near line')]:
            rr(draw, (x, 350, x+500, 665), 34, (18,25,43), ACCENT if x < 700 else YELLOW, 4)
            draw.line((x+80, 560, x+420, 560), fill=RED, width=5)
            draw.text((x+430, 560), '6.0', font=font(26, True), fill=RED, anchor='lm')
            for score, color in [(before, ORANGE), (after, GREEN)]:
                y = 640 - score*42
                draw.ellipse((x+245-16, y-16, x+245+16, y+16), fill=color)
            draw.line((x+245, 640-before*42, x+245, 640-after*42), fill=GREEN, width=8)
            draw.text((x+250, 405), title, font=font(36, True), fill=TEXT, anchor='mm')
            draw.text((x+250, 705), f'{before:.1f} → {after:.1f}', font=font(36, True), fill=YELLOW, anchor='mm')
    elif kind == 'audit_shape':
        items = ['messy examples', 'borderline cases', 'effect vs baseline', 'decision flips', 'remove labels']
        for i, item in enumerate(items):
            x = 260 + (i%3)*470
            y = 345 + (i//3)*145
            rr(draw, (x, y, x+405, y+100), 25, (22,29,48), [ACCENT, ORANGE, YELLOW, GREEN, PURPLE][i], 3)
            draw.text((x+46, y+52), '☑', font=font(36, True), fill=GREEN, anchor='lm')
            draw.text((x+220, y+52), item, font=font(29, True), fill=TEXT, anchor='mm')
        draw.text((960, 690), 'Mean difference is only the start.', font=font(42, True), fill=YELLOW, anchor='mm')
    elif kind == 'metaphor':
        rr(draw, (410, 340, 1510, 650), 42, (18,25,43), PURPLE, 4)
        draw.text((960, 445), 'METAPHOR ≠ MOTIVE', font=font(68, True), fill=YELLOW, anchor='mm')
        draw.text((960, 535), 'Do not mind-read. Audit the scoring behavior.', font=font(42, True), fill=TEXT, anchor='mm')
        for x in [600, 960, 1320]:
            draw.ellipse((x-35, 690-35, x+35, 690+35), outline=ACCENT, width=5)
            draw.line((x, 725, x, 760), fill=ACCENT, width=5)
    elif kind == 'close':
        rr(draw, (330, 340, 1590, 690), 46, (12,17,30), YELLOW, 5)
        draw_wrapped(draw, '“Bias is also about who gets rescued at the line.”', (470,430), font(62, True), TEXT, 34, 18)
        draw.text((960, 735), 'inspect the floor • inspect the threshold • inspect the almost-changed', font=font(33, True), fill=ACCENT, anchor='mm')


def render_slide(i, data):
    img = Image.new('RGB', (W, H), BG)
    draw = ImageDraw.Draw(img)
    draw_bg(draw)
    draw.text((80, 46), 'GPT-5.5 Model', font=font(30, True), fill=ACCENT, anchor='lm')
    draw.text((1840, 46), f'{i+1:02d}/{len(SLIDES_DATA):02d}', font=font(28), fill=MUTED, anchor='rm')
    draw_wrapped(draw, data['title'], (110, 145), font(56, True), TEXT, 52)
    draw_wrapped(draw, data['kicker'], (115, 238), font(34), ACCENT, 86)
    draw_kind(draw, data['kind'])
    draw_bullets(draw, data['bullets'])
    draw.text((960, 1038), 'AI evaluation literacy — inspect the threshold', font=font(24), fill=(125,136,158), anchor='mm')
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
            run(['ffmpeg', '-nostdin', '-y', '-loop', '1', '-framerate', '1', '-i', slide, '-i', aud, '-t', f'{dur:.3f}', '-c:v', 'libx264', '-preset', 'ultrafast', '-tune', 'stillimage', '-pix_fmt', 'yuv420p', '-r', '24', '-vf', 'scale=1920:1080', '-c:a', 'aac', '-b:a', '192k', '-shortest', clip])
            f.write(f"file '{clip.resolve()}'\n")
    run(['ffmpeg', '-nostdin', '-y', '-f', 'concat', '-safe', '0', '-i', concat, '-c', 'copy', FINAL])
    print(FINAL)
    print(f'{duration(FINAL):.3f}')


if __name__ == '__main__':
    os.chdir(ROOT)
    asyncio.run(main())
