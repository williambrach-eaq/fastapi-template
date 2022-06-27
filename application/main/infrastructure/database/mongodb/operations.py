from abc import ABC
from typing import Dict

import motor.motor_asyncio

from application.main.config import settings
from application.main.infrastructure.database.db_interface import DataBaseOperations
from application.main.utility.config_loader import ConfigReaderInstance


class Mongodb(DataBaseOperations, ABC):
    def __int__(self):
        super(Mongodb, self).__init__()

    async def update_single_db_record(self, uri, record: Dict):

        db_name = "db"
        col_name = "collection_1"

        client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        collection = client[db_name][col_name]
        result = await collection.update_one({"i": 51}, {"$set": {"key": "value"}})

    async def update_multiple_db_record(self, uri, record: Dict):

        db_name = "db"
        col_name = "collection_1"

        client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        collection = client[db_name][col_name]
        result = await collection.update_many({}, {"$set": {"test": 2}})

    async def fetch_single_db_record(self, uri, unique_id: str):

        db_name = "db"
        col_name = "collection_1"

        client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        collection = client[db_name][col_name]
        result = await collection.find_one({}, {"_id": 0})
        return result

    async def fetch_multiple_db_record(self, uri, unique_id: str):

        db_name = "db"
        col_name = "collection_1"

        client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        collection = client[db_name][col_name]
        cursor = collection.find({}, {"_id": 0})
        result = await cursor.to_list(length=100)
        return result

    async def insert_single_db_record(self, uri, record: Dict):

        db_name = "db"
        col_name = "collection_1"

        client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        collection = client[db_name][col_name]
        result = await collection.insert_one(record)

    async def insert_multiple_db_record(self, uri, record: Dict):

        db_name = "db"
        col_name = "collection_1"

        client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        collection = client[db_name][col_name]
        result = await collection.insert_many(record)

    async def delete_single_db_record(self, uri, record: Dict):

        db_name = "db"
        col_name = "collection_1"

        client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        collection = client[db_name][col_name]
        result = await collection.delete_one({"i": {"$gte": 1000}})

    async def delete_multiple_db_record(self, uri, record: Dict):

        db_name = "db"
        col_name = "collection_1"

        client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        collection = client[db_name][col_name]
        result = await collection.delete_many({"i": {"$gte": 1000}})

    async def count_documents_in_db(self, uri, collectionName):

        db_name = "db"
        col_name = collectionName

        client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        collection = client[db_name][col_name]
        result = await collection.count_documents({})
        return result
