#Atikah's GCD calculator#
#greatest integer that will divide two given integers

def gcd(): 

    print('\n gcd calculator \n')
    
    # using str.isnumeric() as a fail safe for non-positive integer inputs
        
    a = input('a = ')
    while a.isnumeric() == False:
        a = input('Enter a positive integer. a = ')
    a = int(a)

    b = input('b = ')
    while b.isnumeric() == False:
        b = input('Enter a positive integer. b = ')
    b = int(b)
    
    # swap a and b such that a is greater, if not already the case
    
    if b > a:
        b, a = a, b

    # a and b are related by the following: a = b*q + r ...
    # ...where q is the quotient a over b, and r is the remainder
    # the theorem gcd(a,b) = gcd(b,r) allows for iterations of the gcd to be taken..
    # ...with increasingly small values until r=0
    # gcd(a,0) = a is always the last iteration

    while b > 0:
        
        q = a // b # floor division rounding to the next integer down
        r = a - b*q 
        print(a,'=',b,'*',q,'+',r) # full steps are needed to later apply euclid's extended algorithm
        a = b
        b = r
        
    print('gcd(a,b) = ',a)



    


