#!/usr/bin/env python3

import sys


def process_input(wire, turns):
    x = 0
    y = 0
    for i in turns:
        if i[0] == 'L':
            for j in range(int(i[1:])):
                x -= 1
                wire.add((x, y))
        elif i[0] == 'R':
            for j in range(int(i[1:])):
                x += 1
                wire.add((x, y))
        elif i[0] == 'U':
            for j in range(int(i[1:])):
                y += 1
                wire.add((x, y))
        elif i[0] == 'D':
            for j in range(int(i[1:])):
                y -= 1
                wire.add((x, y))


if __name__ == '__main__':
    wires = [set(), set()]
    inputs = [None, None]

    for i in range(2):
        inputs[i] = sys.stdin.readline().split(",")
        process_input(wires[i], inputs[i])

    intersect = wires[0].intersection(wires[1])
    print(min([abs(x[0]) + abs(x[1]) for x in intersect]))
