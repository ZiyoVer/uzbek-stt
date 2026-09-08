import argparse

import whisper

def load_model(model_name='base'):
    """Whisper modelni yuklash uchubn"""
    model = whisper.load_model(model_name)
    return model

def transcribe_audio(model, audio_path, language='uz'):
    result = model.transcribe(audio_path, language=language)
    return result['text']

# Preserve compatibility with the original misspelled function name.
trancribe_audio = transcribe_audio

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe an audio file with Whisper.")
    parser.add_argument("audio_path", help="Path to an audio file")
    parser.add_argument("--model", default="base", help="Whisper model name")
    parser.add_argument("--language", default="uz", help="Language code (default: uz)")
    args = parser.parse_args()
    model = load_model(args.model)
    print(transcribe_audio(model, args.audio_path, language=args.language))
