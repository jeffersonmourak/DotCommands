# -*- coding: utf-8 -*-

import os
import importlib
import sys

from dot_commands import fileAnalizer
from dot_commands import setupCommands
from dot_commands import installation

def initiator(name):
    module = importlib.import_module("dot_commands.cores." + projectType.lower() + ".loader")
    return getattr(module, "start")

def initiateModule(name, arguments):
    currentPath = os.getcwd()
    initiator(name)(currentPath, arguments)

def getInstalledPath():
    pathArray = __file__.split("/")[:-1]
    return "/".join(pathArray)

if __name__ == "__main__":
    installation.path = getInstalledPath()
    projectType = fileAnalizer.getProjectMainType(os.getcwd())

    arguments = sys.argv[1:]

    if not arguments[0] == "setup":
        initiateModule(projectType.lower(), arguments)

    else:
        setupCommands.list(os.getcwd())
