class calculator:
    """Calculator class

    Attributes:
        vec (list of number): number vector
    """

    def __init__(self, vec: list):
        """Init calculator class

        Args:
            vec (list): using vector
        """
        self.vec = vec

    def __add__(self, object: float) -> None:
        """Addition inner function

        Args:
            object (float): scalar that add
        """
        self.vec = list(map(lambda v: v + object, self.vec))
        print(self.vec)

    def __mul__(self, object: float) -> None:
        """Multiply inner function

        Args:
            object (float): scalar that mul
        """
        self.vec = list(map(lambda v: v * object, self.vec))
        print(self.vec)

    def __sub__(self, object: float) -> None:
        """Subtraction inner function

        Args:
            object (float): scalar that sub
        """
        self.vec = list(map(lambda v: v - object, self.vec))
        print(self.vec)

    def __truediv__(self, object: float) -> None:
        """Division inner function

        Args:
            object (float): scalar that div
        """
        if object == 0:
            raise ValueError('Cannot divided by zero')
        self.vec = list(map(lambda v: v / object, self.vec))
        print(self.vec)
