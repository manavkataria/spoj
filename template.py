#!/usr/bin/env python

"""
SPOJ Problem #1: Life, the Universe, and Everything
Problem Code: TEST

Designed as a reusable template for all programs
"""

import logging

DEBUG = False

def process(N, data):
    for i in range(0,N):
        if (data[i] != 42):
            print(data[i])
        else:
            return

def read_inputs():
    data = []
    N = 0

    N = input()
    logging.debug('N: %d', N)

    for i in range(0,N):
        logging.debug('i: %d', i)

        x = input()

        if (x): data.append(x)
        else: pass

    return [N, data]

def setup_logging():
    global DEBUG
    if (DEBUG):
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    else:
        logging.basicConfig(format='%(message)s', level=logging.INFO)

def main():
    setup_logging()
    [N, data] = read_inputs()
    process(N, data)

if __name__ == "__main__":
    main()
