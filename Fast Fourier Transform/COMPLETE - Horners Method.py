# The optimal method for evaluating polynomials
# Has time complexity O(n)

def horners_method(poly, x):
    n = len(poly) - 1
    result = poly[0]
    
    for i in range(n):
        result = result*x + poly[i+1]
    
    return result
    

poly = [2, -6, 2, -1]
x = 3
ans = horners_method(poly, x)
print(ans)