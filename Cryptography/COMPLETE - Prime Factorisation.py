def power_product(n: list) -> int:
    """Takes as input a list of pairs of integers,
    returns the product of all the first integers to the power of the second integer for each pair"""
    product = 1
    for base, exp in n:
        product *= base**exp
    return product
