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

    while True:
        x = input()

        if (x!=42): data.append(x)
        else: break

    return [len(data), data]

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