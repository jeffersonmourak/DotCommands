# -*- coding: utf-8 -*-

import os

projectPattern = [
    {
        "name": "Python",
        "extentions": [".pyc", ".py"]
    }
]

def fileProjectType(filename):
    filename, ext = os.path.splitext(filename)
    _type = getByExtention(ext)
    return "Other" if _type == False else _type

def getByExtention(extention):
    for pattern in projectPattern:
        if extention in pattern["extentions"]:
            return pattern["name"]

    return False
