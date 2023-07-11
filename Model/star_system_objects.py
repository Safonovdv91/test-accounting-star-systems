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
    def __init__(self, type_object="Unknown", diametr=0, weight=0, id_star_system="Unknown"):
        super().__init__()
        self._is_star_system = None
        self._weight = None
        self._type_object = None
        self._diameter = None
        self.set_type_object(type_object)
        self.set_diameter(diametr)
        self.set_weight(weight)
        self.set_star_system_id(id_star_system)

    def set_type_object(self, choose):
        """Choose from [star, blackhole, blue gigant]"""
        if choose == "Unknown":
            self._type_object = choose
            return True
        type_objects = ["1 - Star", "2 - Worm Hole", "3 - Blue Gigant", "4 - Red Gigant"]
        try:
            choose = int(choose)
            self._type_object = type_objects[choose-1]
        except TypeError:
            return False
        except IndexError:
            return False
        return True

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

    def set_star_system_id(self, id_star_system):
        self._is_star_system = id_star_system
        """ пока не известно, будет выпадать список из существующих систем"""

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

class Creator:
    def create_new_star_system(self):
        new_star_system = Star_System()
        print("What the system name?")
        print("name:", end="")
        while not new_star_system.set_name(input()):
            print("Print plz correct name")
        print("What the system age?")
        print("Age: ", end="")
        while not new_star_system.set_age(input()):
            print("Type correct age: ", end="")
        print(f"Do {new_star_system.get_name()} have mass center?")
        if input().upper() == "YES" or input().upper() == "Y":
            print("What is object is centr?")
            # тут вывести планеты которые принаджжат этой системы
        else:
            print("Ok, system doesn't have mass center.")
        print("Adding to db")
        server = MongoDatabase("Star_systems")
        server.add(new_star_system)
        server.close()
        print("Adding success")

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
        print(Creator().create_new_star_system())
        print("Information add")

    types_universe_obj = ["Star", "Black Hole", "Planet", "Satellite"]

if  __name__ == "__main__":
    main()


