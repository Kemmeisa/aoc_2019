#!/usr/bin/env python3

import math
import sys


if __name__ == '__main__':
    sum = 0
    for mass in sys.stdin.readlines():
        sum += math.floor(int(mass) / 3) - 2
    print(sum)
