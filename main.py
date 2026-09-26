from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.get("/greet")
async def greet_name(name: str | None = "User", age: int = 0) -> dict:
    return {"message": f"Hello {name}", "age": age}
