#!/usr/bin/env python3
"""
Ableton Documentation Linter
A terminal trainer for writing Ableton-style release notes.
Run with: python3 ableton_linter.py
"""

import re
import os
import sys
import datetime
import textwrap
import random

# ─────────────────────────────────────────────────────────────────────────────
# ANSI COLORS
# ─────────────────────────────────────────────────────────────────────────────

class C:
    RESET     = "\033[0m"
    BOLD      = "\033[1m"
    DIM       = "\033[2m"
    UNDERLINE = "\033[4m"
    RED       = "\033[91m"
    GREEN     = "\033[92m"
    YELLOW    = "\033[93m"
    BLUE      = "\033[94m"
    MAGENTA   = "\033[95m"
    CYAN      = "\033[96m"
    WHITE     = "\033[97m"

def col(color, text): return f"{color}{text}{C.RESET}"
def bold(text):       return col(C.BOLD, text)
def dim(text):        return col(C.DIM, text)
def red(text):        return col(C.RED, text)
def green(text):      return col(C.GREEN, text)
def yellow(text):     return col(C.YELLOW, text)
def cyan(text):       return col(C.CYAN, text)
def magenta(text):    return col(C.MAGENTA, text)
def blue(text):       return col(C.BLUE, text)

# ─────────────────────────────────────────────────────────────────────────────
# PRACTICE SCENARIOS (seeded from real Ableton Live 12.x release notes)
# ─────────────────────────────────────────────────────────────────────────────

