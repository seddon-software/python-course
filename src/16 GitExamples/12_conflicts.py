import sys
from single_step import s

s('cd myrepo')


s('git checkout mybranch')
s('echo This was written from the mybranch branch > conflict_file')
s('git add .')
s('git commit -m "adding a file to mybranch demonstrating conflicts"')
s('git push -u origin mybranch')

s('git checkout master')
s('echo This was written from the master branch > conflict_file')
s('git add .')
s('git commit -m "adding a file to master demonstrating conflicts"')
s('git push -u origin master')

s('git merge mybranch')


if sys.platform == "win32":
    s('type conflict_file')
else:
    s('cat conflict_file')    




