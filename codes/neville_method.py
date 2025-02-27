from colors import bcolors

def neville(x_data, y_data, x_interpolate):
    n = len(x_data)

    # Initialize the tableau
    tableau = [[0.0] * n for _ in range(n)]

    for i in range(n):
        tableau[i][0] = y_data[i]

    for j in range(1, n):
        for i in range(n - j):
            tableau[i][j] = ((x_interpolate - x_data[i + j]) * tableau[i][j - 1] -
                             (x_interpolate - x_data[i]) * tableau[i + 1][j - 1]) / (x_data[i] - x_data[i + j])

    return tableau[0][n - 1]


def main():
    # קלט מספר המשתמש עבור נקודות ה- x וה- y
    n = int(input("Enter the number of data points: "))

    x_data = []
    y_data = []
    print("Enter the x and y values (separated by space):")
    for i in range(n):
        x, y = map(float, input(f"Point {i+1}: ").split())
        x_data.append(x)
        y_data.append(y)

    # קלט עבור נקודה להערכה
    x_interpolate = float(input("\nEnter the x value to interpolate: "))

    # חישוב והצגת התוצאה
    interpolated_value = neville(x_data, y_data, x_interpolate)
    print(bcolors.OKBLUE, f"\nInterpolated value at x = {x_interpolate} is y = {round(interpolated_value, 4)}", bcolors.ENDC)


if __name__ == "__main__":
    main()
