import os, sys, time
import subprocess

def setupTempDirectory():
    tempDirectory = os.path.expandvars("$HOME/tmp")
    if os.path.isdir(tempDirectory):
        return      # nothing to do

    os.system("clear")
    print(f"setting up TEMP directory: {tempDirectory}")
    time.sleep(5)
    # make sure the permissions are ok
    os.system(f"mkdir -p {tempDirectory}")
    os.system(f"chmod 777 {tempDirectory}")
    # create a copy of the current environment
    env = os.environ.copy()
    # add a new environment variable
    env["TEMP"] = tempDirectory
    return env

env = setupTempDirectory()

def red(text):
    return f"\033[31m{text}\033[0m"

def execute(message, cmd, shell=False):
    global env
    time.sleep(5)
    os.system("clear")
    print(f"{red(cmd)}\n{message}")
    print("="*len(message))
    input('?')
    if shell:
        result = subprocess.run(f"{cmd}", env=env, shell=shell)
    else:
        result = subprocess.run(cmd.split(), env=env, shell=shell)
    try:
        result.check_returncode()
    except Exception as e:
        print(e)
        sys.exit(1)
    print()

try:
    import pipx
except:
    execute(message="install pipx", cmd="python -m pip3 install pipx", shell=True)

execute(message="build extension module with pipx", cmd="python -m pipx run build")
execute(message="install extension module with pip", cmd="python -m pip install --force-reinstall .")

execute(message="test", cmd="true")
import roots as r
print(r.sumOfRoots(10))
print()

# clean up
execute(message="clean up", cmd="rm -r dist")
execute(message="tree", cmd="tree .")
