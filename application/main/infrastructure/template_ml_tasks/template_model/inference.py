import os
import logging
import json
import numpy as np
import joblib

from application.initializer import LoggerInstance
from application.main.config import settings

logger = LoggerInstance().get_logger(__name__)
model = None
MODEL_NAME = "regressor_1"


class InferenceTask:

    @staticmethod
    async def load_model(model_path):

        model = None
        model = joblib.load(model_path)

        return model

    @staticmethod
    async def init():
        model_path = settings.MODEL_CONFIGS[MODEL_NAME].path

        logging.info("Init complete")
        if model is None:
            await InferenceTask.load_model(model_path)

    @staticmethod
    def run(raw_data):
        logger.info("model 1: request received")
        global model
        if model is None:
            InferenceTask.init()

        # DO PREDICTION
        result = None

        logger.info("Request processed")
        return result
