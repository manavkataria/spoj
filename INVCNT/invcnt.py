#!/usr/bin/env python

"""
SPOJ Problem #6256: Inversion Count
Problem Code: INVCNT

Designed as a reusable template for all programs
"""

import logging

DEBUG = False

def countInvMerge(array, start, middle, end):
    logging.debug('Merge: start %d, middle %d, end %d', start, middle, end)
    logging.debug(array[start:end+1])

    tmpArray = []

    i = start
    j = middle+1

    invcount=0

    while(i<=middle and j <= end):
        logging.debug('Merge: (%d <= %d)?', array[i], array[j])

        if (array[i] <= array[j]):
            tmpArray.append(array[i])
            i+=1
        else:
            tmpArray.append(array[j])
            j+=1
            invcount+=(middle-i+1)

    #copy left array left-over into tmpArray
    while(i<=middle):
        tmpArray.append(array[i])
        i+=1

    #Copy tmpArray back to array
    for i in range(start,start+len(tmpArray)):
        array[i] = tmpArray[i-start]

    return invcount


def countInvSplit(array, start, end):
    logging.debug('Split: start %d, end %d', start, end)
    logging.debug(array[start:end+1])

    middle = (start+end)/2

    if ((end-start+1) <= 1): return 0
    else:
        cl = countInvSplit(array, start, middle)
        cr = countInvSplit(array, middle+1, end)
        cm = countInvMerge(array, start, middle, end)

        logging.debug('cr(%d), cl(%d), cm(%d), sum(%d)', cr, cl, cm, cr+cl+cm)

        return (cl+cr+cm)

def process(N, data):
    global DEBUG
    DEBUG = True

    for i in range(0,N):
        logging.debug('Processing Array:')
        logging.debug(data[i])

        result = countInvSplit(data[i][1], 0, data[i][0]-1)

        logging.info(result)


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
