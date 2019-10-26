import numpy as np
import numpy.random as npr
import sounddevice as sd
import operator
import functools
import argparse

FREQ = 44100
NUM_SECS = 10
MAX_VAL = 128
PROBLEM_CARD = 7
LINSPACE_SCALE = int(1e2)
VOL_ADJ = 1e2

def prod(iterable):
    return functools.reduce(operator.mul, iterable, 1)

def scaled_cos(scale, inp):
    return np.cos(scale * inp)

def gen_problem(max_val, problem_card):
    return list(npr.randint(0, max_val, problem_card))

def gen_sound(problem, linspace_stop, freq, num_secs, vol_adj):
    inp = np.linspace(0, linspace_stop, freq * num_secs)
    curr_res = prod(scaled_cos(member, inp) for member in problem)
    return curr_res * vol_adj

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Play sounds corresponding to an NP-complete problem, or, alternately phrased, with very many and very high overtones.")
    parser.add_argument('--freq', type=int, default=44100, help='frequency')
    parser.add_argument('--num_secs', type=int, default=10, help='number of seconds of sound')
    parser.add_argument('--max_val', type=int, default=128, help='maximum number for random number partition instance')
    parser.add_argument('--problem_card', type=int, default=7, help='cardinality for number partition instance')
    parser.add_argument('--linspace_stop', type=int, default=int(1e2), help='how far the linear space transformed into cos scales')
    parser.add_argument('--vol_adj', type=int, default=int(1e2), help='adjustment for volume scaling')
    args = parser.parse_args()
    prob = gen_problem(args.max_val, args.problem_card)
    sound = gen_sound(prob, args.linspace_stop, args.freq, args.num_secs, args.vol_adj)
    sd.play(sound, FREQ, blocking=True)
