import whisper

def load_model(model_name='base'):
    """Whisper modelni yuklash uchubn"""
    model = whisper.load_model(model_name)
    return model

def trancribe_audio(model, audio_path, language='uz'):
    result = model.transcribe(audio_path, language=language)
    return result['text']

if __name__ == "__main__":
    model = load_model('base')

    text = trancribe_audio(model, 'test.gg')
    print(f"Natija {text}")

    