import sys
from single_step import s

s('cd myrepo')
s('git branch mybranch')
s('git checkout mybranch')
 
s('echo "branch file no. 1" > branch1.txt')
s('echo "branch file no. 2" > branch2.txt')
s('echo "branch file no. 3" > branch3.txt')
if sys.platform == "win32":
    s('del hello3.txt')
else:
    s('rm hello3.txt')
s('git add .') 
s('git status') 
s('git commit -m "created a new branch"')
# this is required to let the remote repo know we have a new branch
s('git push --set-upstream origin mybranch')

