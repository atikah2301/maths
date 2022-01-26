# The number of irreducible polynomials of degree n with binary coefficients

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

def is_prod_of_distinct_primes(n):
    factors = prime_factorisation(n)
    for base, exp in factors:
        if exp > 1:
            return False
    return True

def divisors(n):
    d = []
    for i in range(1, (n//2)+2):
        if n % i == 0:
            d.append(i)
    d.append(n)
    return d

def mobius(n):
    if n==1: return 1
    if is_prod_of_distinct_primes(n):
        k = len(prime_factorisation(n))
        return (-1)**k
    else: return 0

def eulers_totient(n: int) -> int:
    z = [] # list of numbers no greater than n
    g = [] # list of GCDs corresponding to z[i]
    t = [] # list of z[i] with corresponding g[i]==1 i.e. totients

    # Create a list of all 0<i<n
    i = 1
    while i <= n:
        z.append(i)
        i += 1

    i = 0
    while i < n:
        a = n
        b = z[i]
        # Calculate gcd(i,n), then add to list g
        while b != 0:
            a , b = b, a%b
        g.append(a)
        # if the gcd=1, then add to list t, of totients
        if a == 1:
            t.append(z[i])
        i += 1

    return len(t)

def irreducible_polynomials(n):
    """"""
    d = divisors(n)
    exp = d[::-1]
    sum = 0
    for i in range(len(d)):
        sum += (2**exp[i])*mobius(d[i])
    return sum//n

def primitive_polynomials(n):
    """"""
    phi = eulers_totient((2**n)-1)
    return phi//n

print(divisors(4))
print(irreducible_polynomials(4))
print(primitive_polynomials(4))
