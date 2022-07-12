import asyncio
from typing import Dict
from influxdb_client import Point
from typing import List


from application.main.config import settings
from application.main.infrastructure.database.influxdb.operations import Influxdb
from application.main.utility.config_loader import ConfigReaderInstance


class DataBase:
    def __init__(self):
        self._db = Influxdb()
        self.db_config = ConfigReaderInstance.yaml.read_config_from_file(
            settings.APP_CONFIG.SETTINGS_DIR.joinpath(f"influxdb_config.yaml")
        ).__dict__

        self.host = self.db_config[settings.DEV_INFLUX_DB]["host"]
        self.port = self.db_config[settings.DEV_INFLUX_DB]["port"]
        self.user = self.db_config[settings.DEV_INFLUX_DB]["user"]
        self.token = self.db_config[settings.DEV_INFLUX_DB]["token"]
        self.org = self.db_config[settings.DEV_INFLUX_DB]["org"]
        self.bucket = self.db_config[settings.DEV_INFLUX_DB]["bucket"]


        self.connection_uri = f"http://{self.host}:{self.port}"

    async def get_database_config_config_details(self):
        return self._db

    async def get_connection_uri(self):
        return self.connection_uri

    async def update_single_db_record(self, record: Point):
        loop = asyncio.new_event_loop()
        return loop.run_until_complete(self._db.update_single_db_record(self.connection_uri, self.token, self.org, self.bucket, record))

    async def update_multiple_db_record(self, record: List[Point]):
        loop = asyncio.new_event_loop()
        return loop.run_until_complete(self._db.update_multiple_db_record(self.connection_uri, self.token, self.org, self.bucket, record))

    async def fetch_single_db_record(self, time: str, tag: str, tag1: str):
        loop = asyncio.new_event_loop()
        return loop.run_until_complete(self._db.fetch_single_db_record(self.connection_uri, self.token, self.org, self.bucket, time, tag, tag1))

    async def fetch_multiple_db_record(self, time: str, tag: str, tag1: str):
        loop = asyncio.new_event_loop()
        return loop.run_until_complete(self._db.fetch_multiple_db_record(self.connection_uri, self.token, self.org, self.bucket, time, tag, tag1))

    async def insert_single_db_record(self, record: Point):
        loop = asyncio.new_event_loop()
        return loop.run_until_complete(self._db.insert_single_db_record(self.connection_uri, self.token, self.org, self.bucket, record))

    async def insert_multiple_db_record(self, record: List[Point]):
        loop = asyncio.new_event_loop()
        return loop.run_until_complete(self._db.insert_multiple_db_record(self.connection_uri, self.token, self.org, self.bucket, record))

    async def count_records_in_db(self, time: str, tag: str, tag1: str):
        loop = asyncio.new_event_loop()
        return loop.run_until_complete(self._db.count_records_in_db(self.connection_uri, self.token, self.org, self.bucket, time, tag, tag1))