SCENARIOS = {
    1: [
        {
            "title": "Cabinet — companion to the Amp device",
            "context": (
                "Cabinet is an audio effect, developed in collaboration with Softube, that emulates "
                "the sound of five classic guitar speaker cabinets. It uses physical-modelling "
                "technology and is designed to be placed after Amp in the device chain. Cabinet "
                "offers two microphone types (Dynamic and Condenser), two mic positions (Near and "
                "Far), and two on-axis/off-axis options. Output can be set to mono or Dual stereo."
            ),
            "hint": "Open with what Cabinet IS and what it pairs with. Then list its controls in a separate paragraph.",
            "example": (
                "Cabinet is an effect that emulates the sound of five classic guitar speaker "
                "cabinets. Developed in collaboration with Softube, Cabinet uses physical-modelling "
                "technology and is designed to be used after Amp in a device chain.\n\n"
                "Choose between Dynamic and Condenser microphone types, with Near or Far positions "
                "and on-axis or off-axis placement. The Output switch toggles between mono and "
                "Dual stereo processing. Note that Dual mode uses twice as much CPU."
            ),
        },
        {
            "title": "Compressor — main controls",
            "context": (
                "The Compressor reduces the dynamic range of an audio signal by attenuating signals "
                "above a Threshold. The Ratio control determines how strongly the signal is reduced. "
                "Attack sets how quickly the compressor responds once the signal exceeds the threshold, "
                "while Release sets how long it takes to stop compressing once the signal drops back "
                "below. The Knee control adjusts how gradually compression is applied around the "
                "threshold. Makeup gain compensates for the level reduction."
            ),
            "hint": "Describe the device's purpose first, then walk through the controls in logical signal-flow order.",
            "example": (
                "Compressor reduces the dynamic range of an audio signal by attenuating any part of "
                "the signal that rises above the Threshold. The Ratio control determines how much "
                "the signal is reduced once it crosses the threshold.\n\n"
                "Attack sets how quickly compression engages, while Release sets how quickly it "
                "disengages once the signal falls back below the threshold. The Knee parameter "
                "shapes the transition around the threshold, from hard to soft. Use Makeup gain "
                "to compensate for the overall level reduction."
            ),
        },
        {
            "title": "Looper — basic recording workflow",
            "context": (
                "Looper is an audio effect that lets users record and overdub audio loops in real "
                "time, similar to a stompbox-style hardware looper. The large Multi-Purpose "
                "Transport Button cycles through Record, Overdub, Play, and Stop. Audio can be "
                "captured from the track's input or from the audio that reaches Looper in the "
                "device chain. Length can be set in advance or determined by the first recording pass."
            ),
            "hint": "Frame Looper around what the user does with it. Use 'Multi-Purpose Transport Button' verbatim.",
            "example": (
                "Looper is an audio effect for recording and overdubbing audio loops in real time, "
                "modelled on stompbox-style hardware loopers. Click the large Multi-Purpose "
                "Transport Button to cycle through Record, Overdub, Play, and Stop.\n\n"
                "Looper captures audio from the track's input or from any signal that reaches it "
                "in the device chain. Set the loop length in advance, or let the first recording "
                "pass define it."
            ),
        },
    ],
    2: [
        {
            "title": "Stem Separation — Live 12.3",
            "context": (
                "Live Suite now includes built-in stem separation. Any audio clip — a full song, "
                "loop, or sample — can be split into four stems: Vocals, Drums, Bass, and Others. "
                "Users right-click a clip in Session or Arrangement View (or a file in the Browser) "
                "and select 'Separate Stems to New Audio Tracks'. Each stem is placed on its own "
                "track inside a new Group Track. Processing runs locally on the user's machine."
            ),
            "hint": "What can the user now DO? Name the menu command and UI locations exactly.",
            "example": (
                "Stem Separation is now available in Live Suite. Right-click any audio clip in "
                "Session View, Arrangement View, or the Browser and select Separate Stems to New "
                "Audio Tracks to split audio into four stems: Vocals, Drums, Bass, and Others. "
                "Each stem is placed on its own track within a new Group Track."
            ),
        },
        {
            "title": "Link Audio — Live 12.4",
            "context": (
                "Live 12.4 introduces Link Audio, which lets users stream audio in real time between "
                "Link Audio-enabled devices on the same local Wi-Fi network — no cables needed. It "
                "builds on the existing Link protocol that already syncs tempo and transport."
            ),
            "hint": "Lead with what the user can now do. 'Link Audio' is a proper noun — capitalise it.",
            "example": (
                "Link Audio lets you stream audio in real time between Link Audio-enabled devices "
                "on a shared local network. Connect wirelessly alongside existing Link-based tempo "
                "and transport sync."
            ),
        },
        {
            "title": "Expressive Chords device — Live 12.2",
            "context": (
                "A new MPE-enabled Max for Live device called Expressive Chords generates harmonies "
                "and articulations from simple single-note MIDI input. It works with MPE-capable "
                "controllers and is designed for users who want expressive chord playing without "
                "needing advanced music theory knowledge."
            ),
            "hint": "Describe input → output. 'Expressive Chords' is the device name — keep the capitals.",
            "example": (
                "Expressive Chords is a new MPE-enabled Max for Live device that turns single-note "
                "input into full harmonies and articulations. Use it with any MPE-capable controller "
                "to explore chord voicings without prior theory knowledge."
            ),
        },
        {
            "title": "Bounce Track in Place — Live 12.2",
            "context": (
                "Users can now select any portion of a MIDI or audio track, right-click, and choose "
                "'Bounce Track in Place' to convert that selection to audio on a new track. The new "
                "track sits at the same position and is numbered one higher than the source track."
            ),
            "hint": "Name the command exactly as it appears in the UI. Describe what you do and what you get.",
            "example": (
                "Select any portion of a MIDI or audio track and use Bounce Track in Place to "
                "convert the selection to audio on a new track. The bounced track is placed at the "
                "same position and numbered one higher than the source."
            ),
        },
        {
            "title": "Auto Filter new filter types — Live 12.2",
            "context": (
                "Auto Filter has been updated with three new filter types: Vowel, DJ, and Comb. "
                "The modulation section has been overhauled for greater precision. New mixing "
                "controls and a real-time frequency visualisation have also been added."
            ),
            "hint": "List the specific additions. 'Auto Filter' is a device name — capitalise it.",
            "example": (
                "Auto Filter has three new filter types: Vowel, DJ, and Comb. The modulation "
                "section has been updated for greater accuracy, with new mixing controls and "
                "real-time frequency visualisation."
            ),
        },
        {
            "title": "Browser Filter View simplified",
            "context": (
                "The Browser's Filter View has been redesigned. The title bar has been replaced "
                "with a toggle button to the right of the search bar. A new drop-down menu gives "
                "access to filter group visibility, auto-tag options, and more."
            ),
            "hint": "Focus on what changed visually and how it helps. 'Browser' and 'Filter View' are UI names.",
            "example": (
                "The Browser's Filter View has been simplified. A toggle to the right of the search "
                "bar now replaces the title bar, and a new drop-down menu provides access to filter "
                "groups and auto-tag settings."
            ),
        },
        {
            "title": "Ctrl+F search now clears previous terms",
            "context": (
                "When starting a new search with Ctrl+F (Windows) / Cmd+F (Mac), any previous search "
                "terms and active filters in the All label are now cleared automatically."
            ),
            "hint": "Name the shortcut for both platforms. Describe the old state and the new behaviour.",
            "example": (
                "Starting a new search with Ctrl+F (Windows) / Cmd+F (Mac) now clears any previous "
                "search terms and active filters in the All label automatically."
            ),
        },
        {
            "title": "Komplete Kontrol S MK3 control surface update",
            "context": (
                "The Komplete Kontrol S MK3 control surface script has been updated. Track meters "
                "now show in the track's colour. Encoders can fine-tune parameter values while Shift "
                "is held. Tempo mode is accessible via Shift + Metro. Devices can be selected, "
                "controlled, and viewed in Plugin mode."
            ),
            "hint": "Describe each capability clearly. 'Komplete Kontrol S MK3' and 'Plugin mode' are proper names.",
            "example": (
                "Updated the Komplete Kontrol S MK3 control surface. Track meters now display in "
                "the track's color. Hold Shift to fine-tune parameters with the encoders. Access "
                "Tempo mode via Shift + Metro, and select or control devices in Plugin mode."
            ),
        },
    ],
    3: [
        {
            "title": "Stem separation CPU bug on Apple Silicon",
            "context": (
                "On macOS Tahoe 26.1 on Apple Silicon machines, stem separation was using the CPU "
                "instead of the Neural Engine, causing it to run significantly slower than expected. "
                "This has now been resolved."
            ),
            "hint": "Name the platform, describe what was wrong, state what now works.",
            "example": (
                "Fixed an issue on macOS Tahoe 26.1 on Apple Silicon where Stem Separation used "
                "the CPU instead of the Neural Engine, causing slower-than-expected processing times."
            ),
        },
        {
            "title": "Crash when undoing a Soundtoys plug-in load",
            "context": (
                "Loading a Soundtoys plug-in and then performing an undo step to remove it caused "
                "Live to crash. This has been fixed."
            ),
            "hint": "State the exact trigger (load + undo) and the fix. One clear sentence is enough.",
            "example": (
                "Fixed a crash that occurred when loading a Soundtoys plug-in and then using Undo "
                "to remove it."
            ),
        },
        {
            "title": "Sidechain export failure with Group Track source",
            "context": (
                "When exporting audio with 'Include Master and Return Effects' enabled, sidechaining "
                "failed silently if the sidechain source was a Group Track. This is now fixed."
            ),
            "hint": "Specify both conditions that triggered the bug. Use 'Group Track' with capitals.",
            "example": (
                "Fixed a bug where exporting audio with Include Master and Return Effects enabled "
                "would cause sidechaining to fail when the sidechain source was a Group Track."
            ),
        },
        {
            "title": "Bounced track showing wrong track number",
            "context": (
                "When using 'Bounce to New Track', the new track was displaying the source track's "
                "number instead of a unique number. Bounced tracks now display a number one higher "
                "than the source track."
            ),
            "hint": "Describe what the user saw (wrong number) and what they see now (correct number).",
            "example": (
                "Fixed an issue where tracks created with Bounce to New Track displayed the source "
                "track's number. Bounced tracks now show a unique number one higher than the source."
            ),
        },
    ],
    4: [
        {
            "title": "Free entry — write about any Ableton feature",
            "context": (
                "Write a release note for any real or plausible Ableton feature, bug fix, or "
                "improvement. Some ideas from recent Live 12.x releases:\n"
                "  • Auto Shift — real-time pitch correction device added in Live 12.1\n"
                "  • Roar — multiband saturation device with compressor and feedback routing\n"
                "  • Meld synth — MPE-capable bi-timbral synthesizer\n"
                "  • Granulator III — updated granular synthesizer by Robert Henke\n"
                "  • MIDI Transformations — apply ornaments, acceleration curves, chord variations\n"
                "  • Sound similarity search in the Browser\n"
                "  • Splice integration in the Browser\n\n"
                "Or invent a plausible feature entirely. Just make it specific and user-facing."
            ),
            "hint": "Pick something concrete. Write as if it ships tomorrow in the official release notes.",
            "example": (
                "Auto Shift is now available as a native real-time pitch correction device in Live 12.1. "
                "Place it on any audio track and use the Correction knob to dial in how strongly "
                "pitch is pulled toward the nearest scale degree. Set the scale in the Scale and "
                "Root controls, or link it to a MIDI track for melodic guidance."
            ),
        },
    ],
}

TYPE_LABELS = {1: "Manual", 2: "Release Note", 3: "Bug Fix", 4: "Free"}

# ─────────────────────────────────────────────────────────────────────────────
# LINTING DATA
# ─────────────────────────────────────────────────────────────────────────────

BRITISH_SPELLINGS = {
    "colour": "color", "colours": "colors", "favourite": "favorite", "favourites": "favorites",
    "behaviour": "behavior", "behaviours": "behaviors", "organisation": "organization",
    "organise": "organize", "organising": "organizing", "organised": "organized",
    "recognise": "recognize", "recognising": "recognizing", "recognised": "recognized",
    "utilise": "utilize", "utilising": "utilizing", "utilised": "utilized",
    "maximise": "maximize", "minimise": "minimize", "optimise": "optimize",
    "centralise": "centralize", "synchronise": "synchronize", "analyse": "analyze",
    "analysing": "analyzing", "analysed": "analyzed", "defence": "defense",
    "offence": "offense", "licence": "license", "practise": "practice",
    "grey": "gray", "labelled": "labeled", "travelling": "traveling",
    "cancelled": "canceled", "focussed": "focused", "programme": "program",
    "programmes": "programs", "theatre": "theater", "centre": "center",
    "fibre": "fiber", "calibre": "caliber", "metre": "meter",
}

MARKETING_WORDS = [
    "exciting", "excited", "excitement", "powerful", "powerfully", "innovative", "innovation",
    "amazing", "amazingly", "incredible", "incredibly", "fantastic", "awesome",
    "revolutionary", "game-changing", "game changer", "groundbreaking", "ground-breaking",
    "cutting-edge", "next-level", "best-in-class", "world-class", "seamless", "seamlessly",
    "delightful", "delightfully", "beautiful", "beautifully", "stunning", "robust",
    "ultimate", "perfect", "perfectly", "supercharge", "supercharged", "elevate",
    "transform", "transformative", "unleash", "unlock potential",
]

DEV_WORDS = [
    "implemented", "refactored", "codebase", "pull request", "backend", "frontend",
    "api call", "endpoint", "regression", "hotfix", "deploy", "deployed", "deployment",
    "repo ", "repository", "commit", "merged", "merge request", "stack trace",
    "null pointer", "exception thrown", "deprecated", "legacy code", "unit test",
    "integration test", "callback", "asynchronous", "thread-safe", "concurrency",
    "memory leak", "garbage collection", "runtime error",
]

# Known UI element names — if found lowercase, flag them
KNOWN_UI_ELEMENTS = {
    "arrangement view", "session view", "clip view", "detail view", "device view",
    "clip editor", "note editor", "midi editor", "filter view", "browser",
    "master track", "group track", "return track", "instrument rack",
    "audio effect rack", "midi effect rack", "drum rack", "drum sampler",
    "auto filter", "auto pan", "auto shift", "link audio",
    "expressive chords", "bounce track in place", "bounce to new track",
    "separate stems to new audio tracks", "plugin mode", "tempo mode",
    "scale and root", "correction knob", "width control", "noise gate",
    "roar", "meld", "granulator", "operator", "analog", "wavetable",
    "echo", "reverb", "compressor", "limiter", "eq eight", "eq three",
    "saturator", "corpus", "resonator", "vocoder", "spectral blur",
    "push", "move", "note", "live suite", "live standard", "live intro",
    # Auto Shift parameters
    "correction", "formant", "vibrato", "tolerance", "correction speed",
    "formant shift", "vibrato depth", "pitch correction",
    # Other Live 12 features and devices
    "stem separation", "multi-purpose transport button",
    "midi transformations", "midi transformation",
    "granulator iii", "auto shift correction",
    "cabinet", "looper", "amp",
}

PASSIVE_PATTERNS = [
    r"\bwas (added|fixed|updated|changed|improved|removed|replaced|redesigned|renamed|enabled|disabled)\b",
    r"\bwere (added|fixed|updated|changed|improved|removed|replaced|redesigned|renamed)\b",
    r"\bhas been (added|fixed|updated|changed|improved|removed|replaced|redesigned)\b",
    r"\bhave been (added|fixed|updated|changed|improved|removed|replaced)\b",
    r"\bcan be (found|accessed|opened|used|enabled|disabled|set|configured)\b",
    r"\bis (shown|displayed|enabled|disabled|rendered|triggered|activated)\b",
]

FUTURE_PASSIVE_PATTERNS = [
    r"\bwill be (added|fixed|updated|changed|improved|removed|replaced|redesigned|renamed|enabled|disabled|done|released|available|supported|included)\b",
    r"\bwould be (added|fixed|updated|changed|improved|removed|replaced|redesigned|renamed)\b",
]

ACRONYMS = {
    "midi": "MIDI", "mpe": "MPE", "cpu": "CPU", "gpu": "GPU",
    "vst": "VST", "au": "AU", "aax": "AAX", "daw": "DAW",
    "lfo": "LFO", "adsr": "ADSR", "osc": "OSC",
}

CONTRACTIONS = [
    "don't", "can't", "won't", "isn't", "it's", "you're", "they're",
    "doesn't", "didn't", "hasn't", "haven't", "couldn't", "wouldn't",
    "we're", "i'm", "i've", "you've", "they've", "we've",
    "i'd", "you'd", "they'd", "we'd", "that's", "there's", "what's",
    "i'll", "you'll", "they'll", "we'll",
]

