from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#from databases import Database

app = FastAPI()

# Set up CORS (Cross-Origin Resource Sharing) middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure database connection
#database = Database("postgresql://username:password@localhost/database_name")
#app.state.database = database

# @app.on_event("startup")
# async def startup():
#     # Connect to the database
#     await database.connect()

# @app.on_event("shutdown")
# async def shutdown():
#     # Disconnect from the database
#     await database.disconnect()

# Define your API routes and endpoints here
# Example:
@app.get("/hello")
async def hello():
    return {"message": "Hello, FastAPI!"}
