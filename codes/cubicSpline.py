import numpy as np


def compute_cubic_spline_coefficients(x, y):
    n = len(x) - 1
    h = [x[i + 1] - x[i] for i in range(n)]
    alpha = [3 * (y[i + 1] - y[i]) / h[i] - 3 * (y[i] - y[i - 1]) / h[i - 1] for i in range(1, n)]

    # Set up the system of equations
    l = [1] + [2 * (h[i - 1] + h[i]) for i in range(1, n)] + [1]
    mu = [0] + [h[i] / (h[i - 1] + h[i]) for i in range(1, n)]
    z = [0] * (n + 1)

    # Forward elimination
    for i in range(1, n):
        l[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * mu[i - 1]
        mu[i] = h[i] / l[i]
        alpha[i - 1] = (alpha[i - 1] - h[i - 1] * z[i - 1]) / l[i]
        z[i] = alpha[i - 1] - mu[i] * z[i]

    # Back substitution
    c = [0] * (n + 1)
    b = [0] * n
    d = [0] * n
    for j in range(n - 1, -1, -1):
        c[j] = z[j] - mu[j] * c[j + 1]
        b[j] = (y[j + 1] - y[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    # Coefficients for the cubic spline
    a = y[:-1]
    return a, b, c[:-1], d


def evaluate_natural_cubic_spline(x, y, x_vals):
    a, b, c, d = compute_cubic_spline_coefficients(x, y)
    y_vals = []
    for x_val in x_vals:
        for i in range(len(x) - 1):
            if x[i] <= x_val <= x[i + 1]:
                dx = x_val - x[i]
                y_val = a[i] + b[i] * dx + c[i] * dx ** 2 + d[i] * dx ** 3
                y_vals.append(round(y_val, 4))
                break
    return y_vals


def main():
    # קלט מהמשתמש עבור x ו- y
    n = int(input("Enter the number of data points: "))

    x_data = []
    y_data = []
    print("Enter the x and y values (separated by space):")
    for i in range(n):
        x, y = map(float, input(f"Point {i + 1}: ").split())
        x_data.append(x)
        y_data.append(y)

    x_data = np.array(x_data)
    y_data = np.array(y_data)

    # קלט עבור נקודות להערכה
    x_vals = list(map(float, input("Enter the x values to evaluate (separated by spaces): ").split()))

    # חישוב והדפסה של התוצאות
    y_vals = evaluate_natural_cubic_spline(x_data, y_data, x_vals)

    for i, x_val in enumerate(x_vals):
        print(f"f({x_val}) ≈ {y_vals[i]}")


if __name__ == "__main__":
    main()
