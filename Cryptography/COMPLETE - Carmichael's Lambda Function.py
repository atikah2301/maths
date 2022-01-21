# Carmichael's Lambda Function is calculates the SMALLEST POSITIVE m
# for n such that a^m is congruent to 1 mod n
# for the group of all unit elements in the ring of all congruence classes mod n

from math import sqrt
from math import lcm

def carmichael(n: list) -> int:
    """
    n: list of tuples of integers, representing the prime factorisation of n
    so for 819 we'd have n=[(3,2),(7,1),(13,1)]
    where the first number in the tuple is the base, and second is the exponent
    """

def power_product(n: list) -> int:
    """Takes as input a list of pairs of integers,
    returns the product of all the first integers to the power of the second integer for each pair"""
    product = 1
    for base, exp in n:
        product *= base**exp
    return product

def prime_factorisation(n: int) -> list:
    original_n = n
    factors = []
    # Extract any factors of 2
    while n % 2 == 0:
        if len(factors) == 1:
            factors[0] = (factors[0][0], factors[0][1] + 1)
        else:
            factors.append((2,1))
        n = n / 2

    # Check odd factors
    for i in range(3, int(n)+3, 2):
        while n % i == 0:
            if not factors:
                factors.append((i, 1))
            elif factors[-1][0] == i:
                factors[-1] = (factors[-1][0], factors[-1][1] + 1)
            else:
                factors.append((i, 1))
            n = n / i

        # Stop checking when all factors are found
        if power_product(factors) == original_n:
            return factors

