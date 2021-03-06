#!/usr/bin/python3
"""
    Method that determines if all the boxes can be opened.
"""


def join(T, R):
    res = []
    for e in R:
        res += T[e]
    return res


def canUnlockAll(boxes):
    """
        Return True if ALL boxes can be opened, else return False.
    """
    unlocked_boxes_index = [0]
    index = 0
    total = list(set(boxes[0]) | {0})
    added = True
    while added:
        added = False
        for j in join(boxes, total[index:]):
            if j not in total:
                total.append(j)
                index += 1
                added = True

    return len(total) == len(boxes)