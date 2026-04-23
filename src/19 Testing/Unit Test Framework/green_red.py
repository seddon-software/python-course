# ANSI colors
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

import unittest
class ColorResult(unittest.TextTestResult):

    def addSuccess(self, test):
        bar = "█"*30
        Pass = f"{bar}"
        print(f"{GREEN}{bar}{RESET}:{test}")

    def addFailure(self, test, err):
        bar = "█"*30
        Fail = f"{bar}"
        print(f"{RED}{bar}{RESET}:{test}")

    def addError(self, test, err):
        print(f"{RED}ERROR{RESET} {test}")

class ColorRunner(unittest.TextTestRunner):
    resultclass = ColorResult


