'''
Help
====

You can ask for a help message with the optional parameter "-h" or "--help".  Recall the SystemExit handler
is only thee to stop vscode from exiting prematurely and is not required on a console.
'''

import argparse

# call this with -h or --help to see usage message
parser = argparse.ArgumentParser("-h", usage="this is the usage message", exit_on_error=False)
try:
    parser.parse_args("-h".split())
except SystemExit as e: pass

try:
    parser.parse_args("--help".split())
except SystemExit as e: pass

