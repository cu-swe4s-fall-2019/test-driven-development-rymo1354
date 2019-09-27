import sys
import math


def list_mean(L):
    """
    computes the mean of a list of numbers

    Arguments
    _________
    L : list of ints or floats
        calculate mean of this list

    Returns
    _______
    mean : float
    """
    try:

        s = 0
        for v in L:
            s += v
        return s / len(L)

    except TypeError:
        if type(L) == str:
            raise TypeError('Cannot input string as list')
            sys.exit(1)

        if L is None:
            raise TypeError('Cannot input None as list')
            sys.exit(1)

        if type(L) == int:
            raise TypeError('Cannot input integer as list')
            sys.exit(1)

        if type(L) == float:
            raise TypeError('Cannot input float as list')
            sys.exit(1)

        if type(L) == bool:
            raise TypeError('Cannot input boolean as list')
            sys.exit(1)

        if any(isinstance(x, str) or type(x) == bool
               or isinstance(x, list) or x is None for x in L):
            raise TypeError('Bad Value')
            sys.exit(1)

    except ZeroDivisionError:
        if L == []:
            raise ZeroDivisionError('Array cannot be empty')
            sys.exit(1)

    except ValueError:
        raise ValueError('Unexpected value in array')
        sys.exit(1)


def list_stdev(L):
    """
    computes the stdev of a list of numbers

    Arguments
    _________
    L : list of ints or floats
        calculate mean of this list

    Returns
    _______
    stdev : float
    """

    try:
        s = 0
        for v in L:
            s += v
        return math.sqrt(sum([((s/len(L))-x)**2 for x in L]) / len(L))

    except TypeError:
        if type(L) == str:
            raise TypeError('Cannot input string as list')
            sys.exit(1)

        if L is None:
            raise TypeError('Cannot input None as list')
            sys.exit(1)

        if type(L) == int:
            raise TypeError('Cannot input integer as list')
            sys.exit(1)

        if type(L) == float:
            raise TypeError('Cannot input float as list')
            sys.exit(1)

        if type(L) == bool:
            raise TypeError('Cannot input boolean as list')
            sys.exit(1)

        if any(isinstance(x, str) or type(x) == bool
               or isinstance(x, list) or x is None for x in L):
            raise TypeError('Bad Value')
            sys.exit(1)

    except ZeroDivisionError:
        if L == []:
            raise ZeroDivisionError('Array cannot be empty')
            sys.exit(1)
