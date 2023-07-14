from fastapi import FastAPI
from Model import mongo_database
from Controller import output

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

if __name__ == "__main__":
    main()
