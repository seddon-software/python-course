'''
In this example I've added 2 skip decorators to "test_Point_class.py" and changed its name to:
    test_Point_with_skips.py

The decorators are:
    @pytest.mark.skip
'''

import os

# os.system("pytest mytests/test_Point_with_skips.py")
os.system("pytest mytests/test_Point_with_skips.py --no-header")
