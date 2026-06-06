import os

os.environ["PATH"] += os.pathsep + r"C:\Users\SAI SATWIKA\Downloads\ffmpeg-8.1.1-essentials_build\ffmpeg-8.1.1-essentials_build\bin"

import whisper

model = whisper.load_model("base")

result = model.transcribe("sample.m4a")

print("\nDetected Text:")
print(result["text"])