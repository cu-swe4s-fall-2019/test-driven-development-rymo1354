import matplotlib.pyplot as plt
import numpy as np
import math_lib
import matplotlib
matplotlib.use('Agg')


def boxplot(L, out_file_name="boxplot.png"):
    """
    makes boxplot and writes to file

    Arguments
    _________
    L: list or array of numbers (floats or integers)
       numbers that will be put into boxplot
    """
    if L is None:
        raise TypeError("Please supply a list")

    if not isinstance(L, (list, np.ndarray)):
        raise TypeError("Please supply a list")

    if len(L) == 0:
        raise IndexError("No values in list")

    list_types = [not isinstance(val, (float, int, np.float, np.int))
                  for val in L]

    if any(list_types):
        raise TypeError("List contains invalid type")

    if type(out_file_name) != str:
        raise TypeError("Not valid filename")

    else:
        fig = plt.figure(figsize=(3, 3), dpi=300)
        ax = fig.add_subplot(1, 1, 1)
        ax.title.set_text("Mean : "+str(math_lib.list_mean(L)) +
                          " St-Dev : "+str(math_lib.list_stdev(L)))
        ax.set_ylabel("Values")

        ax.boxplot(L)
    try:
        plt.savefig(out_file_name, bbox_inches='tight')
    except PermissionError:
        raise PermissionError("Check file permissions")
    except ValueError:
        raise ValueError("Incompatible file extension")


def histogram(L, out_file_name="histogram.png"):
    """
    makes histogram and writes to file
    Arguments
    ---------
    L: list or array of numbers (floats or integers)
       numbers that will be put into histogram
    """
    if L is None:
        raise TypeError("Please supply a list")

    if not isinstance(L, (list, np.ndarray)):
        raise TypeError("Please supply a list")

    if len(L) == 0:
        raise IndexError("No values in list")

    list_types = [not isinstance(val, (float, int, np.float, np.int))
                  for val in L]

    if any(list_types):
        raise TypeError("List contains invalid type")

    if type(out_file_name) != str:
        raise TypeError("Not valid filename")

    else:
        fig = plt.figure(figsize=(3, 3), dpi=300)
        ax = fig.add_subplot(1, 1, 1)
        ax.title.set_text("Mean : "+str(math_lib.list_mean(L)) +
                          " St-Dev : "+str(math_lib.list_stdev(L)))
        ax.set_ylabel("Values")
        ax.set_xlabel("Frequency")

        ax.hist(L)
    try:
        plt.savefig(out_file_name, bbox_inches='tight')
    except PermissionError:
        raise PermissionError("Check file permissions")
    except ValueError:
        raise ValueError("Incompatible file extension")


def combo(L, out_file_name="histogram_boxplot_combo.png"):
    """
    makes histogram and boxplot combo and writes to file
    Arguments
    ---------
    L: list or array of numbers (floats or integers)
       numbers that will be put into histogram and boxplot
    """
    if L is None:
        raise TypeError("Please supply a list")

    if not isinstance(L, (list, np.ndarray)):
        raise TypeError("Please supply a list")

    if len(L) == 0:
        raise IndexError("No values in list")

    list_types = [not isinstance(val, (float, int, np.float, np.int))
                  for val in L]

    if any(list_types):
        raise TypeError("List contains invalid type")

    if type(out_file_name) != str:
        raise TypeError("Not valid filename")

    else:
        fig = plt.figure(figsize=(3, 3), dpi=300)
        # Histogram
        ax1 = fig.add_subplot(2, 1, 1)
        ax1.title.set_text("Mean : "+str(math_lib.list_mean(L)) +
                           " St-Dev : "+str(math_lib.list_stdev(L)))
        ax1.set_ylabel("Values")
        ax1.set_xlabel("Frequency")

        ax1.hist(L)
        # Boxplot
        ax2 = fig.add_subplot(2, 1, 2)
        ax2.set_ylabel("Values")
        ax2.boxplot(L)
    try:
        plt.savefig(out_file_name, bbox_inches='tight')
    except PermissionError:
        raise PermissionError("Check file permissions")
    except ValueError:
        raise ValueError("Incompatible file extension")
