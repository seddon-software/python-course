'''
The most important point about testing is the name of the test.  The test names should be insightful, and users 
should understand the behavior and expectation of the test by just glancing at the name itself.

You can use the decorator @pytest.mark.skip to skip tests (in this casre the buggy tests).

Note that I've included some tests that are intended to fail.  This is just done to illustrate what failures look like.
'''

import pytest
import sys
sys.path.append("..")
from src.Point import *

# test fixtures are used to create objects with the same name as the fixture function
@pytest.fixture
def pointUnderTest():
    return Point(3,4)   # creates an object reference: pointUnderTest

def test_WeCanDisplayAPoint(pointUnderTest):
    """test we can display coordinates of fixture object: pointUnderTest"""
    assert "3,4" == pointUnderTest.display()

def test_MovePointBy5inXand2inY(pointUnderTest):
    """move fixture by (5,2)"""
    pointUnderTest.moveBy(5, 2)
    assert "8,6" == pointUnderTest.display()
    
def test_MovePointBy7inXand12inY(pointUnderTest):
    """move fixture by (7,12)"""
    pointUnderTest.moveBy(7, 12)
    assert "10,16" == pointUnderTest.display()

@pytest.mark.skip    
@pytest.mark.intended_to_fail
def test_MoveByBy5inXand2inYusingBuggyRoutine(pointUnderTest):
    """move fixture by (5,2)"""
    pointUnderTest.buggyMoveBy(5, 2)
    assert "8,7" == pointUnderTest.display()
    
def test_DistanceIsFromOriginIs5(pointUnderTest):
    """distance of fixture from origin is 5"""
    assert 5 == pointUnderTest.get_distance()

@pytest.mark.skip    
@pytest.mark.intended_to_fail
def test_DistanceIsFromOriginIs5usingBuggyRoutine(pointUnderTest):
    """distance of fixture from origin is 5"""
    assert 5 == pointUnderTest.buggy_get_distance()

