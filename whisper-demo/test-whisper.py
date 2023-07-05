# Script for testing the usage of Whisper for Speech to text.
import whisper

if __name__ == '__main__':
    model = whisper.load_model('base')
    result = model.transcribe("/home/alejandro/Audio/2023-07-05-17-05-21.mp3")
    print(result)