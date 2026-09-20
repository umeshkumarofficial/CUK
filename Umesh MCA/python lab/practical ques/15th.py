# Write a Python function using variable-length positional arguments (*args) to compute the L2 norm
# (Euclidean length) of an arbitrary n-dimensional coordinate vector.

import math

def l2_norm(*args):
    total = 0

    for x in args:
        total = total + x ** 2

    return math.sqrt(total)


print("L2 Norm:", l2_norm(3, 4))