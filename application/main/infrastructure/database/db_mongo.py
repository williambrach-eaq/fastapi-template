import asyncio
from typing import Dict
import motor.motor_asyncio


from application.main.config import settings
from application.main.infrastructure.database.mongodb.operations import Mongodb
from application.main.utility.config_loader import ConfigReaderInstance

class DataBase:
    def __init__(self):
        self._db = Mongodb()
        self.db_config = ConfigReaderInstance.yaml.read_config_from_file(
            settings.APP_CONFIG.SETTINGS_DIR.joinpath(f"mongodb_config.yaml")
        ).__dict__

        self.host = self.db_config[settings.DEV_MONGO_DB]["host"]
        self.port = self.db_config[settings.DEV_MONGO_DB]["port"]
        self.user = self.db_config[settings.DEV_MONGO_DB]["user"]
        self.connection_uri = f"mongodb://{self.user}@{self.host}:{self.port}"

    async def get_database_config_config_details(self):
        return self._db

    async def get_connection_uri(self):
        return self.connection_uri

    async def update_single_db_record(self, record: Dict):
        loop = asyncio.new_event_loop()
        return loop.run_until_complete(self._db.update_single_db_record(self.connection_uri,record))

    async def update_multiple_db_record(self, record: Dict):
        loop = asyncio.new_event_loop()
        return loop.run_until_complete(self._db.update_multiple_db_record(self.connection_uri,record))

    async def fetch_single_db_record(self, unique_id: str):
        loop = asyncio.new_event_loop()
        return loop.run_until_complete(self._db.fetch_single_db_record(self.connection_uri,unique_id))

    async def fetch_multiple_db_record(self, unique_id: str):
        loop = asyncio.new_event_loop()
        return loop.run_until_complete(self._db.fetch_multiple_db_record(self.connection_uri,unique_id))

    async def insert_single_db_record(self, record: Dict): 
        loop = asyncio.new_event_loop()
        return loop.run_until_complete(self._db.insert_single_db_record(self.connection_uri, record))        

    async def insert_multiple_db_record(self, record: Dict):
        loop = asyncio.new_event_loop()
        return loop.run_until_complete(self._db.insert_multiple_db_record(self.connection_uri,record))
