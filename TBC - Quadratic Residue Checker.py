def peel(a, p):
    # Returns (k, b) such that a = p^k * b and b is minimal.
    if a == 0: return (1, 0)
    k = 0
    while a % p == 0:
        k += 1
        a = a // p
    return (k, a)

def is_quadratic_residue(a, n):
    for (p, e) in factor(n):
        (k, b) = peel(a % p**e, p)
        if b == 0: continue
        if k % 2: return False
        if p == 2:
            if e == 1: continue
            if b % 4 != 1: return False
            if e >= 3 and b % 8 != 1: return False
        else:  # Euler's criterion
            if power_mod(b, (p - 1)//2, p) != 1:
                return False
    return True
