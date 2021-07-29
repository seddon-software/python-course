import os

# only run tests with a given marker
os.system("pytest -m intended_to_fail -v")

