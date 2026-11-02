"""Question 1 - Hollow Diamond.

Takes an odd number n and prints a hollow diamond pattern.
"""


def print_hollow_diamond(n):
    middle = n // 2  # index of the widest row

    for row in range(n):
        # distance of this row from the top/bottom tip (0 at the tips)
        offset = row if row <= middle else n - 1 - row

        leading_spaces = middle - offset
        inner_spaces = 2 * offset - 1  # spaces between the two stars

        # Print leading spaces
        for _ in range(leading_spaces):
            print(" ", end="")

        # Print the first star
        print("*", end="")

        # Print the second star (only if the row has two stars)
        if offset > 0:
            for _ in range(inner_spaces):
                print(" ", end="")
            print("*", end="")

        print()  # move to the next line


def main():
    n = int(input("Enter an odd number: "))

    if n <= 0 or n % 2 == 0:
        print("Please enter a positive odd number.")
        return

    print_hollow_diamond(n)


if __name__ == "__main__":
    main()
