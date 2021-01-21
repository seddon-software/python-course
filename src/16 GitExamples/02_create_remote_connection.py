from single_step import s

# in this script we end up storing a password in plain text in a git configuration file
# this is not secure.
# However there are a number of alternatives to doing this - just look on google

repo = "myrepo"
username = "seddon-software"        # change this
password = input("Enter password: ")
cmd = "git remote add origin https://{0}:{1}@github.com/{0}/{2}.git".format(username, password, repo)



s('cd myrepo')
# make sure you have created the remote repo: myrepo
s(cmd)
s('git remote -v')
s('git push -u origin master')

