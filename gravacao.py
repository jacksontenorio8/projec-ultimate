import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # Taxa de amostragem
seconds = 5  # Duração da gravação
print("Gravando...")
audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()  # Aguarda o término da gravação
write("output.wav", fs, audio)
print("Áudio salvo como 'output.wav'")
