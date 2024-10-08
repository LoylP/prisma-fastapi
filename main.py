from fastapi import FastAPI
from routes.entry import entry_root
from routes.data import data_root
import uvicorn

app = FastAPI()

app.include_router(entry_root)
app.include_router(data_root)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)