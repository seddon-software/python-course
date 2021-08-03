import sys
from single_step import s


githubUserName = "Chris Seddon"                # change this
githubEmail = "seddon-software@keme.co.uk"      # change this

# create local repo
def windows():
    s(f'git config --global user.name "{githubUserName}"')
    s(f'git config --global user.email {githubEmail}')
    s('rd /S /Q myrepo')
    s('md myrepo')
    s('cd myrepo')
    s('git init')
    
    # add a README file and commit
    s('echo "This is my new repo" > README.txt')
    s('git add README.txt') 
    s('git commit -m "first commit"')

def unix():
    s(f'git config --global user.name "{githubUserName}"')
    s(f'git config --global user.email {githubEmail}')
    s('rm -rf myrepo')
    s('mkdir myrepo')
    s('cd myrepo')
    s('git init')
    
    # add a README file and commit
    s('echo "This is my new repo" > README.txt')
    s('git add README.txt') 
    s('git commit -m "first commit"')


if sys.platform == "win32":
    windows()
else:
    unix()
