# ANSI colors
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
bar = "█"*30

import unittest


class ColorResult(unittest.TextTestResult):

    def addSuccess(self, test):
        super().addSuccess(test)
        print(f"{GREEN}{bar}{RESET}:{test}")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        print(f"{RED}{bar}{RESET}:{test}")

    def addError(self, test, err):
        super().addError(test, err)
        print(f"{RED}{bar}{RESET}:{test}")

class ColorRunner(unittest.TextTestRunner):
    resultclass = ColorResult



