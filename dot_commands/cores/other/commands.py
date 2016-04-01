import subprocess

def fixPath(command, path):
    for index,item in enumerate(command):
        command[index] = item.replace("./", path + "/")

    return command
def runCommand(command, path):
    command = fixPath(command, path)
    print command
    try:
        command = subprocess.Popen(command, stdout=subprocess.PIPE)
        output = command.communicate()[0]
        print output
    except OSError as e:
        print e,
