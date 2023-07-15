from Model import mongo_database


class Handler_response:


    def get_planets_from_system(self, name_system: str = "Solar"):

        collection = mongo_database.MongoDatabase("Universe_objects")
        planets = collection.get_object_from_star_system(name_system)

        return [{"planet name": planet["name"], "planet_type:": planet["type"]} for planet in planets]


    def get_stars_systems(self):

        collection = mongo_database.MongoDatabase("Star_systems")
        stars_systems = collection.get_stars_system()
        return [{"name star system": stars_systems["name"],
                 "age:": stars_systems["age"],
                 "mass center": stars_systems["mass_center"]
                 } for stars_systems in stars_systems]

