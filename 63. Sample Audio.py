# Python Audio

import sounddevice as sd
import soundfile as sf

filename = "After Dark.mp3"

data, samplerate = sf.read(filename)

print(f"Playing {filename}")
sd.play(data, samplerate)
sd.wait()

print("Finished")
