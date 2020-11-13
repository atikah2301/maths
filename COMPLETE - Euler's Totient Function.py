#Euler's Totient Function#

#Count the number of totients
#A totient, t, of natural number n is defined as being:
#coprime to n and no greater than n
#i.e. gcd(z,n)=1 and z<=n

print("Finding Totients for Euler's Totient Function\n")

n = int(input("n = "))
z = [] # list of numbers no greater than n
g = [] # list of GCDs corresponding to z[i]
t = [] # list of z[i] with corresponding g[i]==1 i.e. totients


i = 1
while i <= n:
    z.append(i)
    i += 1

i = 0
while i < n:
    a = n # assign n to a dummy variable
    b = z[i] # assign each z[i] to a dummy variable
    while b != 0:
        a , b = b, a%b
    g.append(a)
    if a == 1:
        t.append(z[i])
    i += 1

print("\n Integers z <= n:",z)
print("\n gcd(z,n):",g)
print("\n Thus, the totients of n are:",t)
print("\n Cardinality (ETF Output):",len(t))
