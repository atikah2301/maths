# code for returning the first n primes

def primes(n):
    all_primes = []
    next_prime = 2
    is_prime = True
    
    while len(all_primes) < n:
        for i in range(len(all_primes)):
            if next_prime % all_primes[i] == 0:
                is_prime = False
                break
        if is_prime:
            all_primes.append(next_prime)
        next_prime += 1
    
    return all_primes
    
print(primes(5))
