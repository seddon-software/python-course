from single_step import s

s('cd myrepo')
s('git status')
s('git checkout master')
s('echo "hello world" > hello4.txt')
s('echo "hello world" > hello5.txt')
s('echo "hello world" > hello6.txt')
s('git add .') 
s('git status') 
s('git commit -m "more files for master branch"')
s('git push -u origin master')

