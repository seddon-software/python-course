'''
This example is taken from:
    https://packaging.python.org/en/latest/tutorials/packaging-projects/

The package structure should be:
    packaging_tutorial/
    ├── LICENSE
    ├── pyproject.toml
    ├── README.md
    ├── src/
    │   └── example_package_YOUR_USERNAME_HERE/
    │       ├── __init__.py
    │       └── example.py
    └── tests/
'''


from pathlib import Path
import os, webbrowser



# remove old package
topDir = "packaging_tutorial"
os.system(f"rm -r {topDir}")

# set up package
print("create package files")
input("continue? ")
os.system(f"mkdir -p {topDir}")
os.chdir(f"{topDir}")
top = Path(os.getcwd())

packageDir = "src/example_package_diamond_light_source"
testDir = "test"
os.system(f"mkdir -p {packageDir}")
os.system(f"mkdir -p {testDir}")

# copy files
os.system(f"cp ../resources/README.md .")
os.system(f"cp ../resources/LICENSE .")
os.system(f"cp ../resources/pyproject.toml .")
os.system(f"cp ../resources/example.py {packageDir}")
os.system(f"cp ../resources/__init__.py {packageDir}")

os.system(f"tree '{top.absolute()}'")

# build dist
print("build dist")
input("continue? ")
os.system("python -m build")

print("check structure")
input("continue? ")
os.system(f"tree 'dist'")

'''
To register an account, go to https://test.pypi.org/account/register/ and complete the steps on that page. 
You will also need to verify your email address before you’re able to upload any packages.
'''
yesno = input("do you need to register at test/pypi (yes/no)? ")
if yesno == "yes":
    import webbrowser
    webbrowser.open("https://test.pypi.org/account/register")


'''
To securely upload your project, you’ll need a PyPI API token.  You'll need a TOTP application - I've used
Authenticator:
    sudo apt install gnome-authenticator

Create an PyPI token at https://test.pypi.org/manage/account/#api-tokens, setting the “Scope” to “Entire account”. 
Don’t close the page until you have copied and saved the token — you won’t see that token again.
'''
yesno = input("do you need a PyPI API token (yes/no)? ")
if yesno == "yes":
    webbrowser.open("https://test.pypi.org/manage/account/#api-tokens")


yesno = input("do you want to upload current package to TestPyPI (yes/no)? ")
if yesno == "yes":
    os.system("python -m twine upload --repository testpypi dist/*")

input("visit TestPyPI - continue?")
webbrowser.open("https://test.pypi.org/project/example_package_diamond_light_source")

yesno = input("uninstall previously installed test package (yes/no)? ")
if yesno == "yes":
    os.system("pip uninstall example-package-diamond-light-source")

input("install our test package - continue? ")
os.system("pip install -i https://test.pypi.org/simple/ example-package-diamond-light-source")