MINIMIZE_WORDS = [
    "simply", "just", "easily", "straightforward", "obviously",
    "of course", "clearly", "naturally", "trivially",
]

WEAK_OPENER_PATTERNS = [
    r"^there (is|are|was|were)\b",
    r"^it is\b",
    r"^this is a\b",
    r"^this allows\b",
]

REDUNDANT_PHRASES = {
    "in order to":           "to",
    "due to the fact that":  "because",
    "at this point in time": "now",
    "in the event that":     "if",
    "on a regular basis":    "regularly",
    "with the exception of": "except",
}

FILLER_PHRASES = [
    "please note", "note that", "it is worth noting", "please be aware",
    "it should be noted", "as you can see", "as mentioned",
]

PARAM_VALUE_PATTERN = re.compile(
    r'(?<!")-?\d+(?:\.\d+)?\s*(?:%|dB|Hz|kHz|BPM|bpm|ms)(?!")',
)

# ─────────────────────────────────────────────────────────────────────────────
# INLINE HIGHLIGHT HELPERS
# ─────────────────────────────────────────────────────────────────────────────

def get_mistake_spans(text):
    """Return a sorted list of (start, end) character spans for every mistake."""
    spans = []
    lower = text.lower()

    for brit in BRITISH_SPELLINGS:
        for m in re.finditer(r'\b' + re.escape(brit) + r'\b', lower):
            spans.append((m.start(), m.end()))

    for word in MARKETING_WORDS:
        for m in re.finditer(r'\b' + re.escape(word) + r'\b', lower):
            spans.append((m.start(), m.end()))

    for word in DEV_WORDS:
        for m in re.finditer(re.escape(word.strip()), lower):
            spans.append((m.start(), m.end()))

    for element in KNOWN_UI_ELEMENTS:
        for m in re.finditer(r'\b' + re.escape(element) + r'\b', text, re.IGNORECASE):
            found = m.group(0)
            if found == found.lower() and found != found.title():
                spans.append((m.start(), m.end()))

    for lower_acr, correct_acr in ACRONYMS.items():
        for m in re.finditer(r'\b' + re.escape(lower_acr) + r'\b', text, re.IGNORECASE):
            if m.group(0) != correct_acr:
                spans.append((m.start(), m.end()))

    for contraction in CONTRACTIONS:
        for m in re.finditer(r'\b' + re.escape(contraction) + r'\b', lower):
            spans.append((m.start(), m.end()))

    for word in MINIMIZE_WORDS:
        for m in re.finditer(r'\b' + re.escape(word) + r'\b', lower):
            spans.append((m.start(), m.end()))

    for phrase in REDUNDANT_PHRASES:
        for m in re.finditer(re.escape(phrase), lower):
            spans.append((m.start(), m.end()))

    for phrase in FILLER_PHRASES:
        for m in re.finditer(re.escape(phrase), lower):
            spans.append((m.start(), m.end()))

    for pat in PASSIVE_PATTERNS:
        for m in re.finditer(pat, lower):
            spans.append((m.start(), m.end()))

    for pat in [r'\ballow(s)? to\b', r'\benable(s)? to\b']:
        for m in re.finditer(pat, lower):
            spans.append((m.start(), m.end()))

    for m in re.finditer(r'\b(ableton live|live \d[\d.]*)\b', text, re.IGNORECASE):
        found = m.group(0)
        if found[0].islower() or found.split()[0].islower():
            spans.append((m.start(), m.end()))

    first_word = re.match(r'\b(\w+)\b', text)
    if first_word and first_word.group(1).lower() in ("i", "we"):
        spans.append((first_word.start(), first_word.end()))

    for m in re.finditer(r'\betc\.?\b', lower):
        spans.append((m.start(), m.end()))

    for m in re.finditer(r'  ', text):
        spans.append((m.start(), m.end()))

    for m in PARAM_VALUE_PATTERN.finditer(text):
        spans.append((m.start(), m.end()))

    for m in re.finditer(r'\.\.\.', text):
        spans.append((m.start(), m.end()))

    # Weak sentence openers — highlight the opener phrase
    sentence_starts = [0]
    for m in re.finditer(r'(?<=[.!?])\s+', text):
        sentence_starts.append(m.end())
    for start in sentence_starts:
        sent_lower = text[start:].lower()
        for pat in WEAK_OPENER_PATTERNS:
            wm = re.match(pat, sent_lower)
            if wm:
                spans.append((start, start + wm.end()))
                break

    return spans


def render_highlighted(text, spans):
    """Return text with mistake spans coloured red and underlined."""
    if not spans:
        return col(C.WHITE, text)

    # Merge overlapping spans
    merged = []
    for span in sorted(spans):
        if merged and span[0] <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], span[1]))
        else:
            merged.append(list(span))

    ERROR = C.RED + C.UNDERLINE
    result = []
    prev = 0
    for start, end in merged:
        if prev < start:
            result.append(col(C.WHITE, text[prev:start]))
        result.append(col(ERROR, text[start:end]))
        prev = end
    if prev < len(text):
        result.append(col(C.WHITE, text[prev:]))
    return "".join(result)


# ─────────────────────────────────────────────────────────────────────────────
# LINTER
# ─────────────────────────────────────────────────────────────────────────────

