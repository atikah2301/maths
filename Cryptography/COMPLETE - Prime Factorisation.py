from math import sqrt

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

#n = 71171171 * 2
print(prime_factorisation(n))
