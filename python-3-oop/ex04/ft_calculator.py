class calculator:
    """calculator class
    """
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Dot product

        Args:
            V1 (list[float]): vector
            V2 (list[float]): vector
        """
        # Can be use reduce function
        result = 0
        for idx, val in enumerate(V1):
            result += (val * V2[idx])
        print(f'Dot product is: {result}')

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add vector

        Args:
            V1 (list[float]): vector
            V2 (list[float]): vector
        """
        result = []
        for idx in range(len(V1)):
            result.append(V1[idx] + V2[idx])
        print(f'Add Vector is : {result}')

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtract vector

        Args:
            V1 (list[float]): vector
            V2 (list[float]): vector
        """
        result = []
        for idx in range(len(V1)):
            result.append(V1[idx] - V2[idx])
        print(f'Sous Vector is : {result}')
