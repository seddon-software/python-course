import scipy
import scipy.fft
import matplotlib.pyplot as plt
import numpy as np

π = scipy.pi

signal_length = 0.5     # [seconds]
sample_rate = 500       # sampling rate [Hz]
dt = 1.0/sample_rate    # time between two samples [s]
df = 1.0/signal_length  # frequency between points in frequency domain [Hz]

t = np.arange(0,signal_length ,dt)     # the time vector

# create synthetic signal (without noise)
y = np.sin(2*π*155*t+π/3) + np.sin(2*π*50*t) + np.sin(2*π*70*t+π/4)

# compute fourier transform
f = scipy.fft.fft(y)

# work out meaningful frequencies in fourier transform
freqs = df*np.arange(0, (len(t)-1)/2., dtype='d')   # d=double precision float

# plot input data y against time
rows = 2
cols = 1
plotNo = 1
plt.subplot(rows, cols, plotNo)
plt.plot(t,y,label='input data')
plt.xlabel('time [sec]')
plt.ylabel('signal')

# plot frequency spectrum
plotNo = 2
plt.subplot(rows, cols, plotNo)
plt.plot(freqs,abs(f[0:len(freqs)]), label='abs(fourier transform)')
plt.xlabel('frequency [Hz]')
plt.ylabel('abs(DFT(signal))')

plt.tight_layout()  # make sure everything fits in window

# save plot to disk
plt.savefig('fft-results.pdf')

fig = plt.gcf()
fig.canvas.manager.set_window_title("Fast Fourier Transform")
plt.show()
