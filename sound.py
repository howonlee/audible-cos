import numpy as np
import numpy.random as npr
import sounddevice as sd
import operator
import functools

def prod(iterable):
    return functools.reduce(operator.mul, iterable, 1)

def scaled_cos(scale, inp):
    return np.cos(scale * inp)

# var1 = maxval of randint
# var2 = number of ints genned
problem = list(npr.randint(0, 512, 9))

fs = 44100
secs = 50
# var3 = linspace
inp = np.linspace(0, 1e2, fs * secs)
curr_res = prod(scaled_cos(member, inp) for member in problem)
curr_res = curr_res * 1e2
sd.play(curr_res, fs, blocking=True)
