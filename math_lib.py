import sys
import math


def list_mean(L):

    try:
        s = 0
        for v in L:
            s += v
        return s / len(L)

    except TypeError:
        if type(L) == str:
            raise TypeError('Cannot input string as list')
            sys.exit(1)

        if type(L) is None:
            raise TypeError('Cannot input None as list')
            return None


def list_stdev(L):

    try:
        s = 0
        for v in L:
            s += v
        return math.sqrt(sum([((s/len(L))-x)**2 for x in L]) / len(L))

    except TypeError:
        if type(L) == str:
            raise TypeError('Cannot input string as list')
            sys.exit(1)

        if type(L) is None:
            raise TypeError('Cannot input None as list')
            return None
