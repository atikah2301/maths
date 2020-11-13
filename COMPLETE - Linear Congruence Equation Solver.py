# finding  multipilcative inverses, xi
# i.e. solving equations of the form "ax is congruent to 1 mod n" , where x is unknown

a = int(input("coefficient of x = "))
n = int(input("modulus n = "))
print("Solving for x where "+str(a)+"x is congruent to 1 mod "+str(n))

mod = list(range(1,10000,n)) #creating the 0 residue congruence class for positive integers
mod_2 = list(range(1,-10000,-n)) #creating the same for negative integers
mod.extend(mod_2) #combining into one list

for i in range(1,1000):
    if a*i % n == 1:
        print("x =",i,"is a solution")
        break 