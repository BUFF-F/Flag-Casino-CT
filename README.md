# Flag Casino — Reverse Engineering Practice (HTB-style CTF)

This repository collects a small, self-contained reverse‑engineering exercise used for teaching. The goal is to decode a secret flag by reversing a simple LUT‑based obfuscation. It contains working scripts and supporting data in Python and a C program used to generate the LUT entries.

Intended audience: classmates learning basic RE/CTF techniques.

## What’s in this repo
- script.py — Python decoder that reconstructs the flag from the provided data and LUT.
- lut.py / lut — Look‑up table mapping numeric keys to pseudo‑random 32‑bit values (hex).
- data.py — The obfuscated data items that represent bytes / suffixes to map back to characters.
- script.c — Example C program that demonstrates how the LUT values were generated (srand + rand).
- casino — Compiled binary (challenge artifact / reference).
- .vscode/ — helper launch/tasks files used in development.

## How it works (short)
1. A LUT maps integer keys (0–255) to 32‑bit hex values produced by rand() seeded with the key.
2. The obfuscated data entries are hex strings. The decoder converts each entry to lowercase hex, looks it up in the LUT (matching values to a character code), or finds a LUT key whose hex value ends with the data suffix.
3. The mapped integer is interpreted as an ASCII code (chr) and concatenated to reveal the flag.

## Run the Python decoder
Requirements: Python 3.x

From the repo root:
- Ensure `lut.py` and `data.py` are present.
- Run:
    python script.py

This prints the recovered flag (if all mappings are present).

## Rebuild / explore the LUT in C
Requirements: gcc / MinGW

- Build:
    gcc script.c -o generate_lut
- Run:
    ./generate_lut

The program prints `index:hexvalue` pairs produced by seeding srand(index) and calling rand().

## Learning goals
- Understand deterministic pseudo‑random outputs from seeded rand().
- Practice recovering mappings and suffix matching logic.
- Build simple decoders to transform obfuscated blobs into human‑readable output.

Notes:
- This repo is for learning and practice. Use it to study techniques used in CTF reverse‑engineering challenges, not to unfairly solve ongoing competitions.
- Adjust and instrument the code to experiment with alternative LUTs / data.

License: Use for educational purposes.