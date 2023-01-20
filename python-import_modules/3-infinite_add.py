#!/usr/bin/python3
import sys

if __name__ == '__main__':
    av = sys.argv
    length_argv = len(av)
    sum = 0

    if length_argv > 1:
        for i in range(1, length_argv):
            sum += int(av[i])

    print(sum)