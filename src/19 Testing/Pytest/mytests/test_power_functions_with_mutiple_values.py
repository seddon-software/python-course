import sys
sys.path.append("..")
from src.mycode import * 


import pytest 
 
@pytest.mark.parametrize("input, output",[(5,25),(6,36),(7,49),(8,64)]) 
def test_the_square_function(input, output): 
    assert square(input) == output 


