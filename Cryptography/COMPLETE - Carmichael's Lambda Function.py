# Carmichael's Lambda Function is calculates the SMALLEST POSITIVE m
# for n such that a^m is congruent to 1 mod n
# for the group of all unit elements in the ring of all congruence classes mod n

from math import lcm

def carmichael(n: list) -> int:
    """
    n: list of tuples of integers, representing the prime factorisation of n
    so for 819 we'd have n=[(3,2),(7,1),(13,1)]
    where the first number in the tuple is the base, and second is the exponent
    """
