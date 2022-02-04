import uvicorn
from fastapi import FastAPI

from app.routes import index #auth

def create_app():
    srvr=FastAPI()
    srvr.include_router(index.router)
    return srvr

mysrvr = create_app()

# uvicorn main:app --reload
if __name__ == "__main__" :
    uvicorn.run("_main:mysrvr", port=8888, reload=True)
