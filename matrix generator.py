import numpy as np

def generate_positive_symmetric_integer_matrix(size, max_value=10):

    lower_triangle = np.tril(np.random.randint(1, max_value, size=(size, size))) #generating lower triangular amtrix
    
    symmetric_matrix = lower_triangle + lower_triangle.T - np.diag(lower_triangle.diagonal()) #copy lower triangle to upper for symmetry..
    
    positive_definite_matrix = symmetric_matrix + size * np.eye(size)
    
    return positive_definite_matrix.astype(int)

def save_matrix_to_file(matrix, file_path):
    np.savetxt(file_path, matrix, fmt='%d', delimiter=',')

matrix_size = int(input("Enter the size: "))
result_matrix = generate_positive_symmetric_integer_matrix(matrix_size, max_value=10)

print("Generated Positive Symmetric Integer Matrix:")
print(result_matrix)

file_path = "matrix.csv"   #saving the matrix to matrix.csv
save_matrix_to_file(result_matrix, file_path)
