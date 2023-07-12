from Model.mongo_database import MongoDatabase


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
        if name == "":
            self._name = "Unknown"
            return True
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
    def __init__(self, diameter=0, weight=0, id_star_system="Unknown"):
        super().__init__()
        self._id_star_system = None
        self._weight = None
        self._type_object = None
        self._diameter = None

    def set_type_object(self):
        """Choose from [star, blackhole, blue gigant]"""
        TYPES_OBJECTS = ("Unknown", "Star", "Worm Hole", "Blue Gigant", "Red Gigant")

        print(f"What type?[0-{len(TYPES_OBJECTS)-1}]")
        n = 0
        for each in TYPES_OBJECTS:
            print(f"{n}:{each}")
            n += 1
        try:
            choose = int(input())
            if choose == 0:
                self._type_object = choose
                return True
            self._type_object = TYPES_OBJECTS[choose]
            return True
        except (TypeError, IndexError, ValueError):
            return False


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
        print(f"Which is '{self.get_name()}' system in?:")
        print("Unknown")
        star_systems = MongoDatabase("Star_systems").get()
        for each in star_systems:
            print(f"{each['name']}")
        universe_name = MongoDatabase("Star_systems").get(input())["name"]
        self._id_star_system = universe_name
        return universe_name

    def get_star_system_id(self):
        return self._id_star_system


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


    def choose_type_universe_object(self):
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

if  __name__ == "__main__":
    main()


