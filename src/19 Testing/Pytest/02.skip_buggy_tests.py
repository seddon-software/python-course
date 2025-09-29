'''
skip some tests; i.e. those marked @pytest.mark.skip
'''

import os
os.system("pytest mytests/test_part_of_Point_class.py --no-header")
