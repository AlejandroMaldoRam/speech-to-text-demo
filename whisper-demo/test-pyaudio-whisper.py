# Script for testing the integration between PyAudio and Whisper.
import wave
import sys

import pyaudio

import whisper

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1 if sys.platform == 'darwin' else 2
RATE = 44100
RECORD_SECONDS = 5

# Record audio
with wave.open('output.wav', 'wb') as wf:
    p = pyaudio.PyAudio()
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)

    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

    print('Recording...')
    i = 0
    for _ in range(0, RATE // CHUNK * RECORD_SECONDS):
        if i%(RATE//CHUNK)==0:
            print('*')
        wf.writeframes(stream.read(CHUNK))
        i+=1
    print('Done')

    stream.close()
    p.terminate()

# Transcribe audio
print('Processing...')
model = whisper.load_model('base')
result = model.transcribe("output.wav")
print('Text:')
print(result['text'])