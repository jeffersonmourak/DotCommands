# -*- coding: utf-8 -*-
from os import listdir
from os.path import isfile, join

import patterns
import common

def listDirectory(_dir):
    files = [f for f in listdir(_dir) if isfile(join(_dir, f))]

    return files

def verifyMajority(array):
    majority = {
        "name": "Other",
        "count": 0
    }

    for item in array:
        if item["count"] > majority["count"]:
            majority = item

    return majority

def getProjectMainType(_dir):
    filesType = []
    files = listDirectory(_dir)

    for filename in files:
        _type = patterns.fileProjectType(filename)
        cachePosition = common.dictKeyInArray("name", _type, filesType)

        if(cachePosition == -1):
            filesType.append({
                "name": _type,
                "count": 1
            })
        else:
            filesType[cachePosition]["count"] += 1

    return verifyMajority(filesType)["name"]
