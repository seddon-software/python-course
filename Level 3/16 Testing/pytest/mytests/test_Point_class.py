import pytest
from src.Point import *

@pytest.fixture
def pointUnderTest():
    return Point(3,4)

def test_Constructor(pointUnderTest):
    """constructor test"""
    assert "3,4" == pointUnderTest.display()

def test_MoveBy5and2(pointUnderTest):
    """moveBy test(1)"""
    pointUnderTest.moveBy(5, 2)
    assert "8,6" == pointUnderTest.display()
    
@pytest.mark.intended_to_fail
def test_MoveBy5and2version2(pointUnderTest):
    """moveBy test(2)"""
    pointUnderTest.moveBy(5, 2)
    assert "8,7" == pointUnderTest.display()
    
def test_DistanceIs5(pointUnderTest):
    """distance test(1)"""
    assert 5 == pointUnderTest.get_distance()

@pytest.mark.intended_to_fail
def test_DistanceIs5_1(pointUnderTest):
    """distance test(2)"""
    assert 5.1 == pointUnderTest.get_distance()

