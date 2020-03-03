# from math import *
# math class comes with a method for gcd:

def gcd(a, b):
  while b!=0:
    a, b = b, a % b
    print(a, b)
  return a
print("gcd(a,b) = %s " % gcd(int(input("a = ")),int(input("b = "))))