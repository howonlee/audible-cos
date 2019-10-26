import numpy as np
import numpy.random as npr
import sounddevice as sd
import operator
import functools

def prod(iterable):
    return functools.reduce(operator.mul, iterable, 1)

def scaled_cos(scale, amp, inp):
    return amp * np.cos(scale * inp)

# var1 = top of randint
# var2 = number genned
freqs = list(npr.randint(0, 1e3, 8))
amps = list((npr.rand(30) - 0.5) * 2)
problem = zip(freqs, amps)

fs = 44100
secs = 50
# var3 = linspace
inp = np.linspace(0, 1e6, fs * secs)
curr_res = prod(scaled_cos(member, amp, inp) for member, amp in problem)
curr_res /= (curr_res.std() / 1e1)
sd.play(curr_res, fs, blocking=True)
