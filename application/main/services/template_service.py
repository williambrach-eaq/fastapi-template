import pickle
import re
import nltk
from application.main.config import settings
from application.initializer import LoggerInstance

class TemplateService(object):

    def __init__(self) -> None:
        self.logger = LoggerInstance().get_logger(__name__)

        # LOAD CONFIG VARIABLES
        #self.question_classification_model = settings.APP_CONFIG.CLASSIFICATION_MODEL


    @staticmethod
    def classify(input_text: str) -> str:
        return "TEMPLATE"
    
    @staticmethod
    def classifyImage(image: bytes) -> str:
        return ""
