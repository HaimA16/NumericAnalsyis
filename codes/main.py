import sys
import bisection_method
import condition_of_linear_equations
import cubicSpline
import gauss_seidel
import gaussian_elimination
import inverse_matrix
import Jacobi
import lagrange_interpolation
import linear_interpolation
import LU_factorization
import neville_method
import newtonRapson
import polynomial_interpolation
import secant_method
import simpson_method
import romberg_method
import trapez_method

def display_menu():
    print("\nNumerical Methods Menu:")
    print("1. Bisection Method")
    print("2. Condition of Linear Equations")
    print("3. Cubic Spline Interpolation")
    print("4. Gauss-Seidel Method")
    print("5. Gaussian Elimination")
    print("6. Inverse Matrix Calculation")
    print("7. Jacobi Method")
    print("8. Lagrange Interpolation")
    print("9. Linear Interpolation")
    print("10. LU Factorization")
    print("11. Neville Method")
    print("12. Newton-Raphson Method")
    print("13. Polynomial Interpolation")
    print("14. Secant Method")
    print("15. Simpson's Rule")
    print("16. Romberg Integration")
    print("17. Trapezoidal Rule")
    print("0. Exit")

def main():
    modules = {
        '1': bisection_method,
        '2': condition_of_linear_equations,
        '3': cubicSpline,
        '4': gauss_seidel,
        '5': gaussian_elimination,
        '6': inverse_matrix,
        '7': Jacobi,
        '8': lagrange_interpolation,
        '9': linear_interpolation,
        '10': LU_factorization,
        '11': neville_method,
        '12': newtonRapson,
        '13': polynomial_interpolation,
        '14': secant_method,
        '15': simpson_method,
        '16': romberg_method,
        '17': trapez_method,
    }

    while True:
        display_menu()
        choice = input("Enter your choice (0-17): ")
        if choice == '0':
            print("Exiting the program.")
            sys.exit()
        elif choice in modules:
            print(f"\nRunning {modules[choice].__name__}...\n")
            if hasattr(modules[choice], "main"):
                modules[choice].main()
            else:
                print(f"Error: The module '{modules[choice].__name__}' does not have a main() function.")
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
