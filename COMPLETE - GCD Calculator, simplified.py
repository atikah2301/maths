# from math import *
# math class comes with a method for gcd:

def gcd(a, b):
  while b!=0:
    a, b = b, a % b
    #print("=gcd("+str(a)+","+str(b)+")")
  return a
