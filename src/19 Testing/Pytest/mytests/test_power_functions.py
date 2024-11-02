import sys
sys.path.append("..")
from src.mycode import * 



def test_square_of_4_is_16(): 
    assert square(4) == 16 

def test_cube_of_4_is_64(): 
    assert cube(4) == 64 

def test_quad_of_4_is_256(): 
    assert quad(4) == 256 


