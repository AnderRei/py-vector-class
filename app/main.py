from __future__ import annotations

class Vector:

    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            self.x  * other,
            self.y * other
        )

    @classmethod
    def create_vector_by_two_points(
        cls, start: tuple[float, float], end: tuple[float, float]
        ) -> Vector:
        
        return cls(
            end[0] - start[0],
            end[1] - start[1]
        )
    