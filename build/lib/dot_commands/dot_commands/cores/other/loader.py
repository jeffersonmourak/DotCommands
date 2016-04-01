import sys
from dot_commands import dotFile

def start(currentPath, arguments):
    action = arguments[0]
    dotFile.findAndRun(action,currentPath)
