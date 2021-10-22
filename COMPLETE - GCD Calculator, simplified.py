# from math import *
# math class comes with a method for gcd:

def gcd(a, b):
  while b!=0:
    a, b = b, a % b
    #print("=gcd("+str(a)+","+str(b)+")")
  return a

while True:
  input_ = input("a,b = ")
  if input_:
    a, b = tuple(input_.split(","))  
    a, b = int(a), int(b)
    print(f"gcd({a},{b})={gcd(a, b)}")
  else:
    break
