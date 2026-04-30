"""Backend main entry point"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Read the root endpoint."""
    return {"Hello": "World"}
