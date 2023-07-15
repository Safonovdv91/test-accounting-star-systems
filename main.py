from fastapi import FastAPI
from Model import mongo_database
from Controller import output
from Controller import input

app = FastAPI()


@app.get("/")
def main():
    return mongo_database.main()


@app.get("/stars_system/{name_star_system}")
def stars_system(name_star_system: str):
    return output.Handler_response().get_planets_from_system(name_star_system)


@app.get("/stars_system/")
def stars_system():
    return output.Handler_response().get_stars_systems()

@app.post("/stars_system/add/{name_stars_system}")
def add_system(name_stars_system: str, age: int):
    return input.Input_handler().add_new_stars_system(name_stars_system, age)


if __name__ == "__main__":
    main()
