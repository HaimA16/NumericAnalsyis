from colors import bcolors
import sympy as sp

def newton_raphson(f, df, p0, TOL, N=50):
    print("{:<10} {:<15} {:<15} ".format("Iteration", "p0", "p1"))
    for i in range(N):
        if df(p0) == 0:
            print("Derivative is zero at p0, method cannot continue.")
            return None
        p = p0 - f(p0) / df(p0)
        if abs(p - p0) < TOL:
            return p  # Procedure completed successfully
        print("{:<10} {:<15.9f} {:<15.9f} ".format(i, p0, p))
        p0 = p
    return p


def main():
    # הגדרת משתנה x עבור חישוב נגזרות
    x = sp.symbols('x')

    # קלט פונקציה מהמשתמש
    expr = input("Enter the function f(x): (example: (2*x*exp(-x) + log(2*x**2)) * (2*x**4 + 2*x**2 - 3*x - 5)) ")
    f_expr = sp.sympify(expr)
    f = sp.lambdify(x, f_expr, 'numpy')

    # חישוב נגזרת באופן אוטומטי
    df_expr = sp.diff(f_expr, x)
    df = sp.lambdify(x, df_expr, 'numpy')

    # קלט עבור שאר הפרמטרים
    p0 = float(input("\nEnter the initial guess p0: "))
    TOL = float(input("Enter the tolerance (default 1e-6): ") or 1e-6)
    N = int(input("Enter the maximum number of iterations (default 100): ") or 100)

    # הרצת האלגוריתם
    root = newton_raphson(f, df, p0, TOL, N)

    if root is not None:
        print(bcolors.OKBLUE, f"\nThe equation f(x) has an approximate root at x = {root:.9f}", bcolors.ENDC)


if __name__ == "__main__":
    main()
