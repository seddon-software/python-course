import os; os.system("clear")

print("all src and test directories must contain '__init__.py'")
os.system("tree ../src")
input("continue")
os.system("tree mytests")
input("continue")

# only run tests in a given file
os.system("pytest mytests/test_point_class.py")

# clean up "pyc" files
os.system("find .. -name '*.pyc' -exec rm {} \;")

