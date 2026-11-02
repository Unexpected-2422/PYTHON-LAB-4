"""Question 2 - Butterfly Pattern.

Takes the number of rows n and prints a butterfly star pattern.
"""


def print_butterfly_row(stars, spaces):
    # Left wing
    for _ in range(stars):
        print("*", end="")
    # Gap in the middle
    for _ in range(spaces):
        print(" ", end="")
    # Right wing
    for _ in range(stars):
        print("*", end="")
    print()


def print_butterfly(n):
    # Increasing section (rows 1 to n)
    for row in range(1, n + 1):
        stars = row
        spaces = 2 * (n - row)
        print_butterfly_row(stars, spaces)

    # Decreasing section (rows n-1 down to 1)
    for row in range(n - 1, 0, -1):
        stars = row
        spaces = 2 * (n - row)
        print_butterfly_row(stars, spaces)


def main():
    n = int(input("Enter the number of rows: "))

    if n <= 0:
        print("Please enter a positive number.")
        return

    print_butterfly(n)


if __name__ == "__main__":
    main()
