from abc import ABC, abstractmethod


class Character(ABC):
    """Character Abstract class

    Attributes:
        first_name (str): name of object
        is_alive (bool): boolean that object is alive
    """

    @abstractmethod
    def __init__(self, first_name: str, is_alive=True) -> None:
        """Character init function

        Args:
            first_name (str): first_name
            is_alive (bool, optional): is_alive. Defaults to True.
        """

        # 생성자를 통해 초기화한 값들이 __dict__에 들어간다
        super().__init__()
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self) -> None:
        """die abstract function
        """
        pass


class Stark(Character):
    """Stark Abstract class

    Attributes:
        first_name (str): name of object
        is_alive (bool): boolean that object is alive
    """

    def __init__(self, first_name: str, is_alive=True) -> None:
        """Stark init function

        Args:
            first_name (str): first_name
            is_alive (bool, optional): is_alive. Defaults to True.
        """
        super().__init__(first_name, is_alive)

    def die(self) -> None:
        """die function implement
        """
        self.is_alive = False
