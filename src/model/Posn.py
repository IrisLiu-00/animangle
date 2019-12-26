class Posn:
    """A location on a 2D plane, represented by an x and y coordinate.

    Attributes:
        x (int): x coordinate
        y (int): y coordinate
    """

    # immutable, public

    def __init__(self, x: int, y: int):
        """Creates a position having the given x and y coordinate"""
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Posn) and other.x == self.x and other.y == self.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Posn({self.x}, {self.y})"
