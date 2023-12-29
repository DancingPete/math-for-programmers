# Standard library imports
import math as m

# Local imports
from math_for_programmers.2_drawing_with_2d_vectors import Vector

def ex_2_27():
    """Exercise 2.27
    Confirm that the vector given by Cartesian coordinates (-1.34, 2.68) has
    a length of approximately 3 as expected.
    """

    length = Vector(-1.34, 2.68)
    return (
        "Exercise 2.27\n"
        f"length: {length}"
    )


def main():
    """Run each execise."""

    print(ex_2_27())

if __name__ == "__main__": main()
