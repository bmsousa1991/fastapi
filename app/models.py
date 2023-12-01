from sqlalchemy import Column, Integer, String, Numeric, Date, BigInteger
from database import Base

class Movie(Base):
    __tablename__ = "movie"

    movie_id = Column(Integer, primary_key=True, nullable= False)
    title = Column(String(1000), nullable= False)
    budget = Column(Integer, nullable= False)
    homepage = Column(String(1000), nullable= False)
    overview = Column(String(1000), nullable= False)
    popularity = Column(Numeric(12,6), nullable= False)
    release_date = Column(Date, nullable= False)
    revenue = Column(BigInteger, nullable= False)
    runtime = Column(Integer, nullable= False)
    movie_status = Column(String(50), nullable= False)
    tagline = Column(String(1000), nullable= False)
    vote_average = Column(Numeric(4,2), nullable= False)
    vote_count = Column(Integer, nullable= False)
