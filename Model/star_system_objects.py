
class Universe_object:
    """
    Общие свойства космического объекта :
    атрибуты:
        имя
        возраст

    методы:
        добавлять
        удалять
        редактировать

    """
    def __init__(self, name="Unknown", age=0):
        self._age = None
        self._name = None
        self.set_name(name)
        self.set_age(age)

    def set_name(self, name):
        if type(name) is str:
            self._name = name
            return True
        return False

    def get_name(self):
        return self._name

    def set_age(self, age):
        try:
            age = float(age)
        except ValueError:
            return False
        if age < 0:
            return False
        self._age = age
        return True

    def get_age(self):
        return self._age


class CelestialBody(Universe_object):
    """ атрибуты:имя, тип, возраст, диаметр, масса
    методы:
        добавлять, удалять, редактировать"""
    def __init__(self, type_object: str, name: str, age: float, diameter: float, star_system):
        super().__init__(name, age)
        self.type_object = type_object
        self.diameter = diameter
        self.star_system_id = star_system

class Star_System(Universe_object):
    """
    Звездная система
    атрибуты:
        имя
        возраст
        центр масс: объект(типа звезда, или черная дыра
    методы:
        добавлять
        удалять
        редактировать

        добалять космический объект
        делать космический объект центром масс

    """
    def __init__(self, name="Unknown", age=0, mass_center=None):
        super().__init__(name, age)
        self.set_mass_center(mass_center)

    def set_mass_center(self, mass_center):
        self._mass_center = mass_center

    def get_mass_center(self):
        return self._mass_center

    def create_new(self):
        new_star_system = Star_System()
        print("What the system name?")
        print("name:", end="")
        while not new_star_system.set_name(input()):
            print("Print plz correct name")
        print("What the system age?")
        print("Age: ", end="")
        while not new_star_system.set_age(input()):
            print("Type correct age: ", end="")
        return new_star_system


def main():
    print("What do u want:")
    print("1 - Create star system , 2 - Create any")
    if input() == "1":
        print(Star_System().create_new())


    types_universe_obj = ["Star", "Black Hole", "Planet", "Satellite"]

if  __name__ == "__main__":
    main()


