#Atikah's GCD calculator#

def gcd():

    print('\n gcd calculator \n')

    a = input('a = ')
    while a.isnumeric() == False:
        a = input('Enter a positive integer. a = ')
    a = int(a)

    b = input('b = ')
    while b.isnumeric() == False:
        b = input('Enter a positive integer. b = ')
    b = int(b)

    if b > a:
        b, a = a, b

    # a = b*q + r
    # gcd(a,b) = gcd(b,r)
    # gcd(a,0) = a

    while b > 0:
        
        q = a // b # previously used math.floor(a/b) from import math
        r = a - b*q
        print(a,'=',b,'*',q,'+',r)
        a = b
        b = r
        

    print('gcd(a,b) = ',a)

while True:
        gcd()


    


