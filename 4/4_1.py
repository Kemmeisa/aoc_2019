#!/usr/bin/env python3

import sys


def check_valid(val):
    s = str(val)
    if len(s) != 6:
        return False
    if s != ''.join(sorted(s)):
        return False
    for i in range(0, len(s) - 1):
        if s[i] == s[i + 1]:
            return 1
    return 0


def run(lower, upper):
    count = 0
    for i in range(lower, upper + 1):
        count += check_valid(i)
    return count


if __name__ == '__main__':
    lower = int(sys.stdin.readline())
    upper = int(sys.stdin.readline())
    print(run(lower, upper))

