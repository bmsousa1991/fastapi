from sqlalchemy.orm import Session
from models import Base


class MovieData:
 
    def fetch_all(get_db: Session, skip: int = 0, limit: int = 100):
     return get_db.query(Movie).offset(skip).limit(limit).all()
     
    def fetch_by_id(get_db: Session,movie_id):
     return get_db.query(Movie).filter(Movie.movie_id == movie_id).first()
 

 

