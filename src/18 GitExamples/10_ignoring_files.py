import sys
from single_step import s

s('cd myrepo')
s('echo f\* > .gitignore')
s('echo g\* >> .gitignore')

if sys.platform == "win32":
    s('type .gitignore')
else:
    s('cat .gitignore')    
s('git rm -r --cached .')
s('git add .')
s('git commit -am "Remove ignored files"')


