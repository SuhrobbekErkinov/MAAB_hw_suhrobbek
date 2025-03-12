import math

class Vector:
    def __init__(self, *args):
        self.args = tuple(args)

    def __str__(self):
        return f"Vector{self.args}"

    def __add__(self, other):
        if not isinstance(other, Vector) or len(self.args) != len(other.args):
            raise ValueError("Either vectors don't have the same length or other is not Vector type!")
        return Vector(*(a + b for a, b in zip(self.args, other.args)))

    def __sub__(self, other):
        if not isinstance(other, Vector) or len(self.args) != len(other.args):
            raise ValueError("Either vectors don't have the same length or other is not Vectory type!")
        return Vector(*(a - b for a, b in zip(self.args, other.args)))

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*(a * other for a in self.args))
        elif isinstance(other, Vector):
            if len(other.args) != len(self.args):
                raise ValueError("Vectors don't have the same length. Operation can't be done.")
            return sum(a * b for a, b in zip(self.args, other.args))
        else:
            raise TypeError("Only dot and scalar products are supported.")

    def magnitude(self):
        return math.sqrt(sum(a**2 for a in self.args))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ZeroDivisionError("0 vector cannot be normalized")
        return Vector(*(a/mag for a in self.args))

if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    print(v1)
    v2 = v1 * 4
    print(v2)
    v3 = v1 * v2
    print(v3)
    v5 = v1 - v2
    print(v5)
    print(v2.magnitude())
    v4 = v1.normalize()
    print(v4)