import numpy as np

def matrix_addition(A,B):
    return np.add(A,B)

def matrix_mult(A,B):
    return A @ B

def matrix_transpose(A,B):
    return A.T

def matrix_det(A,B):
    return np.linalg.det(A)

def matrix_inverse(A,B):
    return np.linalg.inv(A)

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

print(matrix_addition(A,B))
print(matrix_mult(A,B))
print(matrix_transpose(A,B))
print(matrix_det(A,B))
print(matrix_inverse(A,B))



