import subprocess

def runCommand(command):
    try:
        command = subprocess.Popen(command, stdout=subprocess.PIPE)
        output = command.communicate()[0]
        print output
    except OSError as e:
            print e,

def makeCommand(command, argumentList):
    arguments = " ".join(argumentList)
    command += " " + arguments
    return command.split(" ")

def pip(packages):
    runCommand(makeCommand("pip install", packages))
