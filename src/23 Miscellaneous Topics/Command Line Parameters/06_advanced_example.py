import argparse, sys

# A more complicated example that sums several parameters and stores the answer in a logfile
# specified by --log (or stdout if this option is missing)

parser = argparse.ArgumentParser(
        description='sum the integers at the command line')
parser.add_argument(
    'integers', metavar='int', nargs='+', type=int,
    help='integers to be summed')
parser.add_argument(
    '--log', default=sys.stdout, type=argparse.FileType('w'),
    help='the file where the sum should be written')
args = parser.parse_args()
args.log.write('{0}\n'.format(sum(args.integers)))
args.log.close()

