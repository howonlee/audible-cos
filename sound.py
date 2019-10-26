import numpy as np
import numpy.random as npr
import sounddevice as sd

fs = 44100
data = npr.uniform(-1, 1, fs)
sd.play(data, fs, blocking=True)