def lint(text, entry_type):
    issues = []
    score = 10
    words = text.split()
    word_count = len(words)
    lower = text.lower()

    # 1. American English
    for brit, american in BRITISH_SPELLINGS.items():
        pattern = r'\b' + re.escape(brit) + r'\b'
        if re.search(pattern, lower):
            issues.append({
                "severity": "error",
                "rule": "American English",
                "detail": f'"{brit}" → use "{american}"',
                "penalty": 1,
            })
            score -= 1

    # 2. Marketing language
    for word in MARKETING_WORDS:
        pattern = r'\b' + re.escape(word) + r'\b'
        if re.search(pattern, lower):
            issues.append({
                "severity": "error",
                "rule": "No marketing language",
                "detail": f'Remove "{word}" — this is promotional, not technical.',
                "penalty": 1,
            })
            score -= 1

    # 3. Developer language
    for word in DEV_WORDS:
        if word in lower:
            issues.append({
                "severity": "error",
                "rule": "User-facing language",
                "detail": f'"{word.strip()}" is developer language. Describe the user-visible behaviour instead.',
                "penalty": 1,
            })
            score -= 1

    # 4. Paragraph length — flag any paragraph with more than 4 sentences.
    # Skipped in Free mode, where structure isn't enforced.
    if entry_type != 4:
        paragraphs = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]
        long_paragraphs = []
        for idx, para in enumerate(paragraphs, start=1):
            # Lookbehind on [.!?] + whitespace avoids splitting on "Live 12.4".
            parts = re.split(r'(?<=[.!?])\s+', para)
            sentences = [s for s in parts if s.strip()]
            if len(sentences) > 4:
                long_paragraphs.append((idx, len(sentences)))

        if long_paragraphs:
            if len(paragraphs) == 1:
                label = f"This paragraph has {long_paragraphs[0][1]} sentences"
            else:
                label = ", ".join(f"paragraph {i} has {n}" for i, n in long_paragraphs)
            issues.append({
                "severity": "warning",
                "rule": "Paragraph length",
                "detail": f"{label} — keep paragraphs to 4 sentences or fewer. Break dense paragraphs into smaller ones.",
                "penalty": 1,
            })
            score -= 1

    # 5. Starts with I or We
    first_word = re.match(r'\b(\w+)\b', text)
    if first_word and first_word.group(1).lower() in ("i", "we"):
        issues.append({
            "severity": "error",
            "rule": "Do not start with I/We",
            "detail": f'Starts with "{first_word.group(1)}" — rewrite to lead with the subject or action.',
            "penalty": 1,
        })
        score -= 1

    # 6. UI element capitalisation
    for element in KNOWN_UI_ELEMENTS:
        pattern = r'\b' + re.escape(element) + r'\b'
        if re.search(pattern, lower):
            # Check if it appears correctly capitalised anywhere
            correct = element.title().replace("Eq ", "EQ ").replace("Midi", "MIDI").replace(" Mpe", " MPE")
            # Simple heuristic: if the lowercase version appears but correct case doesn't
            matches_in_original = re.findall(pattern, text.lower())
            correct_matches = re.findall(re.escape(element), text.lower())
            # Check for exact-case match
            words_in_text = text
            # Find the actual occurrences and check casing
            for m in re.finditer(pattern, text, re.IGNORECASE):
                found = m.group(0)
                # If it's all lowercase, flag it
                if found == found.lower() and found != found.title():
                    issues.append({
                        "severity": "error",
                        "rule": "UI element capitalisation",
                        "detail": f'"{found}" should be capitalised — it\'s a named UI element (e.g. "{element.title()}").',
                        "penalty": 1,
                    })
                    score -= 1
                    break  # one flag per element

    # 7. Passive voice (not checked for bug fixes — "Fixed a bug where..." is the standard form)
    if entry_type != 3:
        passive_found = []
        for pat in PASSIVE_PATTERNS:
            matches = re.findall(pat, lower)
            if matches:
                passive_found.extend(matches)

        if passive_found:
            examples = ", ".join(f'"{m}"' for m in passive_found[:2])
            issues.append({
                "severity": "warning",
                "rule": "Passive voice",
                "detail": f"Possible passive voice detected: {examples}. Rewrite with an active subject where possible.",
                "penalty": 1,
            })
            score -= 1

    # 7a. Future passive voice — note only, no penalty
    future_passive_found = []
    for pat in FUTURE_PASSIVE_PATTERNS:
        matches = re.findall(pat, lower)
        if matches:
            future_passive_found.extend(matches)

    if future_passive_found:
        examples = ", ".join(f'"{m}"' for m in future_passive_found[:2])
        issues.append({
            "severity": "info",
            "rule": "Future passive voice",
            "detail": f"Future passive detected: {examples}. Consider active form ('will add', 'will include') — no points deducted.",
            "penalty": 0,
        })

    # 8. Type-specific checks
    if entry_type == 2:  # Release Note (new features / improvements)
        action_words = ["can now", "now ", "lets you", "allows you", "use ", "select ", "access ", "drag ", "right-click"]
        has_action = any(w in lower for w in action_words)
        if not has_action:
            issues.append({
                "severity": "warning",
                "rule": "Release note structure",
                "detail": "Release notes should describe what the user can now DO. Lead with a capability, action, or change.",
                "penalty": 1,
            })
            score -= 1

    # 9. Acronym capitalisation
    for lower_acr, correct_acr in ACRONYMS.items():
        pattern = r'\b' + re.escape(lower_acr) + r'\b'
        for m in re.finditer(pattern, text, re.IGNORECASE):
            found = m.group(0)
            if found != correct_acr:
                issues.append({
                    "severity": "error",
                    "rule": "Acronym capitalisation",
                    "detail": f'"{found}" should be "{correct_acr}" — acronyms are always all-caps in Ableton docs.',
                    "penalty": 1,
                })
                score -= 1
                break

    # 10. Contractions
    contraction_found = []
    for contraction in CONTRACTIONS:
        pattern = r'\b' + re.escape(contraction) + r'\b'
        if re.search(pattern, lower):
            contraction_found.append(contraction)
    if contraction_found:
        examples = ", ".join(f'"{c}"' for c in contraction_found[:2])
        issues.append({
            "severity": "error",
            "rule": "No contractions",
            "detail": f"Contractions found: {examples}. Use the full form (e.g. \"don't\" → \"do not\").",
            "penalty": 1,
        })
        score -= 1

    # 11. Condescending / minimize words
    minimize_found = []
    for word in MINIMIZE_WORDS:
        pattern = r'\b' + re.escape(word) + r'\b'
        if re.search(pattern, lower):
            minimize_found.append(word)
    if minimize_found:
        examples = ", ".join(f'"{w}"' for w in minimize_found[:2])
        issues.append({
            "severity": "warning",
            "rule": "Minimize words",
            "detail": f"{examples} — these make tasks sound trivial. Cut them or rephrase.",
            "penalty": 1,
        })
        score -= 1

    # 12. Weak sentence openers
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    weak_openers_found = []
    for sent in sentences:
        sent_lower = sent.strip().lower()
        for pat in WEAK_OPENER_PATTERNS:
            if re.match(pat, sent_lower):
                weak_openers_found.append(sent.strip()[:40])
                break
    if weak_openers_found:
        example = weak_openers_found[0]
        issues.append({
            "severity": "warning",
            "rule": "Weak sentence opener",
            "detail": f'"{example}..." — avoid starting sentences with "There is/are" or "It is". Lead with the subject.',
            "penalty": 1,
        })
        score -= 1

    # 13. "Live" software name capitalisation
    if re.search(r'\bableton live\b', lower) or re.search(r'\blive \d+', lower):
        for m in re.finditer(r'\b(ableton live|live \d[\d.]*)\b', text, re.IGNORECASE):
            found = m.group(0)
            if found[0].islower() or found.split()[0].islower():
                issues.append({
                    "severity": "error",
                    "rule": "Software name capitalisation",
                    "detail": f'"{found}" — "Live" (the software) is always capitalised (e.g. "Live 12", "Ableton Live").',
                    "penalty": 1,
                })
                score -= 1
                break

    # 14. Redundant phrases
    for phrase, replacement in REDUNDANT_PHRASES.items():
        if phrase in lower:
            issues.append({
                "severity": "warning",
                "rule": "Redundant phrasing",
                "detail": f'"{phrase}" → use "{replacement}" instead.',
                "penalty": 1,
            })
            score -= 1

    # 15. Grammar: "allows to" / "enables to" (missing "you")
    if re.search(r'\ballow(s)? to\b', lower) or re.search(r'\benable(s)? to\b', lower):
        issues.append({
            "severity": "error",
            "rule": "Grammar: allows/enables to",
            "detail": '"allows to" and "enables to" are grammatically incorrect. Use "allows you to", "lets you", or "enables you to".',
            "penalty": 1,
        })
        score -= 1

    # 16. Filler phrases
    filler_found = [p for p in FILLER_PHRASES if p in lower]
    if filler_found:
        examples = ", ".join(f'"{p}"' for p in filler_found[:2])
        issues.append({
            "severity": "warning",
            "rule": "Filler phrases",
            "detail": f"{examples} — these add no information. Cut them entirely.",
            "penalty": 1,
        })
        score -= 1

    # 17. Double spaces
    if "  " in text:
        issues.append({
            "severity": "warning",
            "rule": "Double spaces",
            "detail": "Double spaces detected. Use a single space between words and after punctuation.",
            "penalty": 1,
        })
        score -= 1

    # 18. Sentence-ending ellipsis
    if re.search(r'\.\.\.\s*(\n|$)', text.strip()):
        issues.append({
            "severity": "warning",
            "rule": "Trailing ellipsis",
            "detail": '"..." at the end of a sentence implies an unfinished thought. Complete the sentence or cut it.',
            "penalty": 1,
        })
        score -= 1

    # 19. "etc." usage
    if re.search(r'\betc\.?\b', lower):
        issues.append({
            "severity": "warning",
            "rule": "Avoid etc.",
            "detail": '"etc." is vague. Either complete the list or use a phrase like "and other controls".',
            "penalty": 1,
        })
        score -= 1

    # 20. Parameter value formatting
    param_matches = list(PARAM_VALUE_PATTERN.finditer(text))
    if param_matches:
        examples = ", ".join(m.group(0).strip() for m in param_matches[:2])
        issues.append({
            "severity": "warning",
            "rule": "Parameter value formatting",
            "detail": f'Parameter values should be in double quotes: {examples}. Write "100%", "-6 dB", "440 Hz" etc.',
            "penalty": 1,
        })
        score -= 1

    score = max(0, score)
    return issues, score, word_count

