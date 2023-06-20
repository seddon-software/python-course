'''
packaging_tutorial/
└── src/
    └── example_package_YOUR_USERNAME_HERE/
        ├── __init__.py
        └── example.py
'''
import os

src = "packaging_tutorial/src/example_package_me"
os.system(f"mkdir -p {src}")
os.chdir(src)
os.system("touch __init__.py example.py")
code = r"""
def add_one(number):
    return number + 1
"""
os.system(f"echo '{code}' > example.py")
os.system(f"cat example.py")
os.system("tree ../../..")

