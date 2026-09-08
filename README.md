# Uzbek STT Utilities

**Python utilities for Uzbek speech transcription, audio preprocessing, and WER/CER evaluation.**

A baseline toolkit built around pretrained Whisper models. For training experiments, see [Uzbek Whisper Fine-Tuning](https://github.com/ZiyoVer/FIne-tuning-).

[Original Uzbek notes](docs/README.uz.md)

## Setup

Install Python and FFmpeg, then create an environment:

```bash
git clone https://github.com/ZiyoVer/uzbek-stt.git
cd uzbek-stt
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, use `.venv\Scripts\activate`. FFmpeg must be available on your PATH. Whisper downloads the selected model weights on first use.

## Transcribe Uzbek audio

```python
from transcribe import load_model, transcribe_audio

model = load_model("base")
text = transcribe_audio(model, "recording.wav", language="uz")
print(text)
```

Or provide an audio file on the command line:

```bash
python transcribe.py recording.wav --model base --language uz
```

## Prepare audio

```python
from preprocess import preprocess_audio

audio, sample_rate = preprocess_audio("recording.ogg", "prepared.wav")
```

Preprocessing loads mono audio, resamples to 16 kHz, normalizes amplitude, and trims leading/trailing silence. It does not perform learned noise reduction.

## Evaluate a transcript

```python
from wer_calculate import calculate_wer, calculate_cer

reference = "Salom dunyo"
hypothesis = "Salom duniyo"
print(calculate_wer(reference, hypothesis))  # 50.0
print(calculate_cer(reference, hypothesis))
```

Scores are percentages. The functions lowercase text before scoring; they do not otherwise normalize punctuation or apostrophes. WER can exceed 100% when there are many insertions.

## Scope

This repository contains baseline scripts, not a trained Uzbek checkpoint or a packaged application. No labeled evaluation dataset is bundled. Historical estimates in the original notes should not be treated as a validated benchmark.

| File | Purpose |
| --- | --- |
| `transcribe.py` | Whisper model loading and transcription |
| `preprocess.py` | Resampling, normalization, and silence trimming |
| `wer_calculate.py` | Word and character error rates |

**Author:** [O'ktam Ziyodullayev](https://github.com/ZiyoVer)
