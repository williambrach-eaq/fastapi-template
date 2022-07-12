from typing import List
from typing import Optional
from typing import Union
import json
from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from fastapi import File, UploadFile

from pydantic import BaseModel

from application.initializer import db_mongo_instance, logger_instance
from application.main.services.template_service import (
    TemplateService,
)

from application.main.infrastructure.database.postgresql.operations import PostgresDb
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


router = APIRouter(prefix="/template")

##### DATABASE INSTANCES
_db = db_mongo_instance


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
    result = PostgresDb.fetch_multiple_db_record()
    print(result)
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
