import actions
import dotFile

def start(currentPath, arguments):
    action = arguments[0]
    arguments = arguments[1:]
    try:
        trigger = getattr(actions, action)
        trigger(arguments)
    except AttributeError:
        dotFile.findAndRun(action,currentPath)
