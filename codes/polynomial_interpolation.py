from colors import bcolors
import numpy as np
from matrix_utility import *


def GaussJordanElimination(matrix, vector):
    matrix, vector = RowXchange(matrix, vector)
    invert = InverseMatrix(matrix, vector)
    return MulMatrixVector(invert, vector)


def UMatrix(matrix, vector):
    U = MakeIMatrix(len(matrix), len(matrix))
    for i in range(len(matrix[0])):
        matrix, vector = RowXchageZero(matrix, vector)
        for j in range(i + 1, len(matrix)):
            elementary = MakeIMatrix(len(matrix[0]), len(matrix))
            elementary[j][i] = -(matrix[j][i]) / matrix[i][i]
            matrix = MultiplyMatrix(elementary, matrix)
    U = MultiplyMatrix(U, matrix)
    return U


def LMatrix(matrix, vector):
    L = MakeIMatrix(len(matrix), len(matrix))
    for i in range(len(matrix[0])):
        matrix, vector = RowXchageZero(matrix, vector)
        for j in range(i + 1, len(matrix)):
            elementary = MakeIMatrix(len(matrix[0]), len(matrix))
            elementary[j][i] = -(matrix[j][i]) / matrix[i][i]
            L[j][i] = (matrix[j][i]) / matrix[i][i]
            matrix = MultiplyMatrix(elementary, matrix)
    return L


def SolveLU(matrix, vector):
    matrixU = UMatrix(matrix, vector)
    matrixL = LMatrix(matrix, vector)
    return MultiplyMatrix(InverseMatrix(matrixU), MultiplyMatrix(InverseMatrix(matrixL), vector))


def solveMatrix(matrixA, vectorb):
    detA = Determinant(matrixA, 1)
    print(bcolors.YELLOW, "\nDET(A) = ", detA)

    if detA != 0:
        print("CondA = ", Cond(matrixA, InverseMatrix(matrixA, vectorb)), bcolors.ENDC)
        print(bcolors.OKBLUE, "\nNon-Singular Matrix - Perform GaussJordanElimination", bcolors.ENDC)
        result = GaussJordanElimination(matrixA, vectorb)
        print(np.array(result))
        return result
    else:
        print("Singular Matrix - Perform LU Decomposition\n")
        print("Matrix U: \n")
        print(np.array(UMatrix(matrixA, vectorb)))
        print("\nMatrix L: \n")
        print(np.array(LMatrix(matrixA, vectorb)))
        print("\nMatrix A=LU: \n")
        result = MultiplyMatrix(LMatrix(matrixA, vectorb), UMatrix(matrixA, vectorb))
        print(np.array(result))
        return result


def polynomialInterpolation(table_points, x):
    matrix = [[point[0] ** i for i in range(len(table_points))] for point in table_points]
    b = [[point[1]] for point in table_points]

    print(bcolors.OKBLUE, "The matrix obtained from the points: ", bcolors.ENDC, '\n', np.array(matrix))
    print(bcolors.OKBLUE, "\nb vector: ", bcolors.ENDC, '\n', np.array(b))
    matrixSol = solveMatrix(matrix, b)

    result = sum([matrixSol[i][0] * (x ** i) for i in range(len(matrixSol))])
    print(bcolors.OKBLUE, "\nThe polynomial:", bcolors.ENDC)
    print('P(X) = ' + ' + '.join([f'({matrixSol[i][0]}) * x^{i}' for i in range(len(matrixSol))]))
    print(bcolors.OKGREEN, f"\nThe Result of P(X={x}) is:", bcolors.ENDC, round(result, 4))
    return result


def main():

    n = int(input("Enter the number of data points: "))

    table_points = []
    print("Enter the x and y values (separated by space):")
    for i in range(n):
        x, y = map(float, input(f"Point {i+1}: ").split())
        table_points.append((x, y))


    x = float(input("\nEnter the x value to interpolate: "))


    print(bcolors.OKBLUE, "----------------- Interpolation & Extrapolation Methods -----------------\n", bcolors.ENDC)
    print(bcolors.OKBLUE, "Table Points: ", bcolors.ENDC, table_points)
    print(bcolors.OKBLUE, "Finding an approximation to the point: ", bcolors.ENDC, x, '\n')
    polynomialInterpolation(table_points, x)
    print(bcolors.OKBLUE, "\n---------------------------------------------------------------------------\n", bcolors.ENDC)


if __name__ == "__main__":
    main()
