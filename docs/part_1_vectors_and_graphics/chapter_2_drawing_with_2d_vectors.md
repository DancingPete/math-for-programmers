# Chapter 2 - Drawing with 2D Vectors

In data science, its common for data sets to have many, many dimensions. Grappling with
these problems in graphics, physics, and data analysis requires a framework for dealing
with higher dimensions. This framework is vector mathematics. (22)

> **Vector mathematics**: Framework for dealing with data in higher dimensions (22)

Vectors are the objects belonging to the multi-dimensional spaces of vector mathematics.

> **Vectors**: Objects belonging to multi-dimensional spaces, having their own notion of
arithmetic (22)

## 2.1 Picturing 2D Spaces

> **Two-dimensional vector**: Point on a plane relative to an origin. (23)

## 2.2 Plane Vector Arithmetic

Operations from vector arithmetic all accomplish useful geometric transformations,
not just algebraic ones. (32)

Vector addition is simple to calculate: given two input vectors, you add their
x-coordinates to get the resulting x-coordinate and then you add their y-coordinates
to get the resulting y-coordinate. (32)

> **Vector addition**: Vector operation taking two vectors as its operands and resulting
in a third vector which is the respective sum of its x-coordinates and its y-coordinates.

The rule for vector addition is sometimes called *tip-to-tail* addition, because
if you move the tail of the second arrow to the tip of the first without changing
its direction, you get the sum as the arrow from the start of the first to the
end of the second. (33)

Sometimes it's useful to take a vector we already have and decompose it as a some of
smaller vectors. (35)
Similarly, it can be useful to think of vectors as a sum of a vector pointing in the x
direction and a vector pointing in the y direction.

```python
Vector(1, 4) = Vector(1, 0) + Vector(0, 4)
```

These two vectors `(Vector(1, 0), Vector(0,4)` are called the x and y components

> **x and y components**: Vectors whose sum is another Vector and whose y and
x elements are 0, respectively.

The length of the vector is the length of the arrow that represents it, or
equivalently, it is the distance from the origin to the point that represents it. (36)

> **length**: Distance between the origin and the point representing a vector

Repeated addition of vectors is unambiguous; you can keep stacking arrows
tip-to-tail as long as you want. (37)

If v were a number, and we wanted to sum $v+v+v+v+v$ we would simply write $5 \cdot v$.
It is possible to do the same with vectors. (37)

The operation of multiplying a vector by a number is called scalar multiplication.
When working with vectors, ordinary numbers are called scalars. (38)

> **Scalar multiplication**: Multiplying each dimension of a vector by a scalar value

> **Scalar**: An ordinary number

Computationally, we execute any scalar multiplcation on a vector by multiplying each
coordinate of the vector by the scalar. (38)

$\text{Where } v = Vector(6, 4),$

$$
1.5 \cdot v = Vector(9, 6)
$$

Given $v$, the opposite vector, $-v$, is the same as the scalar multiple $-1 \cdot v$

> **Opposite vector**: $-1 \cdot Vector$

Having a notion of negating a vector, we can define vector subtraction.
For numbers, $x - y$ is equivalent to $x + (-y)$.
We set the same convention for vectors.

> **Vector subtraction**: $Vector1 - Vector2 = Vector1 + (-1 \cdot Vector2)$

The difference between two vectors is the vector that must be travelled to go from
the tip of the second operand to the tip of the first. (40)
This is called displacement.

> **Displacement**: Vector to travel to go from the tip of the second operand of
a vector subtraction to the tip of the first operand.

Distance on the other hand, it the length of that vector.
While displacement if a vector, distance is a scalar. (41)

## 2.3 Angles and Trigonometry in the Plane

## 2.4 Transforming Collections of Vectors

## 2.5 Drawing with Matplotlib
