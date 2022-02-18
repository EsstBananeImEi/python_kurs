from dataclasses import dataclass, field


@dataclass(order=True, frozen=True)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    age: int
    job: str
    strength: int = 100

    def __post_init__(self):
        object.__setattr__(self, 'sort_index', self.strength)

    def __str__(self):
        return f"{self.name}, {self.age}, {self.job}"


if __name__ == '__main__':
    person1 = Person("Peter", 30, "Handwerker", 50)
    person2 = Person("Vanessa", 25, "Managerin")
    person3 = Person("Vanessa", 25, "Managerin")

    print(id(person2))
    print(id(person3))
    print(person1)
    print(person1 > person2)
