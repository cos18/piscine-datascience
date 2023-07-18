from S1E9 import Character


class Baratheon(Character):
    """Baratheon class

    Attributes:
        first_name (str): name of object
        is_alive (bool): boolean that object is alive
        family_name (str): 'Baratheon' fixed value
        eyes (str): 'brown' fixed value
        hairs (str): 'dark' fixed value
    """

    def __init__(self, first_name: str, is_alive=True) -> None:
        """Baratheon init function

        Args:
            first_name (str): first_name
            is_alive (bool, optional): is_alive. Defaults to True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self) -> str:
        """Baratheon __str__ function

        Returns:
            str: representative string value
        """
        return f' Vector: ({self.family_name}, {self.eyes}, {self.hairs})'

    def __repr__(self) -> str:
        """Baratheon __repr__ function

        Returns:
            str: representative string value
        """
        return self.__str__()

    def die(self) -> None:
        """die function implement
        """
        self.is_alive = False


class Lannister(Character):
    """Lannister class

    Attributes:
        first_name (str): name of object
        is_alive (bool): boolean that object is alive
        family_name (str): 'Lannister' fixed value
        eyes (str): 'blue' fixed value
        hairs (str): 'light' fixed value
    """

    def __init__(self, first_name: str, is_alive=True) -> None:
        """Lannister init function

        Args:
            first_name (str): first_name
            is_alive (bool, optional): is_alive. Defaults to True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def __str__(self) -> str:
        """Lannister __str__ function

        Returns:
            str: representative string value
        """
        return f' Vector: ({self.family_name}, {self.eyes}, {self.hairs})'

    def __repr__(self) -> str:
        """Lannister __repr__ function

        Returns:
            str: representative string value
        """
        return self.__str__()

    def die(self) -> None:
        """die function implement
        """
        self.is_alive = False

    # @classmethod vs @staticmethod : https://wikidocs.net/16074

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool):
        """Create Lannister without __init__

        Args:
            first_name (str): name
            is_alive (bool): alive boolean

        Returns:
            Lannister: New Object
        """
        return cls(first_name, is_alive)
