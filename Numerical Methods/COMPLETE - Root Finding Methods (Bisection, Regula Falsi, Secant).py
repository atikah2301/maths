def bisection(f,a,b,n):
    '''Use bisection method for approximating the roots of a function
    Arguments:
        f : lambda function
        a : upper bound
        b : lower bound
        n : degree of accuracy
    '''

    if f(a)==0:
        print(a+" is the root")
        return a
    elif f(b)==0:
        print(b+" is the root")
        return b
    elif f(a)*f(b)>0:
        print("Failed")
        return None
        
    else:
        while abs(a-b)>n:
            m = (a+b)/2
            print(a,b,m)
            if f(m)==0:
                print(m+" is the root")
                return m
            else:
                if f(a)*f(m)<0:
                    b = m
                elif f(m)*f(b)<0:
                    a = m
                else:
                    print("Failed")
                    return None
                    
#bisection(lambda x: x-3,0,10,0.0001)

def sectant_rf(f,a,b,n):
    '''Use secant method (regula farsi version) for approximating the roots of a function
    Arguments:
        f : lambda function
        a : upper bound
        b : lower bound
        n : degree of accuracy
    '''

    # construct a line between (a,f(a)) and (b,f(b)) using y=f(a)+m(x-a)
    # find the root of that line by letting y=0, so x=a-f(a)/m, and let c=x
    # if f(c)=0 or is sufficiently close, return c
    # elif f(a)*f(c)<0, b=c,
    # elif f(b)*f(c)<0, a=c, i.e. let c replace the value with the same sign as c
    # else failed
    # now computer the new secant and find the new c value, using c=a-f(a)/m

    if f(a)==0:
        print(a+" is the root")
        return a
    elif f(b)==0:
        print(b+" is the root")
        return b
    elif f(a)*f(b)>0:
        print("Failed")
        return None
        
    else:
        while abs(a-b)>n:
            m=(f(a)-f(b))/(a-b)
            c=a-f(a)/m
            print(a,b,c)
            if f(c)==0:
                print(c+" is the root")
                return c
            else:
                if f(a)*f(c)<0:
                    b = c
                elif f(c)*f(b)<0:
                    a = c
                else:
                    print("Failed")
                    return None


















    

