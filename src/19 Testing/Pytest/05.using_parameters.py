'''
run tests that use multiple test values:
    @pytest.mark.parametrize("input, output",[(5,25),(6,36),(7,49),(8,64)]) 
'''

import os

os.system("pytest mytests/test_power_functions_with_mutiple_values.py")

# verbose version
os.system("pytest mytests/test_power_functions_with_mutiple_values.py -v")