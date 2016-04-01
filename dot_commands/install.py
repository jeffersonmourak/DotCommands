import os
import subprocess

path = os.getcwd()

def updatePermissions(filename):
    command = ["chmod", "+x", filename]
    try:
        command = subprocess.Popen(command, stdout=subprocess.PIPE)
        output = command.communicate()[0]
        print output
    except OSError as e:
            print e,

def generateBin():
	commands = ["info", "install", "setup"]
	if not os.path.isdir(os.path.join(path, "bin")):
		os.makedirs(path+"/bin")

	for action in commands:
		filename = open(path+"/bin/."+action, "w")
		filename.write("python " + path + "/main.py " + action + " $*")
		filename.close()
		print "updating permissions for " + action
		updatePermissions(path+"/bin/."+action)

def updatePath():
	home = os.environ["HOME"]
	bashprofile = open(os.path.join(home,".bash_profile"), 'a')
	bashprofile.write("\nexport PATH=\"" + path + "/bin:$PATH\"")
	bashprofile.close()

print "Generating binaries"
generateBin()
print "Updating Path"
updatePath()
