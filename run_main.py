# adminlte :: dash- flask 
# noti-api :: fastapi - uvicorn

from template.homeboard  import app
# app = dash.Dash(__name__, requests_pathname_prefix="/dash/")

# ------
import uvicorn as uvicorn
from fastapi import FastAPI
from starlette.middleware.wsgi import WSGIMiddleware

from app.routes import index #auth

def create_app():
    srvr=FastAPI()
    srvr.mount("/dash", WSGIMiddleware(app.server))   # /dash

    srvr.include_router(index.router)
    return srvr

mysrvr = create_app()

if __name__ == "__main__":
    uvicorn.run("run_main:mysrvr", port=8888, reload=True)