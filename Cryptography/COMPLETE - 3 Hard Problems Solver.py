# When choosing an encryption algorithm for a public key cryptosystem, your algorithm should be easy to solve one way
# but hard to solve when the problem is reversed.
# The code here should solve 3 such "hard problems" in a cyclic fashion
# Where one problem can be easily solved if the solution to another of the 3 is known.

# Problem 1 - Prime factorisation of n into odd primes p and q
# Problem 2 - Finding Carmichael's lambda value or Euler's phi value of n
# Problem 3 - Finding the inverse of a power map function on power e, reduced mod n


from math import gcd

def prob_3_to_1(n: int, e: int, d: int):
    """
    Given a power map e and its inverse d, find the 2 prime factors of n.

    Calculate de-1, factorise out its greatest power of 2.
    The the power be a and the remaining odd factor be b.
    Choose the smallest (or any) x coprime to n.
    Ensure that x^b mod n did not give 1 or -1, otherwise try a different x. Let this value be y.
    Ensure that y^2 mod n gives 1, otherwise try a different x. Let this value be y.
    Then return p = gcd(n, y-1) and q = gcd(n, y+1)
    """
    b = d*e-1
    a = 0
    while b % 2**(a+1) == 0:
        a += 1
        b //= 2**a
    print(f"a={a}, b={b}")
    x = 2
    while True:
        if gcd(x, n) != 1:
            x += 1
            continue
        y = x**b % n
        if abs(y) == 1:
            x += 1
            continue
        y2 = y**2 % n
        if y2 != 1:
            x += 1
            continue
        break
    print(f"x={x}, y={y}")
    p = gcd(n,y-1)
    q = gcd(n,y+1)
    if p < q:
        p, q = q, p
    print(f"p={p}, q={q}")
    if p*q == n:
        print(f"p*q=={n} as expected")
    else:
        print(f"p*q != {n}.. something went wrong")

prob_3_to_1(589, 7, 13)
