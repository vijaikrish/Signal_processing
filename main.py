# This is a sample Python script.

import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack

f = 10      # Frequency, in cycles per second, or Hertz
f1 = 12
f2 = 15
f_s = 100   # Sampling rate, or number of measurements per second

t = np.linspace(0, 2, 2 * f_s, endpoint=False)
x = np.sin(f * 2 * np.pi * t) + np.sin(f1 * 2 * np.pi * t) + np.sin(f2 * 2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, x)
ax.set_xlabel('Time [s]')
ax.set_ylabel('Signal amplitude')
plt.show()

X = fftpack.fft(x)
freqs = fftpack.fftfreq(len(x)) * f_s

fig2, ax = plt.subplots()
ax.stem(freqs, np.abs(X))
ax.set_xlabel('Frequency in Hertz [Hz]')
ax.set_ylabel('Frequency Domain (Spectrum) Magnitude')
ax.set_xlim(-f_s / 2, f_s / 2)
ax.set_ylim(-5, 110)
plt.show()
