# matrix multiplication code

def matrix_multiply(A, B):
    rows_in_A = len(A); cols_in_A = len(A[0])
    rows_in_B = len(B); cols_in_B = len(B[0])
    if cols_in_A != rows_in_B:
        raise Exception("Matrix dimensions not compatible for multiplication")
    
    C = [[0 for i in range(cols_in_B)] for i in range(rows_in_A)] 
        
    for i in range(rows_in_A):
        for j in range(cols_in_B):
            element = 0
            for k in range(rows_in_B):
                element += A[i][k] * A[k][j]
            C[i][j] = element
    return C
	

# matrix determinant code

def sub_matrix(M, i, j):
    sub = []
    for row in (M[:i] + M[i+1:]): # exclude i-th row of M
        sub.append(row[:j] + row[j+1:]) # exclude j-th element of each row
    return sub

def det(A):
    if len(A) != len(A[0]):
        raise Exception("Only square matrices have determinants")
    
    if len(A) == 2:
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    
    result = 0
    for i in range(len(A[0])):
        coefficient = A[0][i]*((-1)**i)
        result += coefficient*det(sub_matrix(A,0,i))
    
    return result
     
    
if __name__ == '__main__':
    
	A = [[1,2,3],[4,5,6],[7,8,9]] # 3x3 matrix, with det 0
	B = [[1,1],[2,2],[3,3]] # 3x2 matrix
	M = [[1,2,3],[4,6,6],[7,8,9]] # 3x3 matrix, with det -12
  
	matrix_multiply(A, A)
	det(M)