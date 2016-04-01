import os, sys
from distutils.core import setup
from distutils.command.install import install as _install

def copy_dir():
    dir_path = 'dot_commands'
    base_dir = os.path.join('dot_commands', dir_path)
    for (dirpath, dirnames, files) in os.walk(base_dir):
        for f in files:
            yield os.path.join(dirpath.split('/', 1)[1], f)

def _post_install(dir):
    from subprocess import call
    call([sys.executable, 'install.py'],
         cwd=os.path.join(dir, 'dot_commands'))


class install(_install):
    def run(self):
        _install.run(self)
        self.execute(_post_install, (self.install_lib,),
                     msg="Running post install task")

setup(
  name = 'dot_commands',
  packages = ['dot_commands'], # this must be the same as the name above
  version = '0.1',
  description = 'Project command unification. powered with python',
  author = 'Jefferson Moura',
  author_email = 'jefinho.moura14@gmail.com',
  # url = 'https://github.com/peterldowns/mypackage', # use the URL to the github repo
  # download_url = 'https://github.com/peterldowns/mypackage/tarball/0.1', # I'll explain this in a second
  keywords = ['dotcommands', 'dot', 'command'], # arbitrary keywords
  classifiers = [],
  package_data = {
	'' : [f for f in copy_dir()]
  },
  cmdclass={'install': install},
)
