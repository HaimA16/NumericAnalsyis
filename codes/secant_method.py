from colors import bcolors
import sympy as sp

def secant_method(f, x0, x1, TOL, N=50):
    print("{:<10} {:<15} {:<15} {:<15}".format("Iteration", "xo", "x1", "p"))
    for i in range(N):
        if f(x1) - f(x0) == 0:
            print("Method cannot continue.")
            return
        p = x0 - f(x0) * ((x1 - x0) / (f(x1) - f(x0)))
        if abs(p - x1) < TOL:
            return p  # Procedure completed successfully
        print("{:<10} {:<15.6f} {:<15.6f} {:<15.6f}".format(i, x0, x1, p))
        x0 = x1
        x1 = p
    return p

def main():
    try:
        expr = input("Enter the function f(x): ").strip()
        x = sp.symbols('x')
        f_expr = sp.sympify(expr)
        f = sp.lambdify(x, f_expr, 'math')

        x0 = float(input("Enter first initial guess x0: ").strip())
        x1 = float(input("Enter second initial guess x1: ").strip())
        tol_input = input("Enter the tolerance (default 1e-6): ").strip()
        tol = float(tol_input) if tol_input else 1e-6
        n = int(input("Enter maximum iterations (default 50): ") or 50)

        root = secant_method(f, x0, x1, tol, n)
        print(bcolors.OKBLUE, f"\nThe equation f(x) has an approximate root at x = {root}", bcolors.ENDC)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
