#!/usr/bin/env python3
"""Validate Day 416 confidence-interval teaching numbers against source text.

This is a preproduction guardrail only. It checks that the numbers used in the
future confidence-interval packet are present in the local research checkout and
that the render-spec axis positions match the stated formula.
"""
from __future__ import annotations

from pathlib import Path
import math
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = Path('/home/computeruse/research-2026-05')
FINDINGS = RESEARCH / 'experiments/replication-wave/results/findings_summary_table.md'
HEADLINE = RESEARCH / 'experiments/replication-wave/results/headline_number_audit.md'
RENDER_SPEC = ROOT / 'docs/day416_confidence_intervals_render_spec_v0.md'

EXPECTED_SOURCE_SNIPPETS = {
    FINDINGS: [
        '| **Claude Opus 4.7** | +2.43 | +0.12 [−0.07, +0.30]',
        '| **Gemini 3.1 Pro** | +0.63 | **+0.29 [+0.14, +0.45]**',
        '| **Kimi K2.6** | **−2.87** ✱ | **+0.01** [−0.30,+0.34]',
        '| **Pooled 4-judge** | +0.38 [−0.33, +1.06]',
    ],
    HEADLINE: [
        '| claude-opus-4.7 paired SELF−OTHER label gap | +0.12 [-0.07, +0.30]',
        '| gemini-3.1-pro paired SELF−OTHER label gap | +0.29 [+0.14, +0.45]',
        '| kimi-k2.6 paired SELF−OTHER label gap | +0.01 [-0.30, +0.34]',
        '| Gemini displayed-`kimi-k2.6` label residual | -0.24 [-0.35, -0.16]',
    ],
}

EXPECTED_RENDER_VALUES = {
    -0.40: 360,
    -0.30: 480,
    -0.07: 756,
    0.00: 840,
    0.01: 852,
    0.12: 984,
    0.14: 1008,
    0.29: 1188,
    0.30: 1200,
    0.34: 1248,
    0.45: 1380,
    0.50: 1440,
    0.60: 1560,
}

AXIS_MIN = -0.40
AXIS_MAX = 0.60
PLOT_X_MIN = 360
PLOT_X_MAX = 1560


def fail(message: str) -> None:
    print(f'FAIL: {message}', file=sys.stderr)
    raise SystemExit(1)


def check_sources() -> None:
    for path, snippets in EXPECTED_SOURCE_SNIPPETS.items():
        if not path.exists():
            fail(f'missing source file {path}')
        text = path.read_text()
        for snippet in snippets:
            if snippet not in text:
                fail(f'missing expected source snippet in {path}: {snippet}')
    print('source snippets: ok')


def x_for(value: float) -> int:
    raw = PLOT_X_MIN + (value - AXIS_MIN) / (AXIS_MAX - AXIS_MIN) * (PLOT_X_MAX - PLOT_X_MIN)
    return int(round(raw))


def check_render_spec() -> None:
    if not RENDER_SPEC.exists():
        fail(f'missing render spec {RENDER_SPEC}')
    text = RENDER_SPEC.read_text()
    required_text = [
        'axis_min = -0.40',
        'axis_max = +0.60',
        'zero = 0.00',
        'hypothetical_threshold = +0.50',
        'plot_x_min = 360',
        'plot_x_max = 1560',
        'hypothetical action line',
        'not from the study',
        'crosses zero ≠ no effect',
        'No render exists. Audio review impossible. Do not upload.',
    ]
    for snippet in required_text:
        if snippet not in text:
            fail(f'missing required render-spec text: {snippet}')

    for value, expected_x in EXPECTED_RENDER_VALUES.items():
        computed_x = x_for(value)
        if computed_x != expected_x:
            fail(f'axis formula mismatch for {value:+.2f}: expected {expected_x}, computed {computed_x}')
        pattern = rf'{re.escape(f"{value:+.2f}" if value != 0 else " 0.00")} -> x={expected_x}'
        if not re.search(pattern, text):
            fail(f'missing stated axis position for {value:+.2f} -> x={expected_x}')
    print('render spec axis mapping: ok')


def main() -> None:
    check_sources()
    check_render_spec()
    print('Day 416 confidence-interval number validation passed.')
    print('Scope: source snippets and render-spec axis positions only; not render/audio/caption/upload approval.')


if __name__ == '__main__':
    main()
