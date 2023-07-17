from pymongo import MongoClient


# from star_system_objects import *


class MongoDatabase:

    def __init__(self, collection_name: str):
        self.connection = MongoClient("172.17.0.2", 27017)
        self._collection_name = collection_name
        self.universe = self.connection["Universe"]

    def close(self):
        self.connection.close()

    def add_star_system(self, obj):
        collection = self.universe[self._collection_name]
        collection.insert_one({
            "name": obj.name,
            "age": obj.age,
            "mass_center": "unknown"
        })

    def add_universe_object(self, obj):
        collection = self.universe[self._collection_name]

        collection.insert_one({
            "name": obj.name,
            "type": obj.get_type_object(),
            "age": obj.age,
            "weight": obj.get_weight(),
            "diameter": obj.get_diameter(),
            "star_system": obj.get_star_system_id()
        })

    def get_object_from_star_system(self, name_star_system: str):
        """ Принимает название звездной системы и выдает объекты(планеты) которые в ней.
        """
        collection = self.universe[self._collection_name]
        return collection.find({"star_system": name_star_system})

    def get_stars_system(self):
        """ Возвращает все известные звездные системы системы.
        """
        collection = self.universe[self._collection_name]
        return collection.find({})

    def get(self, name="Any"):
        if name == "Any":
            return self.universe[self._collection_name].find()
        try:
            collection = self.universe[self._collection_name]
        except TypeError:
            return False
        return collection.find_one({"name": name})

    def update(self, obj):
        pass

    def remove(self, obj):
        pass


class DBStarsSystems(MongoDatabase):
    def __init__(self):
        super().__init__("Star_systems")

    def add(self, name, age):
        collection = self.universe[self._collection_name]
        collection.insert_one({
            "name": name,
            "age": age,
            "mass_center": "unknown"
        })


class DB_Univers_Objects(MongoDatabase):
    def __init__(self):
        super().__init__("Univers_objects")


def main():
    test_db = MongoDatabase("Universe_objects")
    coll = []
    type_mass_center = {"Star", "Worm Hole"}
    for each in test_db.get_object_from_star_system("Solar"):
        if each["type"] in type_mass_center:
            coll.append(each["name"])

    return {"mess": coll}
    pass


if __name__ == "__main__":
    main()
