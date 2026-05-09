'''
run tests that use multiple test values
see inside the test file - it contains the line:
    @pytest.mark.parametrize("input, output",[(5,25),(6,36),(7,49),(8,64)]) 
'''

import os

os.chdir("tests")
os.system("pytest test_powers_with_mutiple_values.py")

# verbose version
os.system("pytest test_powers_with_mutiple_values.py -v")