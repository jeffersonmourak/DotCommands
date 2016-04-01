import action_functions

def install(arguments):
    if len(arguments) > 0:
        action_functions.pip(arguments)
    else:
        print "Please enter a module to install"
