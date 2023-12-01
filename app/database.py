import time
import psycopg2
from psycopg2 import OperationalError

def get_db():
    conn = None
    while not conn:
        try:
            conn = psycopg2.connect(
                dbname="movies",
                user="postgres",
                password="password",
                host="dcs-postgres"
            )
            print("Database connection successful")
        except OperationalError as e:
            print(e)
            time.sleep(5)
    return conn

conn = get_db()