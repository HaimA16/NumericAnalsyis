from colors import bcolors

"""
A function that performs linear interpolation between two points in a table.
Parameters:
- table_points: a list of tuples representing (x, y) points in the table
- point: the point at which to interpolate
Returns:
- None
"""

def linearInterpolation(table_points, point):
    p = [table_points[i][0] for i in range(len(table_points))]
    result = 0
    flag = 1

    for i in range(len(p) - 1):
        if p[i] <= point <= p[i + 1]:
            x1, y1 = table_points[i]
            x2, y2 = table_points[i + 1]
            result = (((y1 - y2) / (x1 - x2)) * point) + ((y2 * x1) - (y1 * x2)) / (x1 - x2)
            print(bcolors.OKGREEN, f"\nThe approximation (interpolation) of the point {point} is: {round(result, 4)}", bcolors.ENDC)
            flag = 0
            break

    if flag:
        x1, y1 = table_points[0]
        x2, y2 = table_points[1]
        m = (y1 - y2) / (x1 - x2)
        result = y1 + m * (point - x1)
        print(bcolors.OKGREEN, f"\nThe approximation (extrapolation) of the point {point} is: {round(result, 4)}", bcolors.ENDC)


def main():

    n = int(input("Enter the number of data points: "))

    table_points = []
    print("Enter the x and y values (separated by space):")
    for i in range(n):
        x, y = map(float, input(f"Point {i+1}: ").split())
        table_points.append((x, y))


    x_interpolate = list(map(float, input("\nEnter the x values to interpolate (separated by spaces): ").split()))


    print("\nInterpolation & Extrapolation Results:")
    for x in x_interpolate:
        linearInterpolation(table_points, x)


if __name__ == "__main__":
    main()
