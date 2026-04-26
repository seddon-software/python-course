'''
Logging
=======

Create a set of 100 pairs of integers taken from the range -5 to +5.
Loop through the set performing a division between the number in each pair.  Because 0 is part of the range, some of the divisions
will fail with a "division by zero" exception.

Log each successful division as INFO and each exception as ERROR.  Include the numbers taking part in the division in the log.
At the end of your program open the log file and print its contents.
'''

import logging, random

LOG_FILENAME = 'logs/Solution1.log'

# Configure logging
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

def main():
    logging.info("Program started")

    numbers = [(random.randint(-5, 5),random.randint(-5, 5)) for x in range(100) for y in range(100)]
    for n1, n2 in numbers:
        try:
            result = n1/n2
            logging.info(f"{n1}/{n2} = {result:.2f}")
        except Exception as e:
            logging.error(f"*** {n1}/{n2}: {e}")

    logging.info("Program finished")

    with open(f"{LOG_FILENAME}", "r") as f:
        content = f.read()
    print(content)

if __name__ == "__main__":
    main()