# Finding Factors #

def single():
    for i in range(1,x+1):
        if x % i == 0:
            print(i," ", end="")

def pairs():
    values = []
    for i in range(1,x+1):
        if x % i == 0:
            values.append(i)

    while values:
        print(values[0],"*",values[-1])
        del values[0]; del values[-1]

x = int(input("Find factors of: "))
display = input("List factors in pairs? ")

if display == "yes":
    pairs()

if display == "no":
    single()

else:
    while display != "yes" and display != "no":
        display = input("List factors in pairs? ")
        if display == "yes":
            pairs()
            break
        if display == "no":
            single()
            break



