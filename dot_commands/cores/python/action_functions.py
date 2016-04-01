import subprocess

from dot_commands import commands

def makeCommand(string, array):
    packages = " ".join(array)
    string = string + " " + packages
    return string.split(" ")

def pip(packages):
    commands.runCommand(makeCommand("pip install", packages))
