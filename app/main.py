from __future__ import annotations
import math


class Vector:

    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
        cls, start: tuple[float, float], end: tuple[float, float]
    ) -> Vector:

        return cls(end[0] - start[0], end[1] - start[1])

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        comprimento = self.get_length()

        if comprimento == 0:
            raise ValueError("Não é possível normalizar um vetor nulo.")

        return Vector(self.x / comprimento, self.y / comprimento)

    def angle_between(self, vector: "Vector") -> int:
        cos_a = (self * vector) / (self.get_length() * vector.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: float) -> "Vector":
        radians = math.radians(degrees)

        x = self.x * math.cos(radians) - self.y * math.sin(radians)
        y = self.x * math.sin(radians) + self.y * math.cos(radians)

        return Vector(x, y)
