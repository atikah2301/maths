# every divisor of an integer n is some combination of factors from its unique prime factorisation
# e.g. n = 12 = 2*2*3 = 2**2 * 3**1
# here the exponents are 2 and 1. 
# These are important because we do not want to generate repeats of a divisor...
#  ...by using a different instance of the same factor
# the number of divisors can be calculated from the product of each exponent of prime factors, plus 1
# in this case, (2 + 1)*(1 + 1) = 6
# indeed, there are 6 factors: 1,2,3,4,6,12

n = int(input())

def divCount(n): 
  
    hh = [1] * (n + 1) # using sieve method for prime factorisation
      
    p = 2 # starting with smallest possible non-trivial
    while((p ** 2) < n):  # half of prime factors lie below the square root of n 
                          # e.g. sqrt(12) = 3.46... 1,2,3 < 3.46... 
        if (hh[p] == 1): 
            for i in range((p * 2), n, p):  
                hh[i] = 0 
        p += 1

    total = 1 # the nunber 1 is the multiplicative identity for integers...
              # acting as the basis for the product which will become our "number of divisors"
    for p in range(2, n + 1): # run through all possible divisors, from the smallest non-trivial value, 2, to n (inclusive)
        if (hh[p] == 1): 
  
            count = 0
            if (n % p == 0):  # if n mod p = 0, i.e. no remainder, then p is a divisor
                while (n % p == 0): 
                    n = int(n / p)
                    count += 1  # short hand for count = count + 1 
                total *= (count + 1) # short hand for total = total * (count + 1)
                                     # i.e. the forumula for number of divisors explained above
                  
    return total 
  
print(divCount(n))
