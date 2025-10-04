'''
pytest will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories.
 
We can use the -m command line option to only run tests with a given mark.
In this test we will only run tests decorated with the mark "intended_to_fail", e.g.
    @pytest.mark.intended_to_fail
    def test_MoveByBy5inXand2inYusingBuggyRoutine(pointUnderTest):
        ...

'''

import os

# only run tests with a given mark
os.system("pytest -m intended_to_fail")

