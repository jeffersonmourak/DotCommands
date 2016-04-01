import commands

def install(arguments):
    if len(arguments) > 0:
        commands.pip(arguments)
    else:
        print "Please enter a module to install"
