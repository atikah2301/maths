from tabulate import tabulate

def gcd(a, b):
  while b!=0:
    a, b = b, a%b
  return a

def find_inverse(a,n):
    """
    Return the multiplicative inverse of a mod n
    """
    if a==0 or gcd(a,n)!=1: return "."
    if a==1: return 1
    k=1
    while True:
        a_inv = (1+n*k)/a 
        if a_inv.is_integer():
            return int(a_inv)
        else:
            k=k+1        

def find_all_inverses(n):
    """
    Return a list of all the multiplicative inverses of a mod n 
    """
    all_a_inv = []
    for a in range(n):
        all_a_inv.append(find_inverse(a,n))
    return all_a_inv

def table_of_inverses(n):
    all_a = list(range(n))
    all_a.insert(0,"a")
    all_inv = find_all_inverses(n)
    all_inv.insert(0,"Inverse")
    table = tabulate([all_a, all_inv])
    print(table)

table_of_inverses(26)