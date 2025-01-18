import numpy as np

# 1. Create a vector with values ranging from 10 to 49.
arr = np.arange(10,50)
print(arr)
print()


# 2. Create a 3x3 matrix with values ranging from 0 to 8.
arr = np.arange(9).reshape(3,3)
print(arr)
print()


# 3. Create a 3x3 identity matrix.
arr = np.eye(3)
print(arr)
print()


# 4. Create a 3x3x3 array with random values.
arr = np.random.rand(3,3,3)
print(arr)
print()


# 5. Create a 10x10 array with random values and find the minimum and maximum values.
arr = np.random.rand(10,10)
print(arr.min())
print()


# 6. Create a random vector of size 30 and find the mean value.
arr = np.random.rand(30)
print(arr.mean())
print()


# 7. Normalize a 5x5 random matrix.
arr = np.random.rand(5,5)
normalized = (arr - arr.mean(axis=0)) / arr.std(axis=0)
print(normalized)
print()


# 8. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product).
matrix1 = np.random.rand(5, 3)
matrix2 = np.random.rand(3, 2)

result = np.dot(matrix1,matrix2)
print(result)
print()


# 9. Create two 3x3 matrices and compute their dot product.
matrix1 = np.random.rand(3, 3)
matrix2 = np.random.rand(3, 3)
result = np.dot(matrix1, matrix2)

print(result)
print()


# 10. Given a 4x4 matrix, find its transpose.
matrix = np.random.rand(4,4)
transpose = matrix.T
print(transpose)
print()


# 11. Create a 3x3 matrix and calculate its determinant.
matrix = np.random.rand(3,3)
determinant = np.linalg.det(matrix)

print(determinant)
print()


# 12. Create two matrices ( A ) (3x4) and ( B ) (4x3), and compute the matrix product ( A \cdot B ).
matrix_A = np.random.rand(3, 4)
matrix_B = np.random.rand(4, 3)

result = np.dot(matrix_A, matrix_B)
print(result)
print()


# 13. Create a 3x3 random matrix and a 3-element column vector. Compute the matrix-vector product.
matrix = np.random.rand(3, 3)
vector = np.random.rand(3, 1)
result = np.dot(matrix, vector)

print(result)
print()


# 14. Solve the linear system ( Ax = b ) where ( A ) is a 3x3 matrix, and ( b ) is a 3x1 column vector.
matrix_A = np.random.rand(3, 3)
vector_b = np.random.rand(3, 1)

solution = np.linalg.solve(matrix_A, vector_b)

print(solution)
print()


# 15. Given a 5x5 matrix, find the row-wise and column-wise sums.
matrix = np.random.rand(5, 5)

row_sums = matrix.sum(axis=1)
column_sums = matrix.sum(axis=0)
print(row_sums)
print(column_sums)
print()