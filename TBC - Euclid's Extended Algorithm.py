#Euclid's Extended Algorithm#

#carry out euclid's algorithm
#store values of a,b from reucursion of a=bq+r
#rearrange each equation for r
#backwards substitution until ax+by=g form 

a = int(input("a = "))
b = int(input("b = "))
c=[]; d=[]; q=[]; r=[]; g=[]

while b!=0:
    c.append(a)
    d.append(b)
    r.append(a%b)
    q.append((a-(a%b))/b)
    a,b = b,a%b
    
print(c)
print(d)
print(q)
print(r)

for i in range(0,len(r)-1):
    c[-2-i]
    d[-2-i]*q[-2-i]