# ─────────────────────────────────────────────────────────────────────────────
# AI REWRITE using Anthropic API (called from artifact context — skipped in CLI)
# For CLI we generate a rule-based corrected hint + show the scenario example
# ─────────────────────────────────────────────────────────────────────────────

def apply_basic_corrections(text):
    """Apply simple mechanical fixes for illustration."""
    result = text
    for brit, american in BRITISH_SPELLINGS.items():
        result = re.sub(r'\b' + re.escape(brit) + r'\b', american, result, flags=re.IGNORECASE)
    return result

# ─────────────────────────────────────────────────────────────────────────────
# SESSION HISTORY
# ─────────────────────────────────────────────────────────────────────────────

HISTORY_FILE = "ableton_linter_history.txt"

def save_to_history(entry_type, scenario_title, user_text, issues, score, word_count, disputes=None):
    if disputes is None:
        disputes = {}
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n{'='*60}\n")
        f.write(f"[{timestamp}] {TYPE_LABELS[entry_type]} — {scenario_title}\n")
        f.write(f"Score: {score}/10  |  Words: {word_count}\n")
        f.write(f"{'─'*60}\n")
        f.write(f"SUBMISSION:\n{user_text.strip()}\n")
        if issues:
            f.write(f"\nISSUES:\n")
            for i, iss in enumerate(issues):
                marker = "✗" if iss["severity"] == "error" else "⚠"
                f.write(f"  {marker} [{iss['rule']}] {iss['detail']}\n")
                if i in disputes:
                    f.write(f"      ↳ DISPUTED: {disputes[i]}\n")
        else:
            f.write("\nNo issues found.\n")
        f.write(f"{'='*60}\n")

# ─────────────────────────────────────────────────────────────────────────────
# UI HELPERS
# ─────────────────────────────────────────────────────────────────────────────

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def wrap(text, width=72, indent=""):
    lines = text.split("\n")
    wrapped = []
    for line in lines:
        if line.strip() == "":
            wrapped.append("")
        else:
            wrapped.extend(textwrap.wrap(line, width=width, initial_indent=indent, subsequent_indent=indent))
    return "\n".join(wrapped)

def divider(char="─", width=72, color=C.DIM):
    print(col(color, char * width))

def header():
    clear()
    print()
    print(col(C.CYAN + C.BOLD, "  ██████  ABLETON DOCUMENTATION LINTER"))
    print(col(C.DIM,           "  Release Note Practice Tool  ·  v1.0"))
    divider()
    print()

