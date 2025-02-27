import numpy as np
from numpy.linalg import norm

from colors import bcolors
from matrix_utility import is_diagonally_dominant


def gauss_seidel(A, b, X0, TOL=1e-16, N=200):
    n = len(A)
    k = 1

    if is_diagonally_dominant(A):
        print('Matrix is diagonally dominant - performing Gauss-Seidel algorithm\n')

    print(
        "Iteration" + "\t\t\t".join([" {:>12}".format(var) for var in ["x{}".format(i) for i in range(1, len(A) + 1)]]))
    print("-----------------------------------------------------------------------------------------------")
    x = np.zeros(n, dtype=np.double)
    while k <= N:

        for i in range(n):
            sigma = 0
            for j in range(n):
                if j != i:
                    sigma += A[i][j] * x[j]
            x[i] = (b[i] - sigma) / A[i][i]

        print("{:<15} ".format(k) + "\t\t".join(["{:<15} ".format(val) for val in x]))

        if norm(x - X0, np.inf) < TOL:
            return tuple(x)

        k += 1
        X0 = x.copy()

    print("Maximum number of iterations exceeded")
    return tuple(x)


def main():
    # קלט מספר המשתמש למטריצה A
    n = int(input("Enter the size of the matrix (n x n): "))

    print("Enter the matrix A row by row (separate numbers with spaces):")
    A = []
    for i in range(n):
        row = list(map(float, input(f"Row {i + 1}: ").split()))
        A.append(row)

    A = np.array(A)


    print("\nEnter the vector b (separate numbers with spaces):")
    b = np.array(list(map(float, input().split())))


    print("\nEnter the initial guess X0 (separate numbers with spaces):")
    X0 = np.array(list(map(float, input().split())))


    TOL = float(input("\nEnter the tolerance (default 1e-16): ") or 1e-16)
    N = int(input("Enter the maximum number of iterations (default 200): ") or 200)


    solution = gauss_seidel(A, b, X0, TOL, N)
    print(bcolors.OKBLUE, "\nApproximate solution:", solution, bcolors.ENDC)


if __name__ == "__main__":
    main()
