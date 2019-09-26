import sys


def read_stdin_col(col_num):

    if col_num is None:
        raise TypeError("No column provided")
        sys.exit(1)

    stdin = sys.stdin.readlines()

    column = []

    for line in stdin:
        value = line.rstrip().split(' ')[col_num]
        column.append(value)

    return None