def print_issue(iss):
    if iss["severity"] == "error":
        icon  = red("  ✗")
        label = red(f"[{iss['rule']}]")
    elif iss["severity"] == "warning":
        icon  = yellow("  ⚠")
        label = yellow(f"[{iss['rule']}]")
    else:  # info
        icon  = cyan("  ℹ")
        label = cyan(f"[{iss['rule']}]")
    detail = wrap(iss["detail"], width=66, indent="      ")
    print(f"{icon} {label}")
    print(col(C.DIM, detail))
    print()

def print_score(score):
    bar_len = 30
    filled  = round((score / 10) * bar_len)
    empty   = bar_len - filled

    if score >= 8:
        color = C.GREEN
    elif score >= 5:
        color = C.YELLOW
    else:
        color = C.RED

    bar = col(color, "█" * filled) + col(C.DIM, "░" * empty)
    print(f"\n  {bold('Score:')} {col(color + C.BOLD, str(score))}{col(C.DIM, '/10')}  {bar}\n")

def get_multiline_input(prompt):
    """Collect multi-line input. Paragraphs allowed — two consecutive blank lines submit."""
    print(col(C.DIM, prompt))
    print(col(C.DIM, "  (Single blank line = paragraph break. Two blank lines in a row submit."))
    print(col(C.DIM, "   Type 'END' on its own line to submit, or 'cancel' to abort.)\n"))
    lines = []
    blank_count = 0
    while True:
        try:
            line = input()
        except KeyboardInterrupt:
            return None
        except EOFError:
            break
        stripped = line.strip().lower()
        if stripped == "cancel":
            return None
        if stripped == "end":
            break
        if line == "":
            blank_count += 1
            if blank_count >= 2 and lines:
                break
            lines.append(line)
        else:
            blank_count = 0
            lines.append(line)
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines).strip()

# ─────────────────────────────────────────────────────────────────────────────
# SCREENS
# ─────────────────────────────────────────────────────────────────────────────

def show_menu():
    header()
    print(bold("  MAIN MENU"))
    print()
    print(f"  {cyan('1.')} Manual")
    print(f"  {cyan('2.')} Release Note")
    print(f"  {cyan('3.')} Bug Fix")
    print(f"  {cyan('4.')} Free Entry")
    print()
    divider()
    print(f"  {cyan('H.')} View session history")
    print(f"  {cyan('Q.')} Quit")
    print()
    choice = input(col(C.CYAN, "  Select › ")).strip().upper()
    return choice

def show_scenario(entry_type):
    pool = SCENARIOS[entry_type]
    scenario = random.choice(pool)
    
    header()
    print(bold(f"  {TYPE_LABELS[entry_type].upper()}"))
    divider()
    print()
    print(f"  {bold('Scenario:')} {cyan(scenario['title'])}")
    print()

    # Context block
    ctx_lines = wrap(scenario["context"], width=68, indent="  ")
    print(col(C.DIM, ctx_lines))
    print()

    # Hint
    print(f"  {yellow('Hint:')} {col(C.DIM, scenario['hint'])}")
    print()
    divider()
    print()

    user_text = get_multiline_input("  Write your release note below:")

    if user_text is None:
        return

    if len(user_text.strip()) < 5:
        print(red("\n  Entry too short — nothing to evaluate.\n"))
        input(dim("  Press Enter to continue..."))
        return

    show_feedback(entry_type, scenario, user_text)

def show_dispute_screen(issues, disputes):
    """Let the user select one flagged issue and argue against it."""
    header()
    print(bold("  DISPUTE A FLAG"))
    divider()
    print()
    print(col(C.DIM, "  Which flag do you want to dispute?\n"))

    for i, iss in enumerate(issues, 1):
        icon = red("✗") if iss["severity"] == "error" else yellow("⚠")
        disputed_tag = f"  {dim('[disputed]')}" if (i - 1) in disputes else ""
        detail_short = iss["detail"][:70] + ("…" if len(iss["detail"]) > 70 else "")
        print(f"  {cyan(str(i) + '.')} {icon} {bold(iss['rule'])}{disputed_tag}")
        print(col(C.DIM, f"      {detail_short}"))
        print()

    choice = input(col(C.CYAN, "  Issue number (or Enter to cancel) › ")).strip()
    if not choice:
        return disputes

    try:
        idx = int(choice) - 1
        if idx < 0 or idx >= len(issues):
            raise ValueError
    except ValueError:
        print(red("\n  Invalid number.\n"))
        input(dim("  Press Enter to continue..."))
        return disputes

    print()
    iss = issues[idx]
    print(col(C.DIM, f"  Flag:   [{iss['rule']}]"))
    print(col(C.DIM, f"  Detail: {iss['detail']}"))
    print()
    print(col(C.DIM, "  State your argument — why should this flag not apply here?"))
    reason = input(col(C.CYAN, "  Your argument › ")).strip()

    if reason:
        disputes[idx] = reason
        print()
        print(green("  Argument noted. This flag will not count against your score."))
        print()

    input(dim("  Press Enter to continue..."))
    return disputes


