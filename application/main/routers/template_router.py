from multiprocessing.connection import wait
from typing import List
from typing import Optional
from typing import Union
import json
from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from fastapi import File, UploadFile
from influxdb_client import Point, WritePrecision
from datetime import datetime
import time

from pydantic import BaseModel

from application.initializer import db_mongo_instance, logger_instance, db_influx_instance
from application.main.services.template_service import (
    TemplateService,
)


template_service = TemplateService()


#### MODELS

# https://fastapi.tiangolo.com/tutorial/body/
class TemplateModel(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    key1: Optional[float] = None
    key2: Optional[str] = None
    key3: Optional[int] = None

class TemplateModelInflux(BaseModel):
    tag: str
    tag1: Union[str, None] = None
    field: str
    field_value: float
    time: Union[str, None] = None



router = APIRouter(prefix="/template")

##### DATABASE INSTANCES
_db = db_mongo_instance
_db_influx = db_influx_instance

##### LOGGER INSTANCE
logger = logger_instance.get_logger(__name__)


##### API CALLS


@router.get("/json")
async def template1():
    logger.info("Json template response")

    return JSONResponse(content={"message": "Hello World! 👍🏻"}, status_code=200)


@router.get("/list", response_model=List[TemplateModel])
async def template12(r: List[TemplateModel]):
    logger.info("List input, response")

    data = {
        "name": "string",
        "description": "string",
        "price": 0,
        "tax": 0,
        "key1": 0,
        "key2": "string",
        "key3": 0,
    }
    return [data]

@router.get("/basic")
async def template3(input_text: str):
    logger.info("Basic response")
    result = await _db.update_multiple_db_record("1")
    question_type = template_service.classify(input_text)
    return {
        "data" : result
    }


@router.post("/fileInput")
async def template4(file: UploadFile = File(...)):
    logger.info("File input, response")

    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    image = ""
    image_category = await template_service.classifyImage(image)
    return image_category


@router.post("/insertSingleInflux")
async def insertSingleInflux(r: TemplateModelInflux):
    logger.info("Insert Single Influx response")
    point = Point("mem") \
    .tag(r.tag, r.tag1) \
    .field(r.field, r.field_value) \
    .time(datetime.utcnow(), WritePrecision.NS)

    result = await _db_influx.insert_single_db_record(point)
    return {"insertSuccess" : result}


@router.post("/insertMultiInflux")
async def insertMultiInflux(r: List[TemplateModelInflux]):
    logger.info("Insert Multi Influx response")

    points = []
    for p in r:
        time.sleep(0.0005)
        points.append(Point("mem") \
        .tag(p.tag, p.tag1) \
        .field(p.field, p.field_value) \
        .time(datetime.utcnow(), WritePrecision.NS))

    result = await _db_influx.insert_multiple_db_record(points)
    return {"insertSuccess" : result}


@router.get("/readInfluxSingle")
async def readInfluxSingle(time: str, tag: str, tag1: str):
    logger.info("Single fetch Influx")
    result = await _db_influx.fetch_single_db_record(time, tag, tag1)
    return {
        "data" : result
    }


@router.get("/readInfluxMulti")
async def readInfluxMulti(time: str, tag: str, tag1: str):
    logger.info("Multi fetch Influx")
    result = await _db_influx.fetch_multiple_db_record(time, tag, tag1)
    return {
        "data" : result
    }


@router.get("/countInflux")
async def countInflux(time: str, tag: str, tag1: str):
    logger.info("Count Influx")
    result = await _db_influx.count_records_in_db(time, tag, tag1)
    return {
        "data" : result
    }


@router.put("/updateSingleInflux")
async def updateSingleInflux(r: TemplateModelInflux):
    logger.info("Update Single Influx response")
    point = Point("mem") \
    .tag(r.tag, r.tag1) \
    .field(r.field, r.field_value) \
    .time(r.time, WritePrecision.NS)

    result = await _db_influx.update_single_db_record(point)
    return {"updateSuccess" : result}


@router.put("/updateMultiInflux")
async def updateMultiInflux(r: List[TemplateModelInflux]):
    logger.info("Update Multi Influx response")

    points = []
    for p in r:
        points.append(Point("mem") \
        .tag(p.tag, p.tag1) \
        .field(p.field, p.field_value) \
        .time(p.time, WritePrecision.NS))

    result = await _db_influx.insert_multiple_db_record(points)
    return {"updateSuccess" : result}