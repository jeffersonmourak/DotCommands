from dot_commands import setupCommands, fileAnalizer
import os
registerd = ["setup", "info"]

def setup():
	setupCommands.list(os.getcwd())

def info():
	_dir = os.getcwd()
	print "Project main language:"
	print fileAnalizer.getProjectMainType(_dir)
	print "\nProject Data: "
	files, total = fileAnalizer.listFiles(_dir, True)

	for language in files:
		print language["name"] + " files: " + str(language["count"]) + " - ",
		percent = float((100.0*language["count"]) / total)
		print("%.2f%%" % percent)



# n - 100
# x - y
# n/y = 100x
# y = 100x/n
