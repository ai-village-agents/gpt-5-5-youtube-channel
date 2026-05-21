"""Render a local green-checkmarks v11 caption-band-clearance rough.

This experiment reuses the v9 narration/audio timing but swaps scene 03-06
visuals for caption-band-clear v11 clearance PNGs. It is a local rough only: no reliable
full watch/listen, no final caption approval, and no upload approval.
"""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets" / "day414_green_checkmarks_mockups" / "visual_proofs"
V9 = ROOT / "production" / "day414_green_checkmarks_rough_v9_caption_safe"
AUDIO = V9 / "audio"
OUT = ROOT / "production" / "day415_green_checkmarks_rough_v11_caption_band_clearance"
CLIPS = OUT / "clips"
FINAL = OUT / "green_checkmarks_rough_v11_caption_band_clearance.mp4"
REPORT = OUT / "scene_timings_v11_caption_band_clearance.txt"
FPS = 24

VISUALS = {
    "01": ASSETS / "green_01_receipt_not_verdict.png",
    "02": ASSETS / "green_02_three_questions.png",
    "03": ASSETS / "green_03_fresh_base_caption_band_v11.png",
    "04": ASSETS / "green_04_right_diff_caption_band_v11.png",
    "05": ASSETS / "green_05_uncovered_risk_caption_band_v11.png",
    "06": ASSETS / "green_06_signals_not_verdicts_caption_band_v11.png",
    "07a": ASSETS / "green_07a_review_checklist_caption_safe_v9.png",
    "07b": ASSETS / "green_07b_ai_prompt_caption_safe_v7.png",
    "07c": ASSETS / "green_07c_receipt_close_caption_safe_v8.png",
}
TITLES = {
    "01": "A green check is evidence, not a verdict",
    "02": "Fresh base, right diff, uncovered risk",
    "03": "Fresh base: did the target move?",
    "04": "Right diff: what change will land?",
    "05": "Uncovered risk: what did it not inspect?",
    "06": "Signals are not verdicts",
    "07a": "Checklist: read the receipt",
    "07b": "Ask the AI to slow the moment down",
    "07c": "Keep the check, keep the question",
}
ORDER = ["01", "02", "03", "04", "05", "06", "07a", "07b", "07c"]


def run(cmd):
    subprocess.run([str(x) for x in cmd], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def probe(path: Path) -> float:
    p = subprocess.run([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(path)
    ], check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return float(p.stdout.strip())


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    CLIPS.mkdir(parents=True, exist_ok=True)
    clips = []
    timings = []
    t = 0.0
    for key in ORDER:
        visual = VISUALS[key]
        audio = AUDIO / f"segment_{key}.mp3"
        if not visual.exists():
            raise SystemExit(f"Missing visual {visual}")
        if not audio.exists():
            raise SystemExit(f"Missing reused v9 audio {audio}")
        dur = probe(audio)
        clip = CLIPS / f"segment_{key}.mp4"
        run([
            "ffmpeg", "-nostdin", "-y",
            "-loop", "1", "-framerate", str(FPS), "-i", visual,
            "-i", audio,
            "-t", f"{dur:.3f}",
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", str(FPS),
            "-c:a", "aac", "-b:a", "160k", "-shortest", clip,
        ])
        clip_dur = probe(clip)
        timings.append((key, TITLES[key], t, t + clip_dur, clip_dur, dur))
        t += clip_dur
        clips.append(clip)
    concat = OUT / "concat.txt"
    concat.write_text("".join(f"file '{c}'\n" for c in clips), encoding="utf-8")
    run(["ffmpeg", "-nostdin", "-y", "-f", "concat", "-safe", "0", "-i", concat, "-c", "copy", "-movflags", "+faststart", FINAL])
    final_dur = probe(FINAL)
    lines = [
        "Green-checkmarks rough render v11 caption-band clearance visual polish",
        "",
        f"final_duration {final_dur:.3f}",
        "",
        "Segments:",
    ]
    for key, title, start, end, clip_dur, audio_dur in timings:
        lines.append(f"{key:<3} {start:07.3f}  {end:07.3f}  clip={clip_dur:06.3f}  audio={audio_dur:06.3f}  {title}")
    lines += [
        "",
        "Status: local visual-polish rough only; no full watch/listen, no final caption approval, no upload approval.",
        "Scenes 03-06 use caption-band-clear v11 visual assets; other scenes reuse v9 visual assets.",
    ]
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(FINAL)
    print(REPORT)
    print(f"{final_dur:.3f}")

if __name__ == "__main__":
    main()
