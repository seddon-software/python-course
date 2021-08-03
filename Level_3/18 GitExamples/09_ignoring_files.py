import sys
from single_step import s

# create some empty files for use with git ignore
def windows():
    s('cd myrepo')
    s('copy nul > f1')
    s('copy nul > f2')
    s('copy nul > f3')
    s('copy nul > f4')
    s('copy nul > g1')
    s('copy nul > g2')
    s('copy nul > g3')
    s('copy nul > g4')
    s('git add .')
    s('git status')
    s('git commit -m "added some files with name beginning with f or g"')
    s('git push -u origin master')

def unix():
    s('cd myrepo')
    s('touch f1 f2 f3 f4')
    s('touch g1 g2 g3 g4')
    s('git add .')
    s('git status')
    s('git commit -m "added some files with name beginning with f or g"')
    s('git push -u origin master')

if sys.platform == "win32":
    windows()
else:
    unix()



