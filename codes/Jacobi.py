import numpy as np
from numpy.linalg import norm
from matrix_utility import is_diagonally_dominant


def swap_row(mat, i, j):
    mat[[i, j]] = mat[[j, i]]


def get_best_diagonal(mat, n):
    for i in range(n):
        pivot_row = i
        v_max = mat[pivot_row][i]
        for j in range(i + 1, n):
            if abs(mat[j][i]) > abs(v_max):
                v_max = mat[j][i]
                pivot_row = j

        if not mat[pivot_row][i]:
            return i  # Matrix is singular

        if pivot_row != i:
            swap_row(mat, i, pivot_row)
    return -1


def check_if_singular(mat, b, n):
    singular_flag = get_best_diagonal(mat, n)
    if singular_flag != -1:
        if b[singular_flag]:
            print("Singular Matrix (Inconsistent System)")
            return 0
        else:
            print("Singular Matrix (May have infinitely many solutions)")
            return 0
    return -1


def get_D(mat, n):
    return np.diag(np.diag(mat))


def get_L(mat, n):
    return np.tril(mat, k=-1)


def get_U(mat, n):
    return np.triu(mat, k=1)


def get_jacobi_H(mat, n):
    return np.linalg.inv(get_D(mat, n))


def get_jacobi_G(mat, n):
    inverse_of_D = np.linalg.inv(get_D(mat, n))
    return -np.dot(inverse_of_D, get_L(mat, n) + get_U(mat, n))


def jacobi_iterative(mat, b, n, X0, TOL=0.001):
    H = get_jacobi_H(mat, n)
    G = get_jacobi_G(mat, n)
    k = 1

    print("\nJacobi Method Iterations:")
    print("Iteration" + "\t\t\t".join(
        [" {:>12}".format(var) for var in ["x{}".format(i) for i in range(1, len(mat) + 1)]]))
    print("-----------------------------------------------------------------------------------------------")

    while True:
        x = np.dot(G, X0) + np.dot(H, b)
        print("{:<15} ".format(k) + "\t\t".join(["{:<15} ".format(val) for val in x]))

        if norm(x - X0, np.inf) < TOL:
            return tuple(x)

        k += 1
        X0 = x.copy()


def get_jacobi_solution(mat, b, n, X0, TOL):
    if check_if_singular(mat, b, n) == -1:
        if not is_diagonally_dominant(mat):
            print('Matrix is not diagonally dominant!\n')
        else:
            return jacobi_iterative(mat, b, n, X0, TOL)


def main():
    # קלט מספר המשתמש למטריצה A
    n = int(input("Enter the size of the matrix (n x n): "))

    print("Enter the matrix A row by row (separate numbers with spaces):")
    A = []
    for i in range(n):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        A.append(row)

    A = np.array(A)

    # קלט לווקטור b
    print("\nEnter the vector b (separate numbers with spaces):")
    b = np.array(list(map(float, input().split())))

    # קלט לערכי האתחול X0
    print("\nEnter the initial guess X0 (separate numbers with spaces):")
    X0 = np.array(list(map(float, input().split())))

    # קלט לסובלנות
    TOL = float(input("\nEnter the tolerance (default 0.001): ") or 0.001)

    # הרצת האלגוריתם
    solution = get_jacobi_solution(A, b, n, X0, TOL)
    print("\nApproximate solution:", solution)


if __name__ == "__main__":
    main()
