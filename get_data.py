import sys


def read_stdin_col(col_num):

    if col_num is None:
        raise TypeError("No column provided")
        sys.exit(1)

    if not isinstance(col_num, int):
        raise TypeError("Invalid Column")

    stdin = sys.stdin.readlines()
    if len(stdin[0].rstrip().split(' ')) < col_num:
        raise IndexError('Column out of range')
    column = []

    for line in stdin:
        value = line.rstrip().split(' ')[col_num]
        column.append(value)

    return None
