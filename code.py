import os
import speech_recognition as sr

def transcribe_wav_file(wav_path: str, language: str, output_path: str) -> None:
    if not os.path.isfile(wav_path):
        raise FileNotFoundError(f"NO AUDIO IN THIS PATH..!! {wav_path}")

    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio_data = recognizer.record(source)

    text = recognizer.recognize_google(audio_data, language=language)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)

    print("HERE IS THE FINAL OUTPUT!!")
    print(text)


if __name__ == '__main__':
    audio_file = input("TELL ME THE AUDIO PATH").strip()
    output_file = input("OUTPUT AS TEXT???").strip()
    lang_code = input("THE LANGUAGE U NEED TO CONVERT IS???").strip()

    try:
        transcribe_wav_file(audio_file, lang_code, output_file)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
