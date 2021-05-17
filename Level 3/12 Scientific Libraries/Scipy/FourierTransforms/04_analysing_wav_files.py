import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack
import numpy as np
from matplotlib import pyplot as plt
from math import log

FILENAME = "note64.wav"
# FILENAME = "note67.wav"
# FILENAME = "note71.wav"

def analyzeSignal():    
    Fs, stereoSignal = wavfile.read(FILENAME)
    channels = len(stereoSignal.shape)
    if channels == 2:       # stereo
        # take the average across the 2 channels
        signal = stereoSignal.sum(axis=1) / 2
    L = signal.shape[0]
    secs = L / float(Fs)
    Ts = 1.0 / Fs      # sampling interval in time
    print (f"Signal shape: {stereoSignal.shape}")
    print (f"Channels: {channels}")
    print (f"Sampling frequency: {Fs} Hz")
    print (f"Signal length: {secs:.2f} secs")
    print (f"Time between samples: {Ts:.6f} secs")
    return signal, Fs, L, secs, Ts

signal, Fs, L, secs, Ts = analyzeSignal() 

t = scipy.arange(0, secs, Ts)
Y = scipy.fft(signal)
Z = zeroFrequencyTerm = sumOfSignal = Y[0]
P = positiveFrequencyTerms = Y[1:L//2]
N = negativeFrequencyTerms = Y[L//2 + 1:]

# plotting the signal
plt.subplot(311)
plt.plot(t, signal, "g") 
plt.xlabel('Time')
plt.ylabel('Amplitude')

# plotting the complete fft spectrum
plt.subplot(312)
amplitude = abs(Y)/len(P)
frequency = np.fft.fftfreq(len(Y), Ts)
plt.plot(frequency, amplitude, "r") 
#plt.plot(frequency[10000:-10000], amplitude[10000:-10000], "r") 
plt.xlabel('Frequency (Hz)')
plt.ylabel('Count double-sided')

# plotting the positive fft spectrum
plt.subplot(313)
frequency = np.linspace(0, Fs/2, len(P))
amplitude = abs(P)/len(P)

plt.plot(frequency[:600], amplitude[:600], "b") 
plt.xlabel('Frequency (Hz)')
plt.ylabel('Count single-sided')

# calculate the midi note number
index = amplitude.argmax(axis=0)
maxFrequency = frequency[index]
# print(maxFrequency)
# print(amplitude[index])    
note = 12 * log(maxFrequency/440) + 69 # standard: note A4 is 440Hz 
print(f"Midi note: {note:.1f}")

plt.gcf().canvas.set_window_title(FILENAME)
plt.tight_layout()
plt.show()

