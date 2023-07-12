from Model.mongo_database import MongoDatabase
from Model.star_system_objects import Star_System, CelestialBody
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
        center_mass = input().upper()
        if center_mass == "YES" or center_mass == "Y":
            print("What is object is centr?")
            # тут вывести планеты которые принаджжат этой системы
        else:
            print("Ok, system doesn't have mass center.")
        print("Adding to db")
        server = MongoDatabase("Star_systems")
        server.add(new_star_system)
        server.close()
        print("Adding success")

    def create_new_universe_object(self):
        new_universe_obj = CelestialBody()
        print("What the object name?")
        print("name: ", end="")
        while not new_universe_obj.set_name(input()):
            print("Type plz correct name: ", end="")
        print("What the age?")
        print("Age: ", end="")
        while not new_universe_obj.set_age(input()):
            print("Type correct age: ", end="")

        print(f"Which is '{new_universe_obj.get_name()}' system in?:")
        print("0 - if unknown")
        star_systems = MongoDatabase("Star_systems").get()
        n = 1
        for each in star_systems:
            print(f"{n}: - {each['name']}")
            n += 1
        choose = input()
        universe_id = MongoDatabase("Star_systems").get(choose)["_id"]

        print(universe_id)

        new_universe_obj.set_star_system_id(universe_id)
        print("Adding to db")
        print()
        print(new_universe_obj.get_type_object())
        print(new_universe_obj.get_star_system_id())
        print(new_universe_obj.get_diameter())
        print(new_universe_obj.get_weight())
        print(new_universe_obj.get_age())
        print(new_universe_obj.get_name())

        server = MongoDatabase("Universe_objects")
        server.add_universe_object(new_universe_obj)
        server.close()
        print("Adding success")

if __name__ == "__main__":

    Creator().create_new_universe_object()
