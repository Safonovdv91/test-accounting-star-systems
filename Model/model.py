from dataclasses import dataclass, field


@dataclass
class UniverseObject:
    name: str
    age: int | float


@dataclass()
class CelestialBody(UniverseObject):
    """ атрибуты:имя, тип, возраст, диаметр, масса
    методы:
        добавлять, удалять, редактировать
        """
    type_object: str
    diameter: int | float
    weight: int | float
    permitted_types = ("star", "blackhole", "blue", "gigant", "Unknown", "Worm Hole", "Blue Gigant")

    def validate(self):
        if not isinstance(self.name, str):
            raise ValueError("Имя должно быть строкой")
        if not isinstance(self.age, int):
            raise ValueError("Возраст должен быть целым числом")
        if self.age < 0:
            raise ValueError("Возраст должен быть неотрицательным числом")
        if self.weight < 0:
            raise ValueError("Масса должна быть положительной")
        if self.type_object not in self.permitted_types:
            raise ValueError("Объект должен быть определенного типа")

    def __post_init__(self):
        self.validate()


@dataclass()
class StarSystem(UniverseObject):
    """ атрибуты: имя, возраст, центр масс: объект(типа звезда, или черная дыра)
    методы:
        делать космический объект центром масс
    """
    center_of_mass: str = None


if __name__ == "__main__":
    body1 = CelestialBody("name 1", 23, "star", 12, 1000)

    star_system1 = StarSystem("ss1", 55)
    star_system2 = StarSystem("ss2", 55)
    star_system3 = StarSystem("ss3", 55)
    print(body1)
    print(star_system1)
    print(star_system2)
    print(star_system3)
    body2 = CelestialBody("name 2", 230, "star2", 12, 1000)
    print(body2)
