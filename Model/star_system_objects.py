from Model.mongo_database import MongoDatabase


class UniverseObject:
    """ Общие свойства космического объекта :
    атрибуты:
        имя
        возраст

    методы:
        добавлять
        удалять
        редактировать

    """

    __slots__ = ("_name", "_age")

    def __init__(self, name="empty", age=1):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not value:
            raise AttributeError("Name cant be empty")
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError("Name object must be string")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value: (int, float)):
        if isinstance(value, (int, float)):
            if value < 0:
                raise AttributeError("Age must be ge(>=) than 0")
            self._age = value
        else:
            raise TypeError("Age must be int, or float")


class CelestialBody(UniverseObject):
    """ атрибуты:имя, тип, возраст, диаметр, масса
    методы:
        добавлять, удалять, редактировать
        """

    def __init__(self, diameter=0, weight=0, id_star_system="Unknown"):
        super().__init__()
        self._id_star_system = None
        self._weight = None
        self._type_object = None
        self._diameter = None

    def set_type_object(self, type_obj: str, permitted_types: set) -> bool:
        """ Choose from permitted types like: [star, blackhole, blue gigant, etc..]
        """
        if type_obj not in permitted_types:
            raise ValueError(f"type obj have to be permitted types:{permitted_types}")
        self._type_object = type_obj
        return True

    def get_type_object(self):
        return self._type_object

    def set_diameter(self, diameter=None):
        if diameter is None:
            self._diameter = diameter
            return True
        try:
            if float(diameter) >= 0:
                self._diameter = float(diameter)
                return True
        except ValueError:
            return False
        except TypeError:
            return False
        return False

    def get_diameter(self):
        return self._diameter

    def set_weight(self, weight):
        if weight is None:
            self._weight = weight
            return True
        try:
            if float(weight) >= 0:
                self._weight = float(weight)
                return True
        except ValueError:
            return False
        except TypeError:
            return False
        return False

    def get_weight(self):
        return self._weight

    def set_star_system_name(self, star_system_name=None):
        if star_system_name is not None:
            self._id_star_system = star_system_name
            return self._id_star_system
        print(f"Which is '{self.name}' system in?:")
        print("Unknown")
        star_systems = MongoDatabase("Star_systems").get()
        for each in star_systems:
            print(f"{each['name']}")
        universe_name = MongoDatabase("Star_systems").get(input())["name"]
        self._id_star_system = universe_name
        return universe_name

    def get_star_system_id(self):
        return self._id_star_system


class StarSystem(UniverseObject):
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
        self._mass_center = None
        self.set_mass_center(mass_center)

    def set_mass_center(self, mass_center):
        self._mass_center = mass_center

    def get_mass_center(self):
        return self._mass_center

    @staticmethod
    def choose_type_universe_object():
        """Choose from [star, blackhole, blue gigant, Red Gigant]"""
        type_objects = ["1 - Star", "2 - Worm Hole", "3 - Blue Gigant", "4 - Red Gigant"]
        print("Choose type of object:")
        for each in type_objects:
            print(each)
        try:
            choose = int(input())
            if 0 < choose < len(type_objects) + 1:
                return type_objects[choose]
        except TypeError:
            return False


def main():
    print("What do u want:")
    print("1 - Create star system , 2 - Create planet")
    if input() == "1":
        print("adding")
        print("Information add")

    types_universe_obj = ["Star", "Black Hole", "Planet", "Satellite"]


if __name__ == "__main__":
    main()
