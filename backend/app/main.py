from fastapi import FastAPI


app = FastAPI(
    title="African Real Estate - FastAPI",
    description="Fully features real estate API built using FastAPI",
)


@app.get("/")
def home():
    return {"message": "Welcome to the ARE real estate API"}
