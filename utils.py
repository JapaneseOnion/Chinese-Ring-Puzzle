import os
import sys

def getImagePath(image):
    return os.path.join(os.path.dirname(__file__), 'Images', image)