# Importing NumPy Library
import numpy as np
import sys
import jacobi_method

n = int(input('Enter number of unknowns: '))

a = np.zeros((n, n + 1))

x = np.zeros(n)

print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n + 1):
        a[i][j] = float(input('a[' + str(i) + '][' + str(j) + ']='))

for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Divide by zero detected!')

    for j in range(i + 1, n):
        ratio = a[j][i] / a[i][i]

        for k in range(n + 1):
            a[j][k] = a[j][k] - ratio * a[i][k]

x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]

for i in range(n - 2, -1, -1):
    x[i] = a[i][n]

    for j in range(i + 1, n):
        x[i] = x[i] - a[i][j] * x[j]

    x[i] = x[i] / a[i][i]

print('\nRequired solution by Gauss Elimination Method is: ')
for i in range(n):
    print('X%d = %0.2f' % (i, x[i]), end='\t')

# X0 = 2.00	X1 = -1.00	X2 = 1.00	X3 = 2.00
jacobi_method.jacobi_method()
