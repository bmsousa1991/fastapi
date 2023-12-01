from pydantic import BaseModel

class MovieBase(BaseModel):
    movie_id = int
    title = str
    budget = int
    homepage = str
    overview = str
    popularity = int
    release_date = str
    revenue = int
    runtime = int
    movie_status = str
    tagline = str
    vote_average = int
    vote_count = int

    class Config:
        from_attributes = True