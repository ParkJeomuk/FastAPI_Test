from fastapi import APIRouter
from fastapi import File, UploadFile

import requests
from requests.api import request
from starlette import responses
from starlette.requests import Request
from starlette.responses import JSONResponse

from pydantic import BaseModel
import json

#from inspect import currentframe as frame
from datetime import datetime
from dataclasses import asdict
from typing import Optional

from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


#--------add dash 20220108 pju-----------------------------------------------------------------
from ui.sidebar_callbacks import update_breadcrumbs, activate_page_content
from pages.basic_boxes.callbacks import update_box_graph
from pages.tab_cards.callbacks   import display_tabbox1
from pages.gallery_1.callbacks import make_graph
from pages.gallery_2.callbacks import update_figure

# Dash Page --------------------------------------------------------------------------------
# from pages.dash_pages.callbacks import dash_data_load
from pages.dash_pages.callbacks import dash_plot1_render
from pages.dash_pages.callbacks import dash_plot2_render
from pages.dash_pages.callbacks import dash_plot3_render
from pages.dash_pages.callbacks import dash_plot4_render
from pages.dash_pages.callbacks import dash_plot5_render
from pages.dash_pages.callbacks import dash_data_load
from pages.dash_pages.callbacks import dash_data_table_load
from pages.dash_pages.callbacks import dash_render_datatable
#--------add dash 20220108 pju-----------------------------------------------------------------



router = APIRouter()
# -------------------
# data model
# -------------
db = []

class City(BaseModel):
    name:str
    timezone:str

class CityModify(BaseModel):
    id: int
    name:str
    timezone:str

templates = Jinja2Templates(directory="template")


@router.get("/")
async def root(req: Request):
    """
    `ELB 상태 체크용 API` \n
    :return:
    """
    return JSONResponse( {'hello':'sixxx'} )

@router.get("/cities", response_class=HTMLResponse)
def get_cities(request: Request):
    #result=[]
    context={}

    rsCity = []
    cnt =0
    for aCity in db:
        strs = f"http://worldtimeapi.org/api/timezone/{aCity['timezone']}"
        r = requests.get(strs)
        cur_time = r.json()['datetime']
        cnt += 1
        rsCity.append(
        #result.append(
            {'id': cnt,
             'name':aCity['name'],
             'timezone':aCity['timezone'],
             'current_time':cur_time}
        )

    context['request'] = request
    context['rsCity'] = rsCity
    #return results
    return templates.TemplateResponse('city_list.html', context)

@router.get("/cities/{city_id}")
async def get_city(city_id:int):
    #db[]
    aCity = db[city_id-1]
    strs = f"http://worldtimeapi.org/api/timezone/{aCity['timezone']}"
    r = requests.get(strs)
    cur_time = r.json()['datetime']
    return(
        {'name':aCity['name'],
            'timezone':aCity['timezone'],
            'current_time':cur_time}
    )

@router.post("/uploadfile/")
async def create_upload_file(myFile: UploadFile = File(...)):
    contents = await myFile.read()
    con_dict = json.loads(contents)
    for i in con_dict:
        db.append(i)
    print(db)
    return {"filename": myFile.filename}

@router.post("/cities")
async def create_city(city: City):
    db.append(city.dict())
    return db[-1]

@router.delete("/cities/{city_id}")
def delete_city(city_id:int):
    db.pop(city_id-1) 
    return {}