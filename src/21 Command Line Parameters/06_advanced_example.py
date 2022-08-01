'''
Advanced Example
================

This is a more complicated example that sums several parameters and stores the answer in a logfile
specified by --log (or stdout if this option is missing).
'''

import argparse, sys, os

def setupParser():
    parser = argparse.ArgumentParser(
            description='sum the integers at the command line', exit_on_error=False)
    parser.add_argument('integers', metavar='int', nargs='+', type=int, help='integers to be summed')
    parser.add_argument(
        '--log', default=sys.stdout, type=argparse.FileType('w'),
        help='the file where the sum should be written')
    return parser

def doParse(text):
    try:
        print(f"\nparsing: {text}")
        args = parser.parse_args(text.split())
        fileName = args.log.buffer.name
        print(f"writing to {fileName} ...")
        args.log.write(f'sum of args = {sum(args.integers)}\n')
        if not args.log == sys.stdout: 
            args.log.close()
            cmd = f"cat {fileName}"
            print(f"executing: '{cmd}'")
            os.system(cmd)
        print("=================")
    except SystemExit as e: pass

parser = setupParser()
doParse("2 5 7 9 11")
doParse("--log logfile.txt 2 4 6 8 10 12 14 16 18 20")
doParse("--help")

