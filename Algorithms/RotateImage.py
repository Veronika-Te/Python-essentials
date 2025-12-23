def rotate(matrix):
  """
    Rotate an n x n matrix by 90 degrees clockwise in-place.
    
    Steps:
    1. Transpose the matrix in-place.
    2. Reverse each row to complete the rotation.
  """
  if not matrix:
    return None
  n=(len( matrix))
  for i in range(n):
    for j in range(i+1, row):
      matrix[i][j], matrix[j][i]=matrix[j][i],matrix[i][j]
    
  for i in range(n):
    matrix[i].reverse()
      
  
if __name__=="__main__":
  matrix = [[1,2,3],[4,5,6],[7,8,9]]
  rotate(matrix)
  print(matrix)

