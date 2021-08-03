import sys
from single_step import s


def tagIt(tagId):
#    s('git add .')
#    s('git commit -m "added files about to be tagged"')
    s('git log --pretty=oneline')
    commitId = input(f'\nenter characters of the commit id to tag with {tagId}: ')
    s('git tag', tagId, commitId)
    s('git show-ref --tags')
    s('git log --pretty=oneline --decorate=full')
    
s('cd myrepo')
tagIt('1.0.0')
tagIt('1.0.1')
tagIt('1.0.2')

