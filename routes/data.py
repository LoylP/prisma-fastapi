from fastapi import APIRouter
from models.data import DataModel
from config.config import database_collection

data_root = APIRouter()

@data_root.post("/new/data")
def NewData(data: DataModel):
    data = dict(data)

    res = database_collection.insert_one(data)
    data_id = str(res.inserted_id)

    return {
        "status": "ok",
        "message": "Data created successfully",
        "data_id": data_id
    }