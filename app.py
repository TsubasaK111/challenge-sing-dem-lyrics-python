import os
import subprocess

from threading import Timer

from decimal import Decimal
from fractions import Fraction

import logging

logging.basicConfig(filename='log.log',
                    level=logging.DEBUG,
                    format='%(levelname)s: %(message)s [%(asctime)s]',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

class PrintLine:
    def __init__(self,line):
        self.line = line
        # return line
    def pprint(self):
        print self.line

def sing(filename, beatsPerMinute):
        songLines = open(filename, "r").readlines()

        secondsPerBeat = Fraction(60,beatsPerMinute)
        time = 0

        for line in songLines:
            printLine = PrintLine(line)
            t = Timer(time, printLine.pprint)
            t.start()
            time += secondsPerBeat


# ============================================================================


# cwd = str(os.getcwd())
# lsResults = os.listdir(cwd)
#
# if "Bob Dylan - The Times They Are A-Changin'.md" in lsResults:
#     sing("Bob Dylan - The Times They Are A-Changin'.md", 100)
