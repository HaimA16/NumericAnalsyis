import numpy as np
import sympy as sp
from colors import bcolors


def romberg_integration(func, a, b, n):
    """
    Romberg Integration

    Parameters:
    func (function): The function to be integrated.
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    n (int): The number of iterations (higher value leads to better accuracy).

    Returns:
    float: The approximate definite integral of the function over [a, b].
    """
    h = b - a
    R = np.zeros((n, n), dtype=float)

    R[0, 0] = 0.5 * h * (func(a) + func(b))

    for i in range(1, n):
        h /= 2
        sum_term = 0

        for k in range(1, 2 ** i, 2):
            sum_term += func(a + k * h)

        R[i, 0] = 0.5 * R[i - 1, 0] + h * sum_term

        for j in range(1, i + 1):
            R[i, j] = R[i, j - 1] + (R[i, j - 1] - R[i - 1, j - 1]) / ((4 ** j) - 1)

    return R[n - 1, n - 1]


def main():
    # הגדרת משתנה x
    x = sp.symbols('x')

    # קלט עבור הפונקציה
    expr = input("Enter the function f(x): ")
    f_expr = sp.sympify(expr)
    f = sp.lambdify(x, f_expr, 'numpy')

    # קלט עבור גבולות האינטגרציה
    a = float(input("Enter the lower limit of integration (a): "))
    b = float(input("Enter the upper limit of integration (b): "))

    # קלט עבור מספר האיטרציות
    n = int(input("Enter the number of iterations (higher value = better accuracy, default 5): ") or 5)

    # חישוב האינטגרל
    integral = romberg_integration(f, a, b, n)

    # הצגת התוצאה
    print(f"\nDivision into n={n} sections")
    print(bcolors.OKBLUE, f"Approximate integral in range [{a},{b}] is {integral:.6f}", bcolors.ENDC)


if __name__ == "__main__":
    main()
