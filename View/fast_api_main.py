from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def main():
    return {"Message": "Hello man"}

if __name__ == "__main__":
    main()
