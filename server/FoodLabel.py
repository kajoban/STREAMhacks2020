import os, io
from google.cloud import vision
from google.cloud.vision import types
import pandas as pd

class FoodLabel(object):
        
    '''
        Pass image via HTTP request as bytes
    '''
    def __init__(self, image):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =r'Carbon_Foodprint.json'

        client = vision.ImageAnnotatorClient()

        image = vision.types.Image(content=image)
        response = client.object_localization(image = image)
        localized_object_annotations = response.localized_object_annotations

        self.labels = []
        for obj in localized_object_annotations:
            if obj.score >= 0.7:
                self.labels.append(obj.name)
    def getLabels(self):
        return self.labels
    



