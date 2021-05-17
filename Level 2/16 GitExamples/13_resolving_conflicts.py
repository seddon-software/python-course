from single_step import s

s('cd myrepo')

s('echo This was written to resolve the conflict > conflict_file')
s('git add conflict_file')
s('git commit -m "merged master and fixed conflict"')
s('git push -u origin master')

