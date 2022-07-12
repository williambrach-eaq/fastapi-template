from abc import ABC
from typing import Dict
import asyncio
from datetime import datetime
from typing import List


from influxdb_client import Point, WritePrecision
from influxdb_client.client.influxdb_client_async import InfluxDBClientAsync
from application.main.config import settings
from application.main.infrastructure.database.db_interface import DataBaseOperations
from application.main.utility.config_loader import ConfigReaderInstance


class Influxdb(DataBaseOperations, ABC):
    def __int__(self):
        super(Influxdb, self).__init__()

    async def update_single_db_record(self, connection_uri, token, org_name, bucket_name, record: Point):

        async with InfluxDBClientAsync(url=connection_uri, token=token, org=org_name) as client:
            write_api = client.write_api()
            result = await write_api.write(bucket_name, org_name, record)
            await client.close()
            return result

    async def update_multiple_db_record(self, connection_uri, token, org_name, bucket_name, record: List[Point]):

        async with InfluxDBClientAsync(url=connection_uri, token=token, org=org_name) as client:
            write_api = client.write_api()

            result = await write_api.write(bucket_name, org_name, record)
            await client.close()
            return result


    async def fetch_single_db_record(self, connection_uri, token, org_name, bucket_name, time: str, tag: str, tag1: str):

        async with InfluxDBClientAsync(url=connection_uri, token=token, org=org_name) as client:
            query = f'from(bucket: "{bucket_name}") |> range(start: {time})  |> filter(fn: (r) => r["{tag}"] == "{tag1}") |> last()'
            tables = await client.query_api().query(query, org=org_name)
            await client.close()
            for table in tables:
                return table.records

    async def fetch_multiple_db_record(self, connection_uri, token, org_name, bucket_name, time: str, tag: str, tag1: str):

        async with InfluxDBClientAsync(url=connection_uri, token=token, org=org_name) as client:
            query = f'from(bucket: "{bucket_name}") |> range(start: {time})  |> filter(fn: (r) => r["{tag}"] == "{tag1}")'
            tables = await client.query_api().query(query, org=org_name)
            await client.close()
            for table in tables:
                return table.records

    async def insert_single_db_record(self, connection_uri, token, org_name, bucket_name, record: Point):

        async with InfluxDBClientAsync(url=connection_uri, token=token, org=org_name) as client:
            write_api = client.write_api()
            result = await write_api.write(bucket_name, org_name, record)
            await client.close()
            return result

    async def insert_multiple_db_record(self, connection_uri, token, org_name, bucket_name, record: List[Point]):

        async with InfluxDBClientAsync(url=connection_uri, token=token, org=org_name) as client:
            write_api = client.write_api()

            result = await write_api.write(bucket_name, org_name, record)
            await client.close()
            return result

    async def count_records_in_db(self, connection_uri, token, org_name, bucket_name, time: str, tag: str, tag1: str):

        async with InfluxDBClientAsync(url=connection_uri, token=token, org=org_name) as client:
            query = f'from(bucket: "{bucket_name}") |> range(start: {time})  |> filter(fn: (r) => r["{tag}"] == "{tag1}") |> count()'
            tables = await client.query_api().query(query, org=org_name)
            await client.close()
            for table in tables:
                return table.records
