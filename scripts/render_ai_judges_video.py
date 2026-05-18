#!/usr/bin/env python3
"""Render the first GPT-5.5 YouTube explainer as slides + TTS narration.

This script intentionally keeps dependencies simple: Pillow + ffmpeg + edge-tts.
It writes intermediate slide PNGs, narration MP3s, per-slide MP4s, and a final draft MP4.
"""
from __future__ import annotations

import asyncio
import math
import os
import shutil
import subprocess
from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "production" / "ai_judges_play_favorites"
SLIDES = OUT / "slides"
AUDIO = OUT / "audio"
CLIPS = OUT / "clips"
FINAL = OUT / "ai_judges_play_favorites_draft.mp4"

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
MODEL_COLORS = {
    "Claude": PURPLE,
    "Gemini": ACCENT,
    "GPT-5.5": GREEN,
    "Kimi": ORANGE,
}

VOICE = "en-US-GuyNeural"
RATE = "+0%"

SLIDE_DATA = [
    {
        "title": "Do AI judges play favorites?",
        "kicker": "Same answer. Different name tag. Different score?",
        "bullets": [
            "Four AI model families wrote answers.",
            "Four AI model families judged them.",
            "Then we changed only the displayed author label.",
        ],
        "narration": "Imagine asking four advanced AI systems to grade each other's answers. Now imagine secretly changing the name tag above each answer. Same words. Same prompt. Same rubric. Different label. Would the judge give its own name a little extra credit? We tested that question across four frontier model families. The answer was not a simple yes. It was more interesting, and more useful.",
    },
    {
        "title": "The experiment",
        "kicker": "10 prompts × 4 authors × 4 judges",
        "bullets": [
            "Prompts covered coding, math, ethics, design, creative writing, history, and explanation.",
            "Each answer was scored on correctness, completeness, clarity, creativity, and constraint adherence.",
            "We separated ordinary blind scoring from a causal label-swap test.",
        ],
        "narration": "The study used ten out-of-distribution prompts: coding, math, ethics, design, creative writing, history, explanation, and more. Four systems answered every prompt. Then four systems judged the responses using the same five-part rubric. The key was separating two questions: what happens in ordinary blind scoring, and what happens when we hold the text fixed and only change the displayed author label?",
    },
    {
        "title": "First result: no single global answer",
        "kicker": "Blind baseline self-preference gaps",
        "chart": "c1_bars",
        "bullets": [
            "Claude, Gemini, and GPT showed positive raw self-gaps.",
            "Kimi showed a large negative raw self-gap.",
            "The average hid the real story: judge-family heterogeneity.",
        ],
        "narration": "In the blind baseline, the average self-preference gap was small and noisy. But the average hid a split. Claude showed a large positive self-gap. GPT-5.5 showed a positive self-gap. Gemini showed a smaller positive gap. Kimi showed a large negative gap. So if you only ask whether AI judges prefer themselves on average, you miss the main result. The main result is heterogeneity.",
    },
    {
        "title": "Why raw gaps can mislead",
        "kicker": "Kimi's apparent self-penalty was mostly a quality confound",
        "chart": "kimi_quality",
        "bullets": [
            "Kimi-authored answers were lower-scoring on this prompt set.",
            "Observed Kimi self-gap: −2.87 points.",
            "Quality-adjusted residual: +0.66 points.",
        ],
        "narration": "Kimi looked like it strongly penalized itself in the observational baseline. But Kimi-authored answers were also much lower-scoring on this prompt set. Once we adjusted for that quality difference, Kimi's residual moved positive. That matters because raw self-gaps can mix bias, style, prompt fit, and actual answer quality. To test label bias causally, we needed a cleaner design.",
    },
    {
        "title": "The causal label-swap test",
        "kicker": "Hold the content fixed. Change only the label.",
        "chart": "label_swap_diagram",
        "bullets": [
            "Same response text.",
            "Different displayed author label.",
            "A score change means the label did causal work.",
        ],
        "narration": "The label-swap test asks a stricter question. Take the same answer. Show it once under one author label, and once under another. Then compare the scores within that same response. Now the content is held fixed. If the score moves, the displayed label did something.",
    },
    {
        "title": "The causal results were asymmetric",
        "kicker": "Displayed-self label effect, paired slice",
        "chart": "label_effect_bars",
        "bullets": [
            "Gemini showed the clearest causal self-label boost.",
            "GPT-5.5 was exactly label-invariant in this paired slice.",
            "Claude trended positive; Kimi was near-zero and noisy.",
        ],
        "narration": "This is where the story became sharp. Gemini showed the clearest causal label effect. In the paired slice, the displayed Gemini label raised scores, and the displayed Kimi label lowered them. Claude showed a smaller positive trend, but it was not as robust. Kimi's own displayed-self effect was near zero and noisy. GPT-5.5 was exactly label-invariant in this paired test: the scores did not move when the displayed label changed.",
    },
    {
        "title": "Recognition was not the whole story",
        "kicker": "Gemini barely self-recognized, yet showed the strongest causal label effect",
        "chart": "recognition",
        "bullets": [
            "Gemini self-recognition: 1 out of 10 self cases.",
            "Gemini causal self-label effect: robustly positive.",
            "So the mechanism is not just: 'I know this is mine.'",
        ],
        "narration": "A tempting explanation is that a model favors its own work because it recognizes its own writing. But Gemini complicates that story. In the authorship-recognition task, Gemini only identified its own responses as Gemini in one out of ten self cases. Yet Gemini had the clearest causal displayed-self label effect. So the mechanism cannot be universally reduced to: the model knows this is mine.",
    },
    {
        "title": "The floor-raiser pattern",
        "kicker": "Labels mattered most when quality left room for interpretation",
        "chart": "floor",
        "bullets": [
            "A favorable label did not act like a fixed bonus.",
            "Lower baseline responses received larger uplift.",
            "The effect looked like benefit-of-the-doubt for weaker work.",
        ],
        "narration": "If labels were just a fixed bonus, the uplift would be roughly the same for strong and weak answers. But that is not what we saw. For judges with nonzero label effects, the self-label uplift was larger when the same response's baseline score was lower. Strong answers were already near the ceiling. Weaker answers had more room for interpretation, and a favorable label seemed to buy them more charity. That is why we call it a floor-raising pattern.",
    },
    {
        "title": "What humans should take away",
        "kicker": "AI evaluation can be useful — but not magic",
        "bullets": [
            "Hide irrelevant author labels when possible.",
            "Use multiple judges, not one model family alone.",
            "Separate observational patterns from causal tests.",
            "Look for heterogeneity before trusting a single headline number.",
        ],
        "narration": "The practical lesson is not never use AI judges. The judges still shared meaningful quality signal. The lesson is: do not treat AI evaluation scores as purely objective measurements when labels, styles, and model identities are visible. Hide irrelevant author labels when possible. Use multiple judges. Look for judge-family heterogeneity. Separate observational patterns from causal tests. And be careful with a single headline number.",
    },
    {
        "title": "So, do AI judges play favorites?",
        "kicker": "Sometimes — but not all in the same way.",
        "bullets": [
            "Gemini's displayed label mattered causally.",
            "GPT-5.5's displayed label did not move scores in this paired test.",
            "Kimi's raw self-penalty was mostly answer quality, not causal dislike of its own name.",
            "The clearest mechanism looked like a charitable floor-raiser for weaker work.",
        ],
        "narration": "So, do AI judges play favorites? Sometimes. But not all in the same way. In our test, Gemini's label mattered causally. GPT-5.5's label did not. Kimi's apparent self-penalty was mostly about answer quality, not a causal dislike of its own name. And the clearest mechanism looked less like vanity and more like a charitable floor-raiser for weaker work. That is a messier answer than yes or no. It is also the kind of answer we need if AI systems are going to evaluate more of the world's work.",
    },
]


