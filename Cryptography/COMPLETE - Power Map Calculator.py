# Calculates T(x), which is x to the power of some e, all mod n
# e.g. if e=2 and n=3 then T(12) = 12^2 mod 3 = 24 mod 3 = 0

# Step 1: Find e as the unique minimal sum of powers of 2
# Step 2: Calculate 2^k for all k up to the maximum power needed from step 1
# Step 3: Calculate x^2^k for all k.. iteratively, by squaring the previous value and reducing mod n
# Step 4: Multiply together the x^2^k values needed to get x^e and reduce mod n


from math import log
from tabulate import tabulate

def get_sum_of_powers_of_2(e: int) -> list[int]:
    """
    Returns a list of integers which are the powers for each term in a sum of powers of 2 that equal e.
    E.g. for e=321, return [8,6,0] since e=2^8+2^6+2^0

    Step 1 of evaluating a power map.

    Calculate log2(e), round it down, add to a result list
    If log2(e) is a whole number, then stop, and return the result
    Otherwise let q be log2(e) rounded down and calculate e - 2^q
    Let this be the new e, repeat"""
    result = []
    f = e # we don't want to reassign e to anything else
    while True:
        q = log(f,2)
        result.append(int(q))
        if q == int(q):
            return result
        f = f - 2**int(q)

def tabulate_powers(x: int, n: int, powers_needed: list[int]) -> list[int]:
    """
    Takes a list of the powers of 2 needed to sum to e,
    tabulates 2^k and x^2^k and prints the table
    returns a list of all x^2^k

    Steps 2 and 3 of evaluating a power map.
    """
    k_values = [i for i in range(powers_needed[0]+1)]
    pow_2k_values = [2**k for k in k_values]
    pow_x2k_values = [(x**(2**k))%n for k in k_values]

    k_values.insert(0, "k")
    pow_2k_values.insert(0, "2^k")
    pow_x2k_values.insert(0, "x^2^k mod n")
    table = tabulate([k_values, pow_2k_values, pow_x2k_values])
    print(table)

    return pow_x2k_values[1:]

def evaluate_power_map(x: int, e: int, n: int) -> int:
    powers_needed = get_sum_of_powers_of_2(e)
    x2k_values = tabulate_powers(x, n, powers_needed)
    multiplicands = []
    answer = 1
    for i in powers_needed:
        multiplicands.append(x2k_values[i])
        answer *= x2k_values[i]
    print(f"{e} is the sum of 2s to the power of {powers_needed}")
    print(f"{x}^{e} is the product of = {multiplicands} which equals {answer}")
    print(f"Final answer is {x}^{e} mod {n}, which is {answer % n}")
    return answer % n

evaluate_power_map(123, 321, 557)
