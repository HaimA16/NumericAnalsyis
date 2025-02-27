from colors import bcolors
import sympy as sp


def lagrange_interpolation(x_data, y_data, x):
    """
    Lagrange Interpolation

    Parameters:
    x_data (list): List of x-values for data points.
    y_data (list): List of y-values for data points.
    x (float): The x-value where you want to evaluate the interpolated polynomial.

    Returns:
    float: The interpolated y-value at the given x.
    """
    n = len(x_data)
    result = 0.0

    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if i != j:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        result += term

    return result


def main():

    n = int(input("Enter the number of data points: "))

    x_data = []
    y_data = []
    print("Enter the x and y values (separated by space):")
    for i in range(n):
        x, y = map(float, input(f"Point {i+1}: ").split())
        x_data.append(x)
        y_data.append(y)


    x_interpolate = list(map(float, input("\nEnter the x values to interpolate (separated by spaces): ").split()))


    print("\nInterpolated Values:")
    for x in x_interpolate:
        y_interpolate = lagrange_interpolation(x_data, y_data, x)
        print(f"Interpolated value at x = {x} is y = {round(y_interpolate, 4)}")


if __name__ == "__main__":
    main()
