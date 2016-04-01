import os.path
import subprocess

from dot_commands import installation

def load(path):
    try:
        dotFile = open(path+"/.dot_profile")
        commands = [line.rstrip('\n') for line in dotFile]
        dotFile.close()
        return commands
    except IOError:
        print ".dot_profile not found"
        exit(0)

def updatePermissions(filename):
    command = ["chmod", "+x", filename]
    try:
        command = subprocess.Popen(command, stdout=subprocess.PIPE)
        output = command.communicate()[0]
        print output
    except OSError as e:
            print e,

def list(path):
    commands = load(path)

    installed = installation.path + "/bin/"

    for command in commands:
        line = command.split("=")
        action = line[0].lower()
        command = line[1]

        if not os.path.isfile(installed+"."+action):
            print "Creating ." + action
            filename = open(installed+"."+action, "w")
            filename.write("python " + getInstalledPath() + "/dotcommands.py " + action + " $*")
            filename.close()
            print "Updating permissions to ." + action
            updatePermissions(installed+"."+action)
        else:
            print "Skiped because this command exists"

    print "Done!"
