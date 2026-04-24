import os, time
import subprocess

os.system("mkdir -p $HOME/tmp")
os.system("chmod 777 $HOME/tmp")
# Create a copy of the current environment
env = os.environ.copy()
# Add a new environment variable
env["TEMP"] = os.path.expandvars("$HOME/tmp")

if_build_failed = """if the build fails because of 'failed to map segment from shared object'
you need to run: 
\texport TEMP=~/tmp"""

def execute(message, cmd, shell=False):
    time.sleep(5)
    os.system("clear")
    print(message)
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
        print(if_build_failed)
        sys.exit(1)
    print()

try:
    import pipx
except:
    execute(message="install pipx", cmd="python -m pip install pipx", shell=True)

execute(message="build extension module with pipx", cmd="python -m pipx run build")
execute(message="install extension module with pip", cmd="python -m pip install --force-reinstall .")

execute(message="test", cmd="true")
import roots as r
print(r.sumOfRoots(10))
print()

# clean up
execute(message="clean up", cmd="rm -r dist")
execute(message="tree", cmd="tree .")
