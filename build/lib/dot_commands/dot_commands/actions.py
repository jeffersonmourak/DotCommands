# -*- coding: utf-8 -*-
from dot_commands import setupCommands, fileAnalizer
import os
registerd = ["setup", "info"]
''
def _prettyTable(data, total):
	maxSize = 0
	postWordSize = 7
	for line in data:
		if len(line["label"]) > maxSize:
			maxSize = len(line["label"])

	data = sorted(data, key=lambda k: k['count'])[::-1]

	for index,line in enumerate(data):
		percentOffset = (maxSize - len(line["label"])) + postWordSize
		percent = float((100.0*line["count"]) / total)

		print str(index + 1) + "º " + line["label"] + " files ",
		print "-" * percentOffset,
		print("%.2f%% - %d" % (percent, line["count"]))

def setup():
	setupCommands.list(os.getcwd())

def info():
	_dir = os.getcwd()
	print "Project main language:"
	print fileAnalizer.getProjectMainType(_dir)
	print "\nProject Data: "
	files, total = fileAnalizer.listFiles(_dir, True)

	_prettyTable(files,total)




# n - 100
# x - y
# n/y = 100x
# y = 100x/n
