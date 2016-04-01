import commands

def load(path):
    try:
        dotFile = open(path+"/.dot_profile")
        commands = [line.rstrip('\n') for line in dotFile]
        dotFile.close()
        return commands
    except IOError:
        print ".dot_profile not found"
        exit(0)

def getCommand(name, path):
    commands = load(path)

    for command in commands:
        line = command.split("=")
        action = line[0]
        command = line[1]
        if action.lower() == name:
            return {
                "name": action.lower(),
                "command": command
            }

def findAndRun(name, path):
    action = getCommand(name, path)
    if action == None:
        print "Command not found"
    else:
        print "Running action " + action["name"]
        commandLine = action["command"].split(" ")
        commands.runCommand(commandLine, path)
