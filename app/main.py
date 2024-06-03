from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn
from app.database.database import create_tables
from app.device_flow.router import router

API_VERSION = "0.0.0"
TITLE = "OIDC With Cognito"

app = FastAPI(
    title=TITLE,    
    version=API_VERSION,
    contact={"name": "Stijn Janssens", "email": "stijn.janssens@dataminded.com"},
)

app.include_router(router, prefix="/api/auth")

@app.get("/")
def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    load_dotenv("./../env")
    create_tables()
    uvicorn.run("app.main:app", host="0.0.0.0", port=5050, reload=True)