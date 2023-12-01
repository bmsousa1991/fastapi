from typing import List
import uvicorn
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from psycopg2 import connect
from database import get_db
from schemas import MovieBase
from psycopg2.extensions import connection
from fastapi.responses import RedirectResponse


app = FastAPI(
    title="Movie FastAPI Application",
    description="Movie FastAPI Application with Swagger, psycopg2, Postgres, and Pydantic",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")



if __name__ == "__main__":
    uvicorn.run("main:app", port=9000, reload=True)
