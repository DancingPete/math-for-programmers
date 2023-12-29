"""Exercises from section 2.2.4."""

# Standard library import
from functools import reduce

# Third party imports
import matplotlib.pyplot as plt

# Local imports
from math_for_programmers.chapter2_2d_vectors import (Polygon, Vector)
from math_for_programmers.exercises_2_1_3 import ex2_3


def ex2_6() -> str:
    """Exercise 2.6

    If the vector u = (-2, 0), the vector v = (1.5, 1.5), and the vector
    w = (4, 1),

        - what are the results of u + v, v + w, and u + w?
        - what is the result of u + v + w
    """

    u = Vector(dimensions=(-2, 0))
    v = Vector(dimensions=(1.5, 1.5))
    w = Vector(dimensions=(4, 1))

    uv = u + v
    vw = v + w
    uw = u + w
    uvw = u + v + w

    return (
        "\nExercise 2.6\n"
        "The resultant sums are as follows:\n"
        f"\tu + v = {uv}\n"
        f"\tv + w = {vw}\n"
        f"\tu + w = {uw}\n"
        f"\tu + v + w = {uvw}\n"
    )


def ex2_7() -> str:
    """Exercise 2.7

    You can add any number of vectors together by summing all of their
    x-coordinates and all of the y-coordinates.
    For instance, the fourfold sum (1,2) + (2,4) + (3,6) + (4,8)
    has x-coordinate 1+2+3+4 = 10 and y component 2+4+6+8 = 20,
    making the result (10, 20).
    Implement a revised add function that takes any number of vector
    arguments.
    """

    def add(vectors: list[Vector]) -> Vector:

        return reduce(lambda x, y: x + y, vectors)

    vectors = [
        Vector(dimensions=(1,2)),
        Vector(dimensions=(2,4)),
        Vector(dimensions=(3,6)),
        Vector(dimensions=(4,8)),
    ]

    return (
        "\nExercise 2.7\n"
        f"The resultant sum of {vectors} is: {add(vectors)}\n"
    )


def ex2_8() -> str:
    """Exercise 2.8

    Write a function translate(tranlation, vectors) that takes a
    translation vector and a list of input vectors, and returns a list
    of the input vectors all traslated by the translation vector.

    For instance, translate((1,1), [(0,0), (0,1), (-3, -3)]) should
    return [(1,1), (1,2), (-2,-2)]
    """

    vector = Vector(dimensions=(1, 1))
    vectors = [
        Vector(dimensions=(0,0)),
        Vector(dimensions=(0,1)),
        Vector(dimensions=(-3,-3)),
    ]

    def translate(vector: Vector, vectors: list[Vector]) -> list[Vector]:

        return [vector +  v for v in vectors]

    return (
        "\nExercise 2.8\n"
        f"The transformation of each vector in {vectors} by {vector} is: "
        f"{translate(vector, vectors)}"
    )


def ex2_9(axs: list[list[plt.Axes]]) -> str:
    """Exercise 2.9

    Any sum of vectors v + w gives the same result as w + v.

    Explain why this is true useing the definition of the vector
    sum on coordinates.

    Also, draw a picture to show why it is true geometrically.
    """

    v = Vector(dimensions=(1, 1))
    w = Vector(dimensions=(-1, 2))
    vw = v + w
    wv = w + v

    axs["left"].set_title("v+w")
    axs["right"].set_title("w+v")

    v.draw_arrow(axs["left"], color="orange")
    v.draw_arrow(axs["right"], color="orange")
    w.draw_arrow(axs["left"], color="blue")
    w.draw_arrow(axs["right"], color="blue")
    vw.draw_arrow(axs["left"], color="green")
    wv.draw_arrow(axs["right"], color="green")

    return (
        "\nExercise 2.9\n"
        "Vector addition is commutative because vector addition "
        "it simply a the performance of a set of scalar additions "
        "of vector elements to each other, which is itself a "
        "commutative operation."
    )


def ex2_10() -> None:
    """Exercise 2.10

    Among the following three arrow vectors (labelled u, v, w),
        - which pair has the sum that gives the longest arrow?
        - which pair sums to give the shortest arrow?
    """

    pass


def ex2_11(ax: plt.Axes) -> None:
    """Exercise 2.11

    Write a function using vector addition to show 100 simltaneous and non-overlapping copies
    of the dinosaur.
    This show the power of computer graphics; imagine how tedious it would be to specify all
    2,100 coordinate pairs by hand!
    """

    vectors = [Vector(dimensions=v) for v in ex2_3()]
    dino = Polygon(vectors)

    for x in range(10):

        for y in range(10):

            transformed_dino = dino + Vector(dimensions=(x*12, y*10))
            transformed_dino.draw(ax, color="green")


def main():
    """Run each execise."""

    print(ex2_6())
    print(ex2_7())
    print(ex2_8())

    fig, axs = plt.subplot_mosaic([["left", "right"]])
    answer = ex2_9(axs)
    print(answer)
    plt.show()

    fig, ax = plt.subplots()
    answer = ex2_11(ax)
    plt.show()

if __name__ == "__main__": main()
