# Standard library imports
import math

# Third party imports
import matplotlib.pyplot as plt


class Vector:
    """Defines a vector of arbitrary dimensions"""

    def __init__(self, dimensions: tuple):
        """Object initializer"""

        self.dimensions: tuple = dimensions
        _index: int = 0

    def __add__(self, v):
        """Provides for addition operator."""

        if len(self.dimensions) != len(v.dimensions):
            error_message = "Dimensions must be equal in number."
            raise ValueError(error_message)

        sums = [
                self.dimensions[index] + v.dimensions[index]
                for index
                in range(len(self.dimensions))
        ]
        return Vector(sums)

    def __iter__(self):
        """Provides for iterator"""

        return self

    def __next__(self):
        """Provides for looping through iterator"""

        if self._index < len(self.dimensions):
            self._index += 1
            return self.dimensions[self._index - 1]
        else:
            self._index = 0
            raise StopIteration

    def __sub__(self, v):
        """Provides for subtraction operator"""

        if len(self.dimensions) != len(v.dimensions):
            error_message = "Dimensions must be equal in number."
            raise ValueError(error_message)

        differences = [
            self.dimensions[index] - v.dimensions[index]
            for index
            in range(len(self.dimensions))
        ]
        return Vector(differences)

    def __repr__(self):
        """Return official str representation of object."""

        return f"Vector(dimensions({self.dimensions[0]}, {self.dimensions[1]})"

    def draw_arrow(self, ax: plt.Axes, color: str) -> None:
        """Draw the Vector as an arrow on the given Axes."""

        ax.arrow(
            0,
            0,
            self.dimensions[0],
            self.dimensions[1],
            length_includes_head=True,
            head_width=0.03,
            color=color,
        )

    def draw_point(self, ax: plt.Axes, color: str) -> None:
        """Draw the Vector as a point on the given Axes."""

        ax.scatter(self.dimensions[0], self.dimensions[1], color=color)

    def length(self) -> float:
        """Calculates length of Vector"""

        return math.sqrt(self.dimensions[0]**2 + self.dimensions[1]**2)


class Polygon:
    """Defines a polygon as a set of Vector objects."""

    def __init__(self, vectors: list[Vector]):
        """Object initializer"""

        self.vectors = vectors

    def __add__(self, v: Vector):
        """Provides for object addition operator"""

        return Polygon([vector + v for vector in self.vectors])

    def __repr__(self):
        """Official str representation of polygon object"""

        return f"Polygon(vectors={self.vectors})"

    def __sub__(self, v: Vector):
        """Provides for object subtraction"""

        return Polygon([vector - v for vector in self.vectors])

    def draw(self, ax: plt.Axes, color: str):
        """Draw polygone on given Axes."""

        vectors = self.vectors
        vectors.append(vectors[0])

        for index in range(len(vectors) - 1):

            ax.plot(
                (vectors[index].dimensions[0], vectors[index+1].dimensions[0]),
                (vectors[index].dimensions[1], vectors[index+1].dimensions[1]),
                color=color,
            )


def main():
    """Sample code to test object functionality."""

    pass


if __name__ == "__main__": main()
