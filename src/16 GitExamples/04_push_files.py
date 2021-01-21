from single_step import s

s('cd myrepo')
s('echo "hello world" > hello1.txt')
s('echo "hello world" > hello2.txt')
s('echo "hello world" > hello3.txt')
s('git add .') 
s('git status') 
s('git commit -m "added more files"')
s('git push -u origin master')

