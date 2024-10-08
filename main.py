from fastapi import FastAPI
from routes.entry import entry_root
from routes.data import data_root

app = FastAPI()


app.include_router(entry_root)
app.include_router(data_root)