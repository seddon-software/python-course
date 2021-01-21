import scipy
import numpy as np
from numpy import pi, sin, cos
import matplotlib.pyplot as plt

Fs = 1000                   # Sampling frequency                    
T = 1/Fs                    # Sampling period       
L = 15000                   # Length of signal (msec)
t = np.arange(0, L*T, T)    # Time vector

# generate synthetic sample
SS = (0.3*sin(2*pi*75*t) + 0.3*sin(2*pi*85*t) + 
     0.7*sin(2*pi*127*t) + 0.9*sin(2*pi*380*t))
# add some noise
S = SS - 7.9*np.random.random_sample(len(t))

# perform discrete Fourier Transformation
Y = scipy.fft(S)
Z = zeroFrequencyTerm = sumOfSignal = Y[0]
P = positiveFrequencyTerms = Y[1:L//2]
N = negativeFrequencyTerms = Y[L//2 + 1:]

# look at first few terms of P and N
# terms are complex conjugates
print([f"{term:.2f}" for term in P[0:4]])        
print([f"{term:.2f}" for term in N[:-5:-1]])

# calculate frequency range
frequency = np.linspace(0, Fs/2, len(P))

# sort amplitudes and find the top two
amplitudes = abs(P/len(P))

sortedAmplitudes = np.sort(amplitudes)
print(sortedAmplitudes[-8:])

def printStats(n):
    amplitude = sortedAmplitudes[-n]
    # find corresponding frequencies
    setOfIndices = np.where(amplitudes == amplitude)      # returns numpy array
    index = setOfIndices[0][0]
    print(f"frequency = {frequency[index]:.2f} amplitude = {amplitude:.2f}")
    
for n in range(1,5):
    printStats(n)

plt.xlabel('frequency [Hz]')
plt.ylabel('abs(DFT(signal))')

plt.grid()
plt.plot(frequency, abs(P/len(P)))
plt.show()
