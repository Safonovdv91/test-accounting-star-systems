from pymongo import MongoClient
# from star_system_objects import *


class MongoDatabase:

    def __init__(self, collection_name: str):
        self.connection = MongoClient("172.17.0.2", 27017)
        self._collection_name = collection_name
        self.universe = self.connection["Universe"]

    def close(self):
        self.connection.close()

    def add(self, obj):
        collection = self.universe[self._collection_name]
        collection.insert_one({
            "name": obj.get_name(),
            "age": obj.get_age(),
            "mass_center": "unknown"
        })

    def add_universe_object(self, obj):
        collection = self.universe[self._collection_name]

        collection.insert_one({
            "name": obj.get_name(),
            "type": obj.get_type_object(),
            "age": obj.get_age(),
            "weight": obj.get_weight(),
            "diameter": obj.get_diameter(),
            "star_system": obj.get_star_system_id()
        })

    def get(self, name="Any"):
        if name == "Any":
            return self.universe[self._collection_name].find()
        collection = self.universe[self._collection_name]
        return collection.find_one({"name": name})

    def update(self, obj):
        pass

    def remove(self, obj):
        pass


def main():
    db = MongoDatabase("Star_systems")
    db = MongoDatabase
    s = db.get("Solar 2")
    print(f"{s['name']} system, Age is {s['age']}, mass center {s['mass_center']}")
    db.close()


if __name__ == "__main__":
    main()
