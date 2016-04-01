# -*- coding: utf-8 -*-

import os

projectPattern = [
    {
        "name": "Python",
        "label": "Python",
        "extentions": [".pyc", ".py", ".pyo"]
    },
    {
        "name": "JavaScript",
        "label": "JavaScript",
        "extentions": [".js"]
    },
    {
        "name": "HTML",
        "label": "HTML (Hyper Text Markup Language)",
        "extentions": [".html", ".htm", ".xhtml", ".jhtml"]
    },
    {
        "name": "CSS",
        "label": "CSS (Cascade Style Sheet)",
        "extentions": [".css"]
    },
    {
        "name": "ASP",
        "label": "ASP Classic",
        "extentions": [".asp"]
    },
    {
        "name": "ASPNET",
        "label": "ASP.NET",
        "extentions": [".aspx", ".axd", ".asx", ".asmx", ".ashx"]
    },
    {
        "name": "Coldfusion",
        "label": "Coldfusion",
        "extentions": [".cfm"]
    },
    {
        "name": "Erlang",
        "label": "Erlang",
        "extentions": [".yaws"]
    },
    {
        "name": "Perl",
        "label": "Perl",
        "extentions": [".pl"]
    },
    {
        "name": "PHP",
        "label": "PHP",
        "extentions": [".php", ".php4", ".php3", ".phtml"]
    },
    {
        "name": "Ruby",
        "label": "Ruby",
        "extentions": [".rb", ".rhtml", ".erb"]
    },
    {
        "name": "XML",
        "label": "XML (eXtented Markup Language)",
        "extentions": [".xml", ".rss", ".svg"]
    },
    {
        "name": "CPP",
        "label": "C++",
        "extentions": [".cpp", ".cxx", ".hpp"]
    },
    {
        "name": "C",
        "label": "C",
        "extentions": [".c", ".h"]
    },
    {
        "name": "Java",
        "label": "Java",
        "extentions": [".class", ".java", ".dpj", ".jsp"]
    },
    {
        "name": "Markdown",
        "label": "Markdown",
        "extentions": [".md"]
    },
    {
        "name": "dll",
        "label": "DLL (Win32 dynamic linked library)",
        "extentions": [".dll"]
    },
    {
        "name": "unixa",
        "label": "A (UNIX static library file)",
        "extentions": [".a"]
    },

]

def fileProjectType(filename):
    filename, ext = os.path.splitext(filename)
    _type = getByExtention(ext)
    return {"name": "Other", "label": "Other"} if _type == False else _type

def getByExtention(extention):
    for pattern in projectPattern:
        if extention in pattern["extentions"]:
            return pattern

    return False
