import math
import numpy as np
import sympy as sp
from colors import bcolors


def max_steps(a, b, err):
    s = int(np.floor(- np.log2(err / (b - a)) / np.log2(2) - 1))
    return s


def bisection_method(f, a, b, tol=1e-6):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("The scalars a and b do not bound a root")
    c, k = 0, 0
    steps = max_steps(a, b, tol)

    print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("Iteration", "a", "b", "f(a)", "f(b)", "c", "f(c)"))

    while abs(b - a) > tol and k < steps:
        c = a + (b - a) / 2

        if f(c) == 0:
            return c

        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

        print("{:<10} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f}".format(k, a, b, f(a), f(b), c, f(c)))
        k += 1

    return c


def main():
    try:
        expr = input("Enter the function f(x): ").strip()
        x = sp.symbols('x')
        f_expr = sp.sympify(expr)
        f = sp.lambdify(x, f_expr, 'math')

        a = float(input("Enter the lower bound (a): ").strip())
        b = float(input("Enter the upper bound (b): ").strip())
        tol_input = input("Enter the tolerance (default 1e-6): ").strip()
        tol = float(tol_input) if tol_input else 1e-6

        roots = bisection_method(f, a, b, tol)
        print(bcolors.OKBLUE, f"\nThe equation f(x) has an approximate root at x = {roots}", bcolors.ENDC, )
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
