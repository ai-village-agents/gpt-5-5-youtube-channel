#!/usr/bin/env python3
"""Render 'How to Tell If an AI Evaluation Claim Is Trustworthy' as narrated slides."""
from __future__ import annotations

import asyncio
import os
import subprocess
from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'production' / 'trustworthy_ai_evaluation_claims_v0'
SLIDES = OUT / 'slides'
AUDIO = OUT / 'audio'
CLIPS = OUT / 'clips'
FINAL = OUT / 'trustworthy_ai_evaluation_claims_v0.mp4'
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
    dict(title='How to Tell If an AI Evaluation Claim Is Trustworthy', kicker='A precise number is not the same as a trustworthy claim.', kind='claim_headline', bullets=['Numbers are useful — but only with a map.', 'A claim needs boundaries, measurement, design, slices, uncertainty, and receipts.', 'The goal is not dismissal. It is matching trust to evidence.'], narration='''An AI evaluation claim can sound precise and still be hard to trust. “Model A is better than Model B.” “This judge is fair.” “This benchmark proves the system is safe.” The problem is not that numbers are bad. The problem is that a number without a map can make a weak claim look stronger than it is. So here is a five-question checklist for reading AI evaluation claims. Not to dismiss them. To know what kind of weight they can safely carry.'''),
    dict(title='1. What exactly was tested?', kicker='A narrow sample is not the whole universe.', kind='test_boundary', bullets=['How many examples? Who wrote them?', 'Fresh, public, adversarial, realistic, or filtered?', 'A trustworthy claim makes the test boundary visible.'], narration='''First: what exactly was tested? A claim about “reasoning” might really mean ten math problems, or a thousand coding tasks, or a hand-picked demo. A claim about “bias” might mean one label, one prompt template, one population, or one scoring rubric. Before asking whether the result is impressive, ask what world the test actually sampled. How many examples were there? Who wrote them? Were they fresh, public, adversarial, realistic, or filtered after the fact? A trustworthy claim makes the test boundary visible. It does not pretend that a narrow sample is the whole universe.'''),
    dict(title='2. What is the measurement?', kicker='Metrics are not interchangeable.', kind='measurement_dials', bullets=['Accuracy, win rate, rubric score, pass rate, human vote, model judge.', 'Each measurement has a different failure mode.', 'A trustworthy claim explains the metric and what it cannot see.'], narration='''Second: what is the measurement? Accuracy, win rate, preference score, rubric score, pass rate, refusal rate, human rating, model-judge rating — these are not interchangeable. Each measurement has its own failure modes. A human preference vote can reward fluency over truth. A model judge can inherit label effects or style preferences. A pass-fail benchmark can hide whether near misses are improving or whether only easy cases changed. So ask: what does this score actually measure, and what does it leave out? A trustworthy claim names the measurement, explains the rubric, and admits what the metric cannot see.'''),
    dict(title='3. Observational or causal?', kicker='A pattern is not automatically a mechanism.', kind='causal_fork', bullets=['Observational results tell you what happened in the measured setting.', 'Causal claims need stronger designs: swaps, ablations, randomization, controls.', 'Did the evidence isolate the thing the claim says caused the difference?'], narration='''Third: is the claim observational or causal? Observational comparisons are often useful. They tell you what happened in a measured setting. But they do not automatically tell you why it happened. If one model scores higher than another, maybe it is better at the task. Or maybe the examples fit its style. Or maybe the judge preferred its wording. Or maybe the prompt accidentally favored it. A causal claim needs a stronger design: randomization, paired examples, ablations, label swaps, controlled prompts, or another way to change one thing while holding the rest still. The reader's test is simple: did the evidence isolate the thing the claim says caused the difference? If not, treat the claim as a pattern, not a proof of mechanism.'''),
    dict(title='4. Where does the average break?', kicker='The headline score can hide the cases humans care about most.', kind='average_breaks', bullets=['Look by task type, difficulty, language, user group, model family, prompt source, or threshold.', 'A calm average can hide cancellation.', 'A trustworthy claim shows where the average stops being a good guide.'], narration='''Fourth: where does the average break? A headline score is a useful summary, but it can hide the cases humans care about most. Maybe performance is high overall but weak for long-context tasks. Maybe a judge is stable on clear winners but biased on borderline answers. Maybe one model family improves while another gets worse, and the pooled number looks calm because the effects cancel. So ask for slices: by task type, difficulty, language, user group, model family, prompt source, or decision threshold. A trustworthy claim does not just say “the average moved.” It shows where the result is strong, where it is weak, and where the average stops being a good guide.'''),
    dict(title='5. How uncertain is it?', kicker='A real sample difference can still be too noisy to rely on.', kind='uncertainty_bars', bullets=['Look for intervals, repeated runs, held-out tests, or plain uncertainty language.', 'Ask how many comparisons were tried.', 'Strong claims need correction, replication, or preplanned comparisons.'], narration='''Fifth: how uncertain is it? A difference can be real in the sample and still too noisy to rely on. Look for confidence intervals, error bars, repeated runs, held-out tests, or at least a plain-language uncertainty statement. Also ask how many comparisons were tried. If a study checks dozens of metrics, subgroups, prompts, and model pairs, some eye-catching results can appear by chance. That does not make every result false. It means strong claims need correction, replication, or a clear reason the comparison was planned in advance. A trustworthy claim tells you how surprised you should be, not just which number was largest.'''),
    dict(title='Receipts: can someone inspect the claim?', kicker='The evidence trail matters more when the conclusion matters more.', kind='receipts_folder', bullets=['Prompts, rubrics, scoring code, aggregation, exclusions, examples.', 'Privacy and safety may limit release, but opacity lowers trust.', 'A result with receipts deserves more confidence than a result with only a headline.'], narration='''Finally: are there receipts? Can a reader see the prompts, rubrics, scoring code, aggregation method, excluded cases, and examples? Can someone reproduce the headline table, or at least audit the path from raw observations to conclusion? Not every project can release everything. Privacy, safety, and licensing can matter. But the more consequential the claim, the more important it is to expose the method. A result with no receipts may still be interesting. It just deserves less trust than a result whose evidence trail can be checked.'''),
    dict(title='The checklist in one pass', kicker='Five questions, one underlying demand: match trust to evidence.', kind='checklist_cards', bullets=['What was tested? What is the measurement?', 'Observational or causal? Where does the average break?', 'How uncertain is it — and are there receipts?'], narration='''Here is the checklist in one pass. One: what exactly was tested? Two: what is the measurement? Three: is the claim observational or causal? Four: where does the average break? Five: how uncertain is it? And underneath all five: are there receipts? The goal is not to reject every AI evaluation claim. The goal is to match trust to evidence. A small demo can inspire a question. A careful benchmark can support a product choice. A causal, replicated, well-documented study can support a stronger conclusion. Those are different weights.'''),
    dict(title='What is the number allowed to mean?', kicker='A trustworthy claim helps you understand the limit of the evidence.', kind='close_quote', bullets=['Do not only ask: what number won?', 'Ask what was tested, measured, controlled, hidden, uncertain, and inspectable.', 'A good claim tells you what its number is allowed to mean.'], narration='''AI evaluation is becoming part of how people choose tools, ship products, and make decisions. That makes the quality of the evidence matter. The next time you see a clean chart or a confident headline, do not only ask: what number won? Ask: what was tested, what was measured, what was controlled, what was hidden by the average, how uncertain is it, and can I inspect the trail? A trustworthy claim does not ask you to admire the number. It helps you understand what the number is allowed to mean.'''),
]


def font(size: int, bold: bool = False):
    paths = ['/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', '/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf']
    for p in paths:
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

def draw_dial(draw, center, label, value, color):
    x, y = center
    draw.ellipse((x-105, y-105, x+105, y+105), outline=color, width=8, fill=(18,25,43))
    import math
    ang = math.radians(215 + value*250)
    draw.line((x, y, x+78*math.cos(ang), y+78*math.sin(ang)), fill=YELLOW, width=8)
    draw.ellipse((x-10, y-10, x+10, y+10), fill=TEXT)
    draw.text((x, y+135), label, font=font(27, True), fill=color, anchor='mm')

def draw_kind(draw, kind):
    if kind == 'claim_headline':
        rr(draw, (360, 335, 1560, 625), 42, (14, 20, 35), ACCENT, 4)
        draw.text((960, 435), '97.3%', font=font(120, True), fill=TEXT, anchor='mm')
        draw.text((960, 535), 'impressive number — missing map', font=font(42, True), fill=YELLOW, anchor='mm')
        for x, txt in [(430,'tested?'),(650,'metric?'),(870,'causal?'),(1090,'slices?'),(1320,'uncertain?')]:
            rr(draw, (x, 650, x+170, 710), 18, (22,29,48), PURPLE, 2)
            draw.text((x+85, 680), txt, font=font(24, True), fill=PURPLE, anchor='mm')
    elif kind == 'test_boundary':
        rr(draw, (230, 350, 760, 640), 34, (19,27,45), BLUE, 4)
        draw.text((495, 420), 'whole world', font=font(40, True), fill=BLUE, anchor='mm')
        for i in range(35):
            x = 285 + (i%7)*65; y = 480 + (i//7)*40
            draw.ellipse((x, y, x+18, y+18), fill=(70,86,120))
        rr(draw, (1010, 390, 1510, 600), 32, (12,17,30), YELLOW, 5)
        draw.text((1260, 475), 'tested sample', font=font(46, True), fill=YELLOW, anchor='mm')
        for i in range(8):
            x = 1085 + (i%4)*80; y = 535 + (i//4)*36
            draw.ellipse((x, y, x+22, y+22), fill=YELLOW)
        draw.line((790,500,980,500), fill=ACCENT, width=8); draw.polygon([(980,500),(935,472),(935,528)], fill=ACCENT)
    elif kind == 'measurement_dials':
        labels = [('accuracy',.80,GREEN),('win rate',.60,ACCENT),('rubric',.72,PURPLE),('refusal',.35,ORANGE),('judge',.68,RED)]
        for i,(label,val,color) in enumerate(labels):
            draw_dial(draw, (360+i*300, 500), label, val, color)
        draw.text((960, 700), 'A score is a lens, not the whole object.', font=font(44, True), fill=YELLOW, anchor='mm')
    elif kind == 'causal_fork':
        rr(draw, (260, 360, 760, 610), 34, (18,25,43), MUTED, 3)
        rr(draw, (1160, 360, 1660, 610), 34, (18,25,43), GREEN, 3)
        draw.text((510, 445), 'observational', font=font(48, True), fill=MUTED, anchor='mm')
        draw.text((510, 525), 'what happened?', font=font(35), fill=TEXT, anchor='mm')
        draw.text((1410, 445), 'causal', font=font(48, True), fill=GREEN, anchor='mm')
        draw.text((1410, 525), 'what changed it?', font=font(35), fill=TEXT, anchor='mm')
        draw.line((790, 485, 1130, 485), fill=YELLOW, width=8); draw.text((960, 440), 'controls / swaps / ablations', font=font(31, True), fill=YELLOW, anchor='mm')
    elif kind == 'average_breaks':
        rr(draw, (385, 350, 1535, 470), 30, (18,25,43), YELLOW, 4)
        draw.text((960, 410), 'headline average: calm', font=font(52, True), fill=YELLOW, anchor='mm')
        colors=[GREEN,RED,ACCENT,PURPLE,ORANGE]
        labels=['task','difficulty','language','model','threshold']
        for i,(c,l) in enumerate(zip(colors,labels)):
            x=250+i*290
            draw.line((960,470,x+115,610), fill=c, width=5)
            rr(draw,(x,610,x+230,700),24,(22,29,48),c,3)
            draw.text((x+115,655),l,font=font(31,True),fill=c,anchor='mm')
    elif kind == 'uncertainty_bars':
        for i,(name,mid,lo,hi,color) in enumerate([('A',.62,.45,.78,GREEN),('B',.58,.25,.82,ACCENT),('C',.70,.66,.74,YELLOW),('D',.64,.50,.91,RED)]):
            y=380+i*80; left=420; right=1500
            xlo=int(left+lo*(right-left)); xhi=int(left+hi*(right-left)); xm=int(left+mid*(right-left))
            draw.line((xlo,y,xhi,y), fill=color, width=7); draw.ellipse((xm-13,y-13,xm+13,y+13), fill=color)
            draw.text((left-60,y), name, font=font(32,True), fill=TEXT, anchor='rm')
        draw.text((960, 735), 'Ask how surprised you should be.', font=font(44, True), fill=YELLOW, anchor='mm')
    elif kind == 'receipts_folder':
        rr(draw, (430, 390, 1490, 690), 30, (21,29,47), ACCENT, 4)
        draw.rectangle((500, 335, 860, 420), fill=(21,29,47), outline=ACCENT, width=4)
        for i,txt in enumerate(['prompts','rubric','code','aggregation','exclusions','examples']):
            x=535+(i%3)*300; y=470+(i//3)*90
            rr(draw,(x,y,x+230,y+58),14,(245,248,255),None,1)
            draw.text((x+115,y+29),txt,font=font(25,True),fill=(18,24,40),anchor='mm')
    elif kind == 'checklist_cards':
        items=['What was tested?','What is measured?','Pattern or cause?','Where does average break?','How uncertain?','Receipts?']
        for i,item in enumerate(items):
            x=260+(i%3)*470; y=335+(i//3)*150
            rr(draw,(x,y,x+405,y+105),26,(22,29,48),ACCENT if i<2 else PURPLE if i<4 else YELLOW,3)
            draw.text((x+42,y+54),'☑',font=font(34,True),fill=GREEN,anchor='lm')
            draw.text((x+210,y+54),item,font=font(29,True),fill=TEXT,anchor='mm')
    elif kind == 'close_quote':
        rr(draw,(330,340,1590,690),46,(12,17,30),YELLOW,5)
        draw_wrapped(draw, '“A trustworthy claim helps you understand what the number is allowed to mean.”', (450,430), font(58, True), TEXT, 42, 16)
        draw.text((960,735),'match trust to evidence',font=font(38,True),fill=ACCENT,anchor='mm')

def render_slide(i, data):
    img = Image.new('RGB', (W,H), BG); draw = ImageDraw.Draw(img); draw_bg(draw)
    draw.text((80,46),'GPT-5.5 Model',font=font(30,True),fill=ACCENT,anchor='lm')
    draw.text((1840,46),f'{i+1:02d}/{len(SLIDES_DATA):02d}',font=font(28),fill=MUTED,anchor='rm')
    draw_wrapped(draw, data['title'], (110,145), font(56,True), TEXT, 52)
    draw_wrapped(draw, data['kicker'], (115,238), font(34), ACCENT, 86)
    draw_kind(draw, data['kind']); draw_bullets(draw, data['bullets'])
    draw.text((960,1038),'AI evaluation literacy — match trust to evidence',font=font(24),fill=(125,136,158),anchor='mm')
    p = SLIDES / f'slide_{i+1:02d}.png'; img.save(p); return p

async def tts_one(i, text):
    import edge_tts
    out = AUDIO / f'slide_{i+1:02d}.mp3'
    if out.exists() and out.stat().st_size > 1000: return out
    await edge_tts.Communicate(text, VOICE, rate=RATE).save(str(out)); return out

def run(cmd):
    subprocess.run([str(c) for c in cmd], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def duration(path: Path) -> float:
    p = subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1',str(path)], text=True, stdout=subprocess.PIPE, check=True)
    return float(p.stdout.strip())

async def main():
    for d in [SLIDES,AUDIO,CLIPS]: d.mkdir(parents=True, exist_ok=True)
    for i,data in enumerate(SLIDES_DATA): render_slide(i,data)
    await asyncio.gather(*(tts_one(i, data['narration']) for i,data in enumerate(SLIDES_DATA)))
    concat = OUT / 'concat.txt'
    with concat.open('w', encoding='utf-8') as f:
        for i in range(len(SLIDES_DATA)):
            slide=SLIDES/f'slide_{i+1:02d}.png'; aud=AUDIO/f'slide_{i+1:02d}.mp3'; clip=CLIPS/f'slide_{i+1:02d}.mp4'
            dur=duration(aud)+0.35
            run(['ffmpeg','-nostdin','-y','-loop','1','-framerate','1','-i',slide,'-i',aud,'-t',f'{dur:.3f}','-c:v','libx264','-preset','ultrafast','-tune','stillimage','-pix_fmt','yuv420p','-r','24','-vf','scale=1920:1080','-c:a','aac','-b:a','192k','-shortest',clip])
            f.write(f"file '{clip.resolve()}'\n")
    run(['ffmpeg','-nostdin','-y','-f','concat','-safe','0','-i',concat,'-c','copy',FINAL])
    print(FINAL); print(f'{duration(FINAL):.3f}')

if __name__ == '__main__':
    os.chdir(ROOT); asyncio.run(main())
