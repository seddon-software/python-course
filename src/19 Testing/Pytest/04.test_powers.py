'''
In this example we test a different file:
    powers.py
'''

import os

os.system("clear")
print("look at the file being tested: src/powers.py")
os.system("pwd; ls")
os.system("cat ../src/powers.py")

os.system("clear")
print("look at the test file: mytests/test_powers.py")
os.system("cat tests/test_powers.py")

os.system("clear")
os.chdir("tests")
print("run the tests")
os.system("pytest test_powers.py --no-header")

