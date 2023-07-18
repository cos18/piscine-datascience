from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King class that inherit Baratheon and Lannister

    Attributes:
        first_name (str): name of object
        is_alive (bool): boolean that object is alive
        family_name (str): 'Baratheon' fixed value
        eyes (str): 'brown' fixed value
        hairs (str): 'dark' fixed value
    """
    def set_eyes(self, eyes: str) -> None:
        """Set King's eye

        Args:
            eyes (str): new eyes string
        """
        self.eyes = eyes

    def set_hairs(self, hairs: str) -> None:
        """Set King's hair

        Args:
            hairs (str): new hairs string
        """
        self.hairs = hairs

    def get_eyes(self) -> str:
        """get King's eye

        Returns:
            str: eye value
        """
        return self.eyes

    def get_hairs(self) -> str:
        """get King's hair

        Returns:
            str: hair value
        """
        return self.hairs
