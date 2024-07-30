import random

def get_input():
    """Gets input sizes for matrix, and creates matrix with random numbers"""
    print("Hello please enter equal values for m and n for further calculations(for square matrix)!")
    while (True):
        try:
            m = int(input("Enter m: "))
            n = int(input("Enter n: "))
            if m == n:
               matrix = [[random.randint(10, 99) for _ in range(n)] for _ in range(m)] 
               return matrix
        except:
            print("Please try again")

def print_elements_of_matrix(matrix_lst: list[int])->list:
    """This function prints elements of matrix"""
    if not matrix_lst:
        return 0
    ele_matrix=[]
    for i in matrix_lst:
        for j in i:
            ele_matrix.append(j)
    return ele_matrix


def find_primary_diag_matrix(matrix_lst: list[int])->list:
    """Finds primary(principal) diagonal"""
    if not matrix_lst:
        return 0
    rows=len(matrix_lst)
    ls_p=[]  
    for i in range(rows):
        ls_p.append(matrix_lst[i][i])
    return ls_p

def find_secondary_diag_matrix(matrix_lst: list[int])->list:
    """Find secondary diagonal in the optimal way"""
    if not matrix_lst:
        return 0
    rows=len(matrix_lst)
    columns=len(matrix_lst[0])
    ls_s=[]
    for i in range(rows):
        ls_s.append(matrix_lst[i][rows-i-1])
    return ls_s

def find_secondary_diag_matrix_2(matrix_lst: list[int])->list:
    """Find secondary diagonal"""
    if not matrix_lst:
        return 0
    rows=len(matrix_lst)
    columns=len(matrix_lst[0])
    ls_s=[]
    for i in range(rows):
        for j in range(columns):
            # Condition for secondary diagonal
            if ((i + j) == (rows - 1)):
               ls_s.append(matrix_lst[i][j])
    return ls_s

def printDiagonalSums(matrix_lst: list[int])-> tuple:
    """Prints sums of primary and secondary diagonals"""
    if not matrix_lst:
        return 0
    principal = 0
    secondary = 0
    n=len(matrix_lst)
    for i in range(0, n): 
        principal += matrix_lst[i][i]
        secondary += matrix_lst[i][n - i - 1]
    return principal,secondary


def find_max_in_matrix(matrix_lst: list[int])-> int:
    """This function finds maximum value in the given matrix"""
    max_matrix=matrix_lst[0][0]
    for i in matrix_lst:
       for j in i:
          if j>max_matrix:
             max_matrix=j
    return max_matrix

def initializeEmptymatrix(matrix:list[int])->list[int]:
    """Initializes empty matrix according to sizes of the given matrix"""
    rows = len(matrix)
    cols = len(matrix[0])
    empty_transposed=[]
    for i in range(cols):
        ls=[]
        empty_transposed.append(ls)

    for j in empty_transposed:
        for i in range(rows):
            j.append(0)
    return empty_transposed

def tranposematrix(matrix:list[int], transposed:list[int])->list[int]:
    """Tranposes the given matrix"""
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
           transposed[j][i] = matrix[i][j]
    return transposed


def rotateMatrix (matrix:list[int])->list[int]:
    """This function turns over 180 degree given matrix"""
    ls=[]
    for i in matrix:
        i.reverse()
        ls.append(i)
    ls.reverse()
    return ls
    

def main()->None:

    #matrix_lst=[[1,2,3],[3,4,8],[9,45,6]]
    matrix_lst=get_input()

    #printing matrix 
    for i in matrix_lst:
        print(i)
    
    #printing elements of matrix
    ls=print_elements_of_matrix(matrix_lst)
    print("Elements of matrix are:", ls)
    print("\n")
    print("_______Diagonals_______")
    print("\n")
    #finding primary diagonal
    p_diag=find_primary_diag_matrix(matrix_lst)
    print("Primary diagonal(with 1 loop): ",p_diag)

    #finding secondary diagonal
    s_diag=find_secondary_diag_matrix(matrix_lst)
    print("Secondary diagonal(with 1 loop): ", s_diag)
    
    #finding secondary diagonal
    s_diag=find_secondary_diag_matrix_2(matrix_lst)
    print("Secondary diagonal(with 2 nested loops): ", s_diag)
    print("\n")
    print("_______Sum of Diagonals_______")
    print("\n")
    #finding sums of elements in two different diagonals(1 example)
    print("Sum of elements in primary diagonal: ", sum(p_diag))
    print("Sum of elements in secondary diagonal: ", sum(s_diag))
    
    #finding sums of elements in two different diagonals(2 example)
    res=printDiagonalSums(matrix_lst)
    principal=res[0]
    secondary=res[1]
    print("Principal Diagonal(sum):", principal)
    print("Secondary Diagonal(sum):", secondary)
    print("\n")
    print("_______Max in Matrix_______")
    #Max in matrix
    max_matrix=find_max_in_matrix(matrix_lst)
    print("\nMax value of matrix is: ", max_matrix)
    print("\n")
    #Tranpose
    print("_______Transpose Matrix_______")
    empty_transposed=initializeEmptymatrix(matrix_lst)
    tranposed=tranposematrix(matrix_lst,empty_transposed)
    
    print("Initial matrix: \n")
    #printing matrix 
    for i in matrix_lst:
        print(i)
    print("\n")
    
    print("Transposed matrix: \n")
    for i in tranposed:
        print(i)
    print("\n")
    
    #Rotate
    print("_______Rotate Matrix_______")
    ls=rotateMatrix(matrix_lst)
    print("Rotated 180 degree:")
    print("\n")
    for i in ls:
        print(i)


if __name__=='__main__':
    main()
    

    
