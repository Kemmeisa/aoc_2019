#!/usr/bin/env python3

import sys


def check_adjacent(s):
    count = 1
    prev = s[0]
    for i in range(1, len(s)):
        if s[i] == prev:
            count += 1
        else:
            prev = s[i]
            if count == 2:
                break
            elif count > 2:
                count = 1
    return count == 2


def check_valid(val):
    s = str(val)
    if len(s) != 6:
        return False
    if s != ''.join(sorted(s)):
        return False
    return check_adjacent(s)


def run(lower, upper):
    count = 0
    for i in range(lower, upper + 1):
        b = check_valid(i)
        if b:
            count += 1
    return count


if __name__ == '__main__':
    lower = int(sys.stdin.readline())
    upper = int(sys.stdin.readline())
    print(run(lower, upper))

