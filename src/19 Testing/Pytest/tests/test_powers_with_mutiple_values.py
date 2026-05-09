import sys, os
sys.path.append("../src")
from powers import * 


import pytest 
 
@pytest.mark.parametrize("input, output",[(5,25),(6,36),(7,49),(8,64)]) 
def test_the_square_function(input, output): 
    assert square(input) == output 


if __name__ == "__main__":
    os.system(f"pytest '{__file__}'")
