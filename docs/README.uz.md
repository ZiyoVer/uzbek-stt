# Uzbek STT (Speech-to-Text)

Ozbek tili uchun Whisper asosida STT loyihasi.

## O'rnatish

```bash
pip install -r requirements.txt
```

## Ishlatish

### Transcribe:
```python
from transcribe import load_model, transcribe_audio

model = load_model("base")
text = transcribe_audio(model, "audio.ogg")
print(text)
```

### WER hisoblash:
```python
from wer_calculate import calculate_wer

wer = calculate_wer("asl matn", "whisper natijasi")
print(f"WER: {wer}%")
```

### Audio preprocessing:
```python
from preprocess import preprocess_audio

preprocess_audio("input.ogg", "output.wav")
```

## Natijalar

| Model | WER |
|------|-----|
| tiny | ~60% |
| base | ~45% |
| small | ~35% |

## Muallif

O'ktam Ziyodullayev