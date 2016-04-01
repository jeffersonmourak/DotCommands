# .Commands

## What's .commands
.commands are shortcut commands to unify your way to manage your projects

# Installation

```

	git clone https://github.com/jeffersonmourak/DotCommands.git
	cd DotCommands
	python setup.py install

```

# Usage

## Installing some packages
Imagine you have a node.js project, so if you want install a module like ```socke.io```
you run ```.install socket.io```

but now you need to change something in your python project, so you enter in project's
folder and type ```.install oxente```

that's how .commands work, you got just one command to run every thing

## Get informations about project
Enter in project's folder and type ```.info```
and you will see

```
Project main language:
JavaScript

Project Data:
1º JavaScript files  ------------------------------ 45.13% - 422
2º Other files  ----------------------------------- 23.96% - 224
3º Python files  ---------------------------------- 18.07% - 169
4º CSS (Cascade Style Sheet) files  --------------- 5.24% - 49
5º HTML (Hyper Text Markup Language) files  ------- 3.96% - 37
6º Markdown files  -------------------------------- 3.10% - 29
7º XML (eXtended Markup Language) files  ---------- 0.53% - 5

```

also you can create your commands too.
to make it, create a ```.dot_profile```
and set the name of command
```
RUN=python manage.py runserver
```
then, run ```.setup```
and this command will be created and ready to run

# CURRENT STATUS
The module now can detect 18 different file extensions

- Python
- JavaScript
- HTML
- CSS
- ASP Classic
- ASP.NET
- Coldfusion
- Erlang
- Perl
- PHP
- Ruby
- XML
- C
- Java
- Markdown
- DLL
- A

# Licence
- MIT
