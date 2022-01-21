# Affine Map Inverse Finder #

# An affine map is the function theta that maps x onto ax+b
# for an alphabet of length n
# First find the multiplicative inverse of a, a'
# Then calculate b', where b' is congruent to -ba' mod n

def gcd(a, b):
  while b!=0:
    a, b = b, a%b
  return a

def find_multiplicative_inverse(a,n):
    """
    Return the multiplicative inverse of a mod n
    """
    if a==0 or gcd(a,n)!=1:
        print("Inverse does not exist")
        return -1
    if a==1: return 1
    k=1
    while True:
        a_inv = (1+n*k)/a 
        if a_inv.is_integer():
            return int(a_inv)
        else:
            k=k+1  

def affine_map_inverse(a=1,b=0,n=26):
  """
  For a given affine map, find its inverse, a' and b'
  """
  inv_a = find_multiplicative_inverse(a,n)
  if inv_a != -1:
      inv_b = -b*inv_a % n
      print(f"a'={inv_a} and b'={inv_b}")
  else:
    print(f"This affine map for a={a} and b={b} is invertible for n={n}")

affine_map_inverse(a=5,b=4,n=17)

