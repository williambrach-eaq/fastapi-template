class LoggerInstance(object):
    def __new__(cls):
        from application.main.utility.logger.custom_logging import LogHandler

        return LogHandler()


class IncludeAPIRouter(object):
    def __new__(cls):
        from application.main.routers.template_router import router as router_template
        from fastapi.routing import APIRouter

        router = APIRouter()
        router.include_router(router_template, prefix="/api/v1", tags=["template"])

        return router


class MongoDbInstance(object):
    def __new__(cls):
        from application.main.infrastructure.database import db_mongo

        return db_mongo.DataBase()

class PsqlInstance(object):
    def __new__(cls):
        from application.main.infrastructure.database import db_postgresql

        return db_postgresql.DataBase()

class InfluxDbInstance(object):
    def __new__(cls):
        from application.main.infrastructure.database import db_influx

        return db_influx.DataBase()


# instance creation
logger_instance = LoggerInstance()
db_mongo_instance = MongoDbInstance()
db_influx_instance = InfluxDbInstance()
