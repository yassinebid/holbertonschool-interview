#!/usr/bin/python3
"""
    Box opener method.
"""


def canUnlockAll(boxes):
    key_list = [0]

    for key in key_list:
        for src in boxes[key]:
            if src not in key_list and src < len(boxes):
                key_list.append(src)
    for index in range(len(boxes)):
        if index not in key_list:
            return False
    return True