def show_feedback(entry_type, scenario, user_text, disputes=None):
    if disputes is None:
        disputes = {}

    rule_tips = {
        "American English":            "Ableton docs use American English throughout.",
        "No marketing language":       "Release notes describe facts, not feelings. If it belongs in an ad, cut it.",
        "User-facing language":        "The reader is a musician, not a developer.",
        "Paragraph length":            "Long paragraphs hide the point. Keep each one to 3 sentences max — split when ideas shift.",
        "Do not start with I/We":      "Lead with the subject: the feature, the fix, or the user.",
        "UI element capitalisation":   "Named UI elements are proper nouns in Ableton docs. Capitalise them.",
        "Passive voice":               "Passive voice hides the subject. 'Fixed an issue' > 'An issue was fixed'.",
        "Future passive voice":        "Future passive ('will be added') is worth noting but not penalized. Active is clearer: 'will add', 'will include', 'will support'.",
        "Release note structure":      "Release notes lead with what the user can DO, not what was added.",
        "Acronym capitalisation":      "MIDI, MPE, CPU, LFO, DAW etc. are always written in all-caps in Ableton docs.",
        "No contractions":             "Technical documentation uses full forms: 'do not', 'cannot', 'it is'.",
        "Minimize words":              "Words like 'simply' or 'just' make tasks sound trivial. Cut them — the instruction is clear without them.",
        "Weak sentence opener":        "'There is/are' and 'It is' bury the real subject. Start with what the feature or action actually is.",
        "Software name capitalisation":"'Live' (the software) and version refs like 'Live 12' are always capitalised.",
        "Redundant phrasing":          "Shorter is clearer. 'in order to' → 'to', 'due to the fact that' → 'because'.",
        "Grammar: allows/enables to":  "'Allows to' is grammatically wrong. Use 'allows you to' or 'lets you'.",
        "Filler phrases":              "'Please note', 'note that' etc. add no information. Cut them entirely.",
        "Double spaces":               "Use a single space between words and after punctuation.",
        "Trailing ellipsis":           "'...' at the end signals an unfinished thought — not appropriate for release notes.",
        "Avoid etc.":                  "'etc.' is vague. Complete the list or write 'and other controls'.",
        "Parameter value formatting":  'Place parameter values in double quotes: 100% is "100%", -6 dB is "-6 dB", 440 Hz is "440 Hz".',
    }

    issues, score, word_count = lint(user_text, entry_type)

    while True:
        # Effective score: restore penalty for each disputed issue
        effective_score = score
        for idx in disputes:
            if idx < len(issues):
                effective_score += issues[idx].get("penalty", 1)
        effective_score = min(10, effective_score)

        header()
        print(bold("  EVALUATION"))
        divider()
        print()

        # Echo submission with inline mistake highlights
        print(col(C.DIM, "  Your submission:"))
        print()
        spans = get_mistake_spans(user_text.strip())
        highlighted = render_highlighted(user_text.strip(), spans)
        for line in highlighted.split("\n"):
            print(f"    {line}")
        print()
        print(col(C.DIM, f"  Word count: {word_count}"))
        print()
        divider()
        print()

        # Score
        print_score(effective_score)
        if disputes and effective_score != score:
            n = sum(1 for i in disputes if i < len(issues))
            print(col(C.DIM, f"  ({n} flag(s) disputed — score reflects your argument)\n"))

        # Issues
        if not issues:
            print(green("  ✓  No issues found. Clean entry!\n"))
        else:
            print(bold(f"  Found {len(issues)} issue(s):\n"))
            for i, iss in enumerate(issues):
                if i in disputes:
                    rule_label = iss["rule"]
                    print(f"{dim('  ◌')} {dim('[' + rule_label + ']')} {dim('[disputed]')}")
                    print(col(C.DIM, wrap(iss["detail"], width=66, indent="      ")))
                    print(col(C.DIM, f"      Your argument: {disputes[i]}"))
                    print()
                else:
                    print_issue(iss)

        divider()
        print()

        # Corrected example
        print(bold("  EXAMPLE RELEASE NOTE (from Ableton style):"))
        print()
        example_lines = wrap(scenario["example"], width=68, indent="  ")
        print(col(C.GREEN, example_lines))
        print()

        divider()

        # Tips summary — skip tips for disputed issues
        active_issues = [iss for i, iss in enumerate(issues) if i not in disputes]
        if active_issues:
            print()
            print(bold("  RULES TRIGGERED:"))
            rules_seen = set()
            for iss in active_issues:
                if iss["rule"] not in rules_seen:
                    rules_seen.add(iss["rule"])
                    tip = rule_tips.get(iss["rule"], "")
                    print(f"  {yellow('→')} {bold(iss['rule'])}")
                    if tip:
                        print(col(C.DIM, f"    {tip}"))
            print()

        divider()
        print()

        # Options
        print(f"  {cyan('1.')} Try again with a new scenario")
        print(f"  {cyan('2.')} Try the same scenario again")
        print(f"  {cyan('3.')} Back to main menu")
        if issues:
            print(f"  {cyan('4.')} Dispute a flag")
        print()
        choice = input(col(C.CYAN, "  Select › ")).strip()

        if choice == "4" and issues:
            disputes = show_dispute_screen(issues, disputes)
            continue  # re-render with updated disputes

        # Save on exit
        save_to_history(entry_type, scenario["title"], user_text, issues, effective_score, word_count, disputes)
        print(col(C.DIM, f"  Session saved to {HISTORY_FILE}"))
        print()

        if choice == "1":
            show_scenario(entry_type)
        elif choice == "2":
            show_feedback_retry(entry_type, scenario)
        return

def show_feedback_retry(entry_type, scenario):
    header()
    print(bold(f"  {TYPE_LABELS[entry_type].upper()} — RETRY"))
    divider()
    print()
    print(f"  {bold('Scenario:')} {cyan(scenario['title'])}")
    print()
    ctx_lines = wrap(scenario["context"], width=68, indent="  ")
    print(col(C.DIM, ctx_lines))
    print()
    print(f"  {yellow('Hint:')} {col(C.DIM, scenario['hint'])}")
    print()
    divider()
    print()
    user_text = get_multiline_input("  Write your revised release note below:")
    if user_text is None or len(user_text.strip()) < 5:
        return
    show_feedback(entry_type, scenario, user_text)

def show_history():
    header()
    print(bold("  SESSION HISTORY"))
    divider()
    print()
    if not os.path.exists(HISTORY_FILE):
        print(col(C.DIM, "  No history yet. Complete a practice session first.\n"))
    else:
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                content = f.read()
            # Show last ~3000 chars
            if len(content) > 3000:
                content = "  [... earlier entries truncated ...]\n\n" + content[-3000:]
            print(col(C.DIM, content))
        except Exception as e:
            print(red(f"  Could not read history: {e}\n"))
    divider()
    print()
    input(dim("  Press Enter to return to menu..."))

# ─────────────────────────────────────────────────────────────────────────────
# MAIN LOOP
# ─────────────────────────────────────────────────────────────────────────────

def main():
    while True:
        choice = show_menu()

        if choice in ("1", "2", "3", "4"):
            show_scenario(int(choice))
        elif choice == "H":
            show_history()
        elif choice == "Q":
            clear()
            print(col(C.CYAN, "\n  Good work. Keep writing.\n"))
            sys.exit(0)
        else:
            pass  # silently loop back

if __name__ == "__main__":
    main()