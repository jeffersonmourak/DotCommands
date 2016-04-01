# -*- coding: utf-8 -*-
from os import listdir
from os.path import isfile, join, isdir

import patterns
import common

def listDirectory(_dir):
    files = []

    for f in listdir(_dir):
        if isfile(join(_dir, f)):
            files.append(f)
        elif isdir(join(_dir, f)):
            files += listDirectory(join(_dir, f))

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

def listFiles(_dir, total=False):
    filesType = []
    countFiles = 0
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
        countFiles += 1
    return (filesType, countFiles) if total else filesType

def getProjectMainType(_dir):
    filesType = listFiles(_dir)
    return verifyMajority(filesType)["name"]
