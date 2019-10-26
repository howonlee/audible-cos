import numpy as np
import numpy.random as npr
import sounddevice as sd
import operator
import functools
import argparse

FREQ = 44100
NUM_SECS = 10
MIN_VAL = 0
MAX_VAL = 128
PROBLEM_CARD = 7
LINSPACE_SCALE = int(1e2)
VOL_ADJ = 1e2

def prod(iterable):
    return functools.reduce(operator.mul, iterable, 1)

def scaled_cos(scale, inp):
    return np.cos(scale * inp)

problem = list(npr.randint(MIN_VAL, MAX_VAL, PROBLEM_CARD))

inp = np.linspace(0, LINSPACE_SCALE, FREQ * NUM_SECS)
curr_res = prod(scaled_cos(member, inp) for member in problem)
curr_res = curr_res * VOL_ADJ
sd.play(curr_res, FREQ, blocking=True)
