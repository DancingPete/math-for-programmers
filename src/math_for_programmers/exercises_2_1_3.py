"""Exercises from section 2.1.3."""

# Third party imports
import matplotlib.pyplot as plt

# Local imports
from math_for_programmers.chapter2_2d_vectors import (Polygon, Vector)


def ex_2_1() -> str:
    """Exercise 2.1

    What are the x- and y-coordinates of the point at the tip of the dinosaur's toe?
    """

    return (
        "\nExercise 2.1\n"
        "What are the x- and y-coordinates of the point at the tip of the dinosaur's toe?\n"
        f"Answer: {(-1, -4)}"
    )


def ex2_2(ax: plt.Axes) -> None:
    """Exercise 2.2

    Draw the point in the plane and the arrow corresponding to the point (2, -2).
    """

    vector = Vector((2, -2))
    vector.draw_point(ax, "orange")
    vector.draw_arrow(ax, "blue")


def ex2_3() -> list[tuple]:
    """Exercise 2.3

    By looking at the locations of the dinosaur's points, infer the
    remaining vectors not included in the dino_vectors list.
    For instance, I already included (6, 4), which is the tip of the dinoaur's
    tail, but I didn't include theh point (-5, -3), which is a point on the dinosaur's
    nose.
    When you're done, dino_vectors should be a list of 21 vectors represented as
    coordinate pairs.
    """

    return [
        (6,4), (5,1), (1,-2), (2,-3), (1,-4), (-1,-4), (0,-3), (-1,0), (-2,1), (-4,0),
        (-5,1), (-2,2), (-5,2), (-5,3), (-4, 4), (-3, 4), (-2,5), (-1,5), (1,2), (3,1)
    ]


def ex2_4(ax: plt.Axes, vectors: list[Vector], color: str) -> None:
    """Exercise 2.4

    Draw the dinosaur with the dots connected by constructing a
    Polygon object with the dino_vectors as its vertices.
    """

    polygon = Polygon(vectors)
    polygon.draw(ax, color)


def ex2_5(ax: plt.Axes, color: str) -> None:
    """Exercise 2.5

    Draw the vectors (x, x**2) for x in the range from x=-10 to
    x=11 as points.
    """

    xx = range(-10, 11)
    yy = [x**2 for x in xx]
    ax.scatter(xx, yy, color=color)


def main():
    """Run each execise."""


    # 2.1
    print(ex_2_1())

    # 2.2
    fig, ax = plt.subplots()
    ax.set_title("Exercise 2.2")
    ex2_2(ax)
    plt.show()

    # 2.3
    dino_vectors = [Vector(t) for t in ex2_3()]

    # 2.4
    fig, ax = plt.subplots()
    ax.set_title("Exercise 2.4")
    ex2_4(ax, dino_vectors, "red")
    plt.show()

    # 2.5
    fig, ax = plt.subplots()
    ax.set_title("Exercise 2.5")
    ex2_5(ax, "blue")
    plt.show()

if __name__ == "__main__": main()
