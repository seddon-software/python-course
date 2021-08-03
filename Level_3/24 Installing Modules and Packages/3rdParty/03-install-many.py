import os, setPath

# Use this script to setup packages
#
# N.B. if you are installing behind a proxy you will have to set 
#    HTTP_PROXY=http://user:password@yourproxy.com:port
# Alternatively use a local repository:
#    run -f http://localhost/repo foo



# modify this if your installation is behind a proxy
def setProxy(url):
    """example call:
          setProxy("http://wwwcache.rl.ac.uk:8080")
    """
    os.environ["HTTP_PROXY"] = url


def run(cmd):
    os.system("echo " + cmd)
    os.system(cmd)
    
setProxy("")
run("pip install --upgrade beautifulsoup4")
run("pip install --upgrade bottle")
run("pip install --upgrade cherrypy")
run("pip install --upgrade cx_oracle")
run("pip install --upgrade django")
run("pip freeze")

1



