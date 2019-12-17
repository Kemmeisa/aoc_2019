#!/usr/bin/env python3

import sys


def process_input(wire, turns, d_map):
    x = 0
    y = 0
    traveled = 0
    for i in turns:
        if i[0] == 'L':
            for j in range(int(i[1:])):
                x -= 1
                traveled += 1
                p = (x, y)
                wire.add(p)
                if p not in d_map:
                    d_map[p] = traveled
        elif i[0] == 'R':
            for j in range(int(i[1:])):
                traveled += 1
                x += 1
                p = (x, y)
                wire.add(p)
                if p not in d_map:
                    d_map[p] = traveled
        elif i[0] == 'U':
            for j in range(int(i[1:])):
                traveled += 1
                y += 1
                p = (x, y)
                wire.add(p)
                if p not in d_map:
                    d_map[p] = traveled
        elif i[0] == 'D':
            for j in range(int(i[1:])):
                traveled += 1
                y -= 1
                p = (x, y)
                wire.add(p)
                if p not in d_map:
                    d_map[p] = traveled


if __name__ == '__main__':
    wires = [set(), set()]
    dist_maps = [dict(), dict()]

    for i in range(2):
        turns = sys.stdin.readline().split(",")
        process_input(wires[i], turns, dist_maps[i])

    intersect = wires[0].intersection(wires[1])

    print(min([dist_maps[0][x] + dist_maps[1][x] for x in intersect]))
