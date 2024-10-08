from pydantic import BaseModel

class DataModel(BaseModel):
    kind: str
    backdrop_path: str
    original_title: str
    overview: str
    popularity: float
    poster_path: str
    release_date: str
    title: str
    vote_average: float
    vote_count: int