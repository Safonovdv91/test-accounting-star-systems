from Model.mongo_database import MongoDatabase
from Model.star_system_objects import StarSystem, CelestialBody


def create_new_star_system():
    new_star_system = StarSystem()
    print("What the system name?")
    print("name:", end="")
    while not new_star_system.set_name(input()):
        print("Print plz correct name")
    print("What the system age?")
    print("Age: ", end="")
    while not new_star_system.set_age(input()):
        print("Type correct age: ", end="")


    MongoDatabase("Star_systems").add_star_system(new_star_system)
    print("Adding success")


def create_new_universe_object():
    """ Создание новго небесного объекта"""

    new_universe_obj = CelestialBody()
    print("You adding new universe object")
    while not new_universe_obj.set_type_object():
        print("Try again")
    print("What the object name?")

    print("name: ", end="")
    while not new_universe_obj.set_name(input()):
        print("Type plz correct name: ", end="")

    print("What the age?")
    print("Age: ", end="")
    while not new_universe_obj.set_age(input()):
        print("Type correct age: ", end="")

    new_universe_obj.set_star_system_name()

    server = MongoDatabase("Universe_objects")
    server.add_universe_object(new_universe_obj)
    server.close()
    print("Adding success")

def create_mass_center():
    """Функция определения центра масс звездной системы из объектов которые
    находятся в ней """
    pass

class Creator:
    pass

if __name__ == "__main__":
    while True:
        create_new_star_system()
        create_new_universe_object()