from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from database.database import Base, get_db, engine, SQLALCHEMY_DATABASE_URL
from routers.students import router

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
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(SQLALCHEMY_DATABASE_URL)

        # Open a cursor to perform database operations
        cur = conn.cursor()

        print("Connection success")

        # Close the cursor and connection
        cur.close()
        conn.close()

    except Exception as e:
        print("Connection failed:", str(e))

# Create Database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(router)

test_connection()