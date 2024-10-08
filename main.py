from fastapi import FastAPI
from routes.entry import entry_root
from routes.data import data_root
import uvicorn
import os
from fastapi import HTTPException
from fastapi.responses import FileResponse

app = FastAPI()

app.include_router(entry_root)
app.include_router(data_root)

base_path = "./public/videos"

@app.get("/videos/{videourl}")
async def serve_specific_video(videourl: str):
    file_path = os.path.join(base_path, videourl)
    if not os.path.isfile(file_path):
        # print(f"File not found: {file_path}")
        raise HTTPException(status_code=404, detail="Video not found")

    response = FileResponse(file_path)
    response.headers["Accept-Ranges"] = "bytes" 
    return response

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)