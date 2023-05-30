from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#from databases import Database
import psycopg2
from database import engine, SQLALCHEMY_DATABASE_URL,Base
from routers import router
#from .models import student

app = FastAPI()

# Set up CORS (Cross-Origin Resource Sharing) middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define your API routes and endpoints here
# Example:
@app.get("/hello")
async def hello():
    return {"message": "Hello, FastAPI!"}


def test_connection():
    try:
        # Connect to an existing database
        # /* eslint-disable-line not -context-manager * /
        with psycopg2.connect(SQLALCHEMY_DATABASE_URL) as conn:

            # Open a cursor to perform database operations
            with conn.cursor() as cur:

                print("connection succss")
    except:
        print("Connection failed")

test_connection()

# Create Database tables
#student.Base.metadata.create_all(bind=engine)
Base.metadata.create_all(bind=engine)

app.include_router(router)
