from View import terminal
from Model import mongo_database


class Checker:

    def check_name(self, name: str):
        if type(name) == str:
            return True
        else:
            return False

    def check_age(self, age: int):
        if type(age) == int:
            if age >= 0:
                return True
        return False
    def set_universe_object_type(self, type_obj: str,
                                 all_types=("Unknown", "Star", "Worm Hole", "Blue Gigant", "Red Gigant"),
                                 ):
        print(f"What type?[0-{len(type_obj) - 1}]")
        n = 0
        for each in type_obj:
            print(f"{n}:{each}")
            n += 1
        try:
            choose = int(input())
            if choose == 0:
                self._type_object = choose

                return True
            self._type_object = type_obj[choose]
            return True
        except (TypeError, IndexError, ValueError):
            return False


class Input_handler:
    def add_new_stars_system(self, name: str, age: int):
        checker = Checker()
        checker.check_name(name)
        checker.check_age(age)
        if checker.check_name(name) and checker.check_age(age):
            mongo_database.DBStarsSystems().add(name, age)
            return {"status": 200, "data": f"Add star system - '{name}' success"}
        else:
            return {"status": 200, "data": "Please send correct data"}