def font(size: int, bold: bool = False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for c in candidates:
        if Path(c).exists():
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()


def draw_wrapped(draw, text, xy, fnt, fill, max_chars, line_gap=12):
    x, y = xy
    for para in text.split("\n"):
        lines = wrap(para, max_chars) or [""]
        for line in lines:
            draw.text((x, y), line, font=fnt, fill=fill)
            bbox = draw.textbbox((x, y), line, font=fnt)
            y += (bbox[3] - bbox[1]) + line_gap
        y += line_gap
    return y


def rounded_rect(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def draw_bar_chart(draw, x, y, w, h, labels, values, colors, minv=-3.2, maxv=2.6, suffix=""):
    zero = y + h - (0 - minv) / (maxv - minv) * h
    draw.line((x, zero, x + w, zero), fill=(120, 130, 150), width=3)
    bar_w = w / len(labels) * 0.56
    gap = w / len(labels)
    for i, (lab, val, col) in enumerate(zip(labels, values, colors)):
        cx = x + gap * (i + 0.5)
        top = y + h - (val - minv) / (maxv - minv) * h
        bottom = zero
        if val < 0:
            top, bottom = zero, top
        rounded_rect(draw, (cx - bar_w/2, top, cx + bar_w/2, bottom), 10, col)
        draw.text((cx, y + h + 25), lab, font=font(34, True), fill=TEXT, anchor="mt")
        sign = "+" if val > 0 else ""
        draw.text((cx, min(top, bottom) - 50 if val >= 0 else max(top, bottom) + 12), f"{sign}{val:.2f}{suffix}", font=font(32, True), fill=col, anchor="mt")


def draw_chart(draw, kind):
    if kind == "c1_bars":
        draw_bar_chart(
            draw, 250, 360, 1420, 430,
            ["Claude", "Gemini", "GPT-5.5", "Kimi"],
            [2.433, 0.627, 1.327, -2.873],
            [MODEL_COLORS["Claude"], MODEL_COLORS["Gemini"], MODEL_COLORS["GPT-5.5"], MODEL_COLORS["Kimi"]],
        )
        draw.text((960, 835), "Blind C1 self-gap: self-authored score minus other-authored score", font=font(30), fill=MUTED, anchor="mm")
    elif kind == "kimi_quality":
        draw_bar_chart(draw, 290, 380, 600, 360, ["raw gap", "quality-adjusted"], [-2.873, 0.662], [RED, GREEN], minv=-3.2, maxv=1.2)
        rounded_rect(draw, (1040, 365, 1610, 735), 28, PANEL, outline=(64, 80, 120), width=2)
        draw.text((1325, 420), "Why the sign changed", font=font(42, True), fill=TEXT, anchor="mm")
        draw_wrapped(draw, "Kimi's own answers were much lower-scoring on this prompt set. Raw self-gap mixed quality with possible bias.", (1090, 490), font(32), MUTED, 31)
    elif kind == "label_swap_diagram":
        rounded_rect(draw, (260, 430, 780, 650), 30, PANEL, outline=ACCENT, width=4)
        rounded_rect(draw, (1140, 430, 1660, 650), 30, PANEL, outline=GREEN, width=4)
        draw.text((520, 500), "Same response text", font=font(42, True), fill=TEXT, anchor="mm")
        draw.text((1400, 500), "Same response text", font=font(42, True), fill=TEXT, anchor="mm")
        draw.text((520, 585), "Label: Gemini", font=font(36), fill=ACCENT, anchor="mm")
        draw.text((1400, 585), "Label: Kimi", font=font(36), fill=ORANGE, anchor="mm")
        draw.line((820, 540, 1100, 540), fill=YELLOW, width=8)
        draw.polygon([(1100,540),(1050,510),(1050,570)], fill=YELLOW)
        draw.text((960, 710), "If the score changes, the label did causal work.", font=font(38, True), fill=YELLOW, anchor="mm")
    elif kind == "label_effect_bars":
        draw_bar_chart(draw, 250, 360, 1420, 430, ["Claude", "Gemini", "GPT-5.5", "Kimi"], [0.120, 0.293, 0.000, 0.007], [PURPLE, ACCENT, GREEN, ORANGE], minv=-0.1, maxv=0.36)
        draw.text((960, 835), "Causal displayed-self-label effect, paired slice", font=font(30), fill=MUTED, anchor="mm")
    elif kind == "recognition":
        draw_bar_chart(draw, 250, 360, 1420, 430, ["Claude", "Gemini", "GPT-5.5", "Kimi"], [10, 1, 10, 0], [PURPLE, ACCENT, GREEN, ORANGE], minv=0, maxv=10.5, suffix="/10")
        draw.text((960, 835), "Self-recognition hits in C4; Gemini had 1/10 but strongest causal label effect", font=font(30), fill=MUTED, anchor="mm")
    elif kind == "floor":
        # Schematic scatter, not raw data.
        import random
        random.seed(7)
        axes = (350, 330, 1550, 780)
        draw.line((axes[0], axes[3], axes[2], axes[3]), fill=MUTED, width=4)
        draw.line((axes[0], axes[1], axes[0], axes[3]), fill=MUTED, width=4)
        for i in range(34):
            base = random.random()
            uplift = 0.75 * (1 - base) + random.gauss(0, 0.11)
            px = axes[0] + base * (axes[2]-axes[0])
            py = axes[3] - max(0, min(1, uplift)) * (axes[3]-axes[1])
            draw.ellipse((px-8, py-8, px+8, py+8), fill=ACCENT)
        draw.line((axes[0]+40, axes[1]+40, axes[2]-40, axes[3]-90), fill=YELLOW, width=6)
        draw.text((950, 830), "Higher baseline quality → less room for label uplift", font=font(32), fill=MUTED, anchor="mm")
        draw.text((950, 285), "Self-label uplift", font=font(30, True), fill=TEXT, anchor="mm")
        draw.text((960, 925), "Baseline score without self label", font=font(30, True), fill=TEXT, anchor="mm")


def render_slide(idx: int, data: dict):
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    # subtle header/footer
    draw.rectangle((0, 0, W, 92), fill=(9, 12, 22))
    draw.text((80, 46), "GPT-5.5 Model", font=font(30, True), fill=ACCENT, anchor="lm")
    draw.text((1840, 46), f"{idx+1:02d}/{len(SLIDE_DATA):02d}", font=font(28), fill=MUTED, anchor="rm")
    draw.text((115, 170), data["title"], font=font(64, True), fill=TEXT)
    draw_wrapped(draw, data.get("kicker", ""), (120, 255), font(36), ACCENT, 80)

    if "chart" in data:
        draw_chart(draw, data["chart"])
        bullet_x, bullet_y = 155, 895
        bullet_font = font(29)
        max_chars = 70
    else:
        bullet_x, bullet_y = 220, 395
        bullet_font = font(42)
        max_chars = 58

    for b in data["bullets"]:
        draw.ellipse((bullet_x, bullet_y+14, bullet_x+16, bullet_y+30), fill=ACCENT)
        bullet_y = draw_wrapped(draw, b, (bullet_x+35, bullet_y), bullet_font, TEXT, max_chars, line_gap=8)
        bullet_y += 10

    draw.text((960, 1038), "Public research artifact: ai-village-agents/research-2026-05", font=font(24), fill=(120, 132, 156), anchor="mm")
    path = SLIDES / f"slide_{idx+1:02d}.png"
    img.save(path)
    return path


async def tts_one(idx: int, text: str):
    import edge_tts
    out = AUDIO / f"slide_{idx+1:02d}.mp3"
    if out.exists() and out.stat().st_size > 1000:
        return out
    communicate = edge_tts.Communicate(text, VOICE, rate=RATE)
    await communicate.save(str(out))
    return out


def run(cmd):
    print("+", " ".join(map(str, cmd)))
    subprocess.run(list(map(str, cmd)), check=True)


def duration(path: Path) -> float:
    p = subprocess.run([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(path)
    ], text=True, stdout=subprocess.PIPE, check=True)
    return float(p.stdout.strip())


async def main():
    for d in [SLIDES, AUDIO, CLIPS]:
        d.mkdir(parents=True, exist_ok=True)
    for i, data in enumerate(SLIDE_DATA):
        render_slide(i, data)
    await asyncio.gather(*(tts_one(i, data["narration"]) for i, data in enumerate(SLIDE_DATA)))

    concat = OUT / "concat.txt"
    with concat.open("w", encoding="utf-8") as f:
        for i in range(len(SLIDE_DATA)):
            slide = SLIDES / f"slide_{i+1:02d}.png"
            aud = AUDIO / f"slide_{i+1:02d}.mp3"
            clip = CLIPS / f"slide_{i+1:02d}.mp4"
            dur = duration(aud) + 0.45
            run([
                "ffmpeg", "-y", "-loop", "1", "-framerate", "1", "-i", slide, "-i", aud,
                "-t", f"{dur:.3f}", "-c:v", "libx264", "-preset", "ultrafast",
                "-tune", "stillimage", "-pix_fmt", "yuv420p", "-r", "24",
                "-vf", "scale=1920:1080", "-c:a", "aac", "-b:a", "192k",
                "-shortest", clip,
            ])
            f.write(f"file '{clip.resolve()}'\n")
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat, "-c", "copy", FINAL])
    print(f"Wrote {FINAL}")
    print(f"Duration: {duration(FINAL):.1f} seconds")


if __name__ == "__main__":
    main_cwd = Path.cwd()
    os.chdir(ROOT)
    asyncio.run(main())
