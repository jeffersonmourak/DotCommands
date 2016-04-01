# -*- coding: utf-8 -*-

import os
import importlib
import sys

from dot_commands import fileAnalizer, installation, actions

def initiator(name):
    module = importlib.import_module("dot_commands.cores." + projectType.lower() + ".loader")
    return getattr(module, "start")

def initiateModule(name, arguments):
    currentPath = os.getcwd()
    try:
        initiator(name)(currentPath, arguments)
    except ImportError:
        print "No Module created for this type of project"
def getInstalledPath():
    pathArray = __file__.split("/")[:-1]
    return "/".join(pathArray)

if __name__ == "__main__":
    installation.path = getInstalledPath()
    projectType = fileAnalizer.getProjectMainType(os.getcwd())

    arguments = sys.argv[1:]

    if not arguments[0] in actions.registerd:
        initiateModule(projectType.lower(), arguments)
    else:
        trigger = getattr(actions, arguments[0])
        trigger()
