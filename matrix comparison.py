import numpy as np
import scipy
import time

def load_matrix_from_file(file_path):
    return np.loadtxt(file_path, delimiter=',')

def decompose_matrix(matrix):

    #QR decomposition:
    start_time = time.time()
    q, r = np.linalg.qr(matrix)
    qr_time = time.time() - start_time

    #LU decomposition:
    start_time = time.time()
    p, l, u = scipy.linalg.lu(matrix)
    lu_time = time.time() - start_time

    #Cholesky decomposition"
    start_time = time.time()
    cholesky = np.linalg.cholesky(matrix)
    cholesky_time = time.time() - start_time

    return qr_time, lu_time, cholesky_time



file_path = "matrix.csv"
loaded_matrix = load_matrix_from_file(file_path)

n = int(input("Enter the number of times to run the comparison: "))

total_qr_time, total_lu_time, total_cholesky_time = 0, 0, 0

for _ in range(n):
    qr_time, lu_time, cholesky_time = decompose_matrix(loaded_matrix)
    total_qr_time += qr_time
    total_lu_time += lu_time
    total_cholesky_time += cholesky_time

average_qr_time = total_qr_time / n
average_lu_time = total_lu_time / n
average_cholesky_time = total_cholesky_time / n

print(f"Average QR Decomposition Time: {average_qr_time}")
print(f"Average LU Decomposition Time: {average_lu_time}")
print(f"Average Cholesky Decomposition Time: {average_cholesky_time}")

#ratio output with rounded values:
qr_ratio = average_qr_time / average_lu_time
lu_ratio = average_lu_time / average_cholesky_time
cholesky_ratio = 1                                      #cholesky as the base (1)
print(f"Average Time Ratio (QR:LU:Cholesky): {qr_ratio:.2f}:{lu_ratio:.2f}:{cholesky_ratio:.2f}")
print(f"Average Time Ratio (rounded) (QR:LU:Cholesky): {round(qr_ratio):.2f}:{round(lu_ratio):.2f}:{cholesky_ratio:.2f}")