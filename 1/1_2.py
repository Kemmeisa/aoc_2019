#!/usr/bin/env python3

import math
import sys


def calculate_fuel(mass):
    fuel = math.floor(mass / 3) - 2
    if fuel <= 0:
        return 0
    return fuel + calculate_fuel(fuel)


if __name__ == '__main__':
    sum = 0
    for line in sys.stdin.readlines():
        sum += calculate_fuel(int(line))
    sys.stdout.write(str(sum))