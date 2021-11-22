#every divisor of n is some combination of factors from its unique prime factorisation
#e.g. n = 12 = 2*2*3 = 2**2 * 3**1
#here the exponents are 2 and 1
#the number of divisors is the product of each exponent of prime factors plus 1
#in this case, (2 + 1)*(1 + 1) = 6
#indeed, there are 6 factors: 1,2,3,4,6,12

n = int(input("Count number of divisors for: "))


def divCount(n): 
  
  
    hh = [1] * (n + 1) 
      
    p = 2
    while((p * p) < n): 
        if (hh[p] == 1): 
            for i in range((p * 2), n, p): 
                hh[i] = 0 
        p += 1

    total = 1 
    for p in range(2, n + 1): 
        if (hh[p] == 1): 
  
 
            count = 0
            if (n % p == 0): 
                while (n % p == 0): 
                    n = int(n / p)
                    count += 1 
                total *= (count + 1)
                  
    return total 
  
print(divCount(n))
