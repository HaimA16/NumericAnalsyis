import math
import sympy as sp
from colors import bcolors


def trapezoidal_rule(f, a, b, n):
    """
    Trapezoidal Rule for Numerical Integration

    Parameters:
    f (function): The function to be integrated.
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    n (int): The number of subintervals.

    Returns:
    float: The approximate definite integral of the function over [a, b].
    """
    h = (b - a) / n
    T = f(a) + f(b)
    integral = 0.5 * T  # Initialize with endpoints

    for i in range(1, n):
        x_i = a + i * h
        integral += f(x_i)

    integral *= h

    return integral


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

    # קלט עבור מספר תת-החלוקות
    n = int(input("Enter the number of subintervals (default 10): ") or 10)

    # חישוב האינטגרל
    integral = trapezoidal_rule(f, a, b, n)

    # הצגת התוצאה
    print(f"\nDivision into n={n} sections")
    print(bcolors.OKBLUE, f"Numerical Integration of definite integral in range [{a},{b}] is {integral:.6f}", bcolors.ENDC)


if __name__ == "__main__":
    main()
