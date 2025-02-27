import math
import numpy as np
import sympy as sp
from colors import bcolors

def simpsons_rule(f, a, b, n):
    """
    Simpson's Rule for Numerical Integration

    Parameters:
    f (function): The function to be integrated.
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    n (int): The number of subintervals (must be even).

    Returns:
    float: The approximate definite integral of the function over [a, b].
    """
    if n % 2 != 0:
        raise ValueError("Number of subintervals (n) must be even for Simpson's Rule.")

    h = (b - a) / n

    integral = f(a) + f(b)  # Initialize with endpoints

    for i in range(1, n):
        x_i = a + i * h
        if i % 2 == 0:
            integral += 2 * f(x_i)
        else:
            integral += 4 * f(x_i)

    integral *= h / 3

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

    # קלט עבור מספר תת-החלוקות (חייב להיות זוגי)
    while True:
        n = int(input("Enter the number of subintervals (even number, default 10): ") or 10)
        if n % 2 == 0:
            break
        print("Error: Number of subintervals must be even. Please enter again.")

    # חישוב האינטגרל
    integral = simpsons_rule(f, a, b, n)

    # הצגת התוצאה
    print(f"\nDivision into n={n} sections")
    print(bcolors.OKBLUE, f"Numerical Integration of definite integral in range [{a},{b}] is {integral:.6f}", bcolors.ENDC)


if __name__ == "__main__":
    main()
