import random
import string
from dataclasses import dataclass, field
# https://docs.python.org/ko/3/library/dataclasses.html


def generate_id() -> str:
    return ''.join(random.choices(string.ascii_lowercase, k=15))


def generate_login(name: str, surname: str) -> str:
    return name[0] + surname


@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        self.login = generate_login(self.name, self.surname)
