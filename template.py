#!/usr/bin/env python

"""
SPOJ Problem #6256: Inversion Count
Problem Code: INVCNT

Designed as a reusable template for all programs
"""

import logging

DEBUG = True

def process(N, data):
    for i in range(0,N):
        if (data[i] != 42):
            print(data[i])
        else:
            return

def read_array(n):
    arr = []
    element = 0
    for i in range(0,n):
        element = input()
        logging.debug('arr[%d]=(%d)', i, element)
        if (element): arr.append(element)
        else: pass

    return [n, arr]

def read_inputs():
    data = []
    x = 0
    N = 0

    N = input()
    logging.debug('N Arrays: %d', N)

    for i in range(0,N):
        logging.debug('i: %d', i)

        x = raw_input() #eat EOF caused by New Line
        x = input()
        logging.debug('x(%d) elements', x)

        if (x): data.append(read_array(x))
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
