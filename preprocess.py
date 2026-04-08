import liborsa
import soundfile as sf

def preprocess_audio(input_path, output_path, target_sr=16000):
    """Audio faylni tozalah va tayyorlash"""

    audio, sr = librosa.load(input_path, sr=target_sr)
    audio = librosa.util.normalize(audio)
    audio, _ = librosa.effects.trim(audio)
    sf.write(output_path, audio, sr)

    duration = len(audio) / target_sr
    print(f"✅ Tayyor: {duration:.2f} sekund")

    return audio, sr


if __name__ == "__main__":
    preprocess_audio("input.ogg", "output.wav")


