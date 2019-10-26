Listen to an NP-Complete Problem
====

The task of finding whether

![integrate product of cosines](https://i.imgur.com/HtOPQQO.gif)

is true or not, for a corresponding to a set of a's, corresponds to a solution of the [number partition problem](https://en.wikipedia.org/wiki/Partition_problem) and therefore is NP-complete [Plaisted]. Therefore, listening to a product of cosines with a frequency scaled by a set of integers corresponds very literally to listening to an NP-complete problem. In this git repo is a generator for number partition problems and the product of cosine problems related to these, and the conversion to sounds.

In the section of the parameter space I've explored, they mostly sound like laundry machines. But they sound like interestingly different laundry machines each time! The mp3 files are some representative examples. The most interesting examples lie close to the critical phase transition of the corresponding number partition problem, as would be expected (that is, when `log2(max\_val) ~= problem cardinality`).

Requires a few packages which are noted in requirements.txt.

Do `./sound.py --help` for all arguments.

If things aren't audible, adjust `--vol_adj` to try to make them audible.

Adjusting `--linspace_stop`, which scales the whole sound by pitch, also has interesting effects.

I took a script for turning wav to mp3's from [here](https://digifesto.com/2013/04/16/bash-script-for-converting-all-wav-files-in-a-directory-to-mp3/).

[Plaisted] Plaisted, David A. "Some polynomial and integer divisibility problems are NP-hard." 17th Annual Symposium on Foundations of Computer Science (sfcs 1976). IEEE, 1976.
