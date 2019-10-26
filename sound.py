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

def gen_problem(min_val, max_val, problem_card):
    return list(npr.randint(min_val, max_val, problem_card))

def gen_sound(problem, linspace_scale, freq, num_secs, vol_adj):
    inp = np.linspace(0, linspace_scale, freq * num_secs)
    curr_res = prod(scaled_cos(member, inp) for member in problem)
    return curr_res * vol_adj

if __name__ == "__main__":
    pass


sd.play(curr_res, FREQ, blocking=True)
