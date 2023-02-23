#!/usr/bin/python3
from sys import argv


def check(position, i, j, n):
    """
    Check if position[i, j] have any intersections
    with any of the previous queens
    position: list of cordination of queens
    [i, j]: position of the new queen
    n: nbr of queens
    """
    # print(position)
    for pos in position:
        all = generat(pos, n)
        if [i, j] in all:
            # print("{},{} => {}".format(i,j,all))
            return 0
    return 1


def generat(pos, n):
    """
    Given a cordination of a queen
    genearte all the possible movment
    in the board
    pos= [x, y]
    n: number of queens
    """
    all = []
    p0 = pos[0]
    p1 = pos[1]
    # print(pos)
    for i in range(n):
        if (p1 + i) < n:
            all.append([p0, p1 + i])
        if (p0 + i) < n:
            all.append([p0 + i, p1])
        if (p1 - i) >= 0:
            all.append([p0, p1 - i])
        if (p0 - i) >= 0:
            all.append([p0 - i, p1])
        if (p0 + i) < n and (p1 + i) < n:
            all.append([p0 + i, p1 + i])
        if (p0 - i) >= 0 and (p1 - i) >= 0:
            all.append([p0 - i, p1 - i])
        if (p0 + i) < n and (p1 - i) >= 0:
            all.append([p0 + i, p1 - i])
        if (p0 - i) >= 0 and (p1 + i) < n:
            all.append([p0 - i, p1 + i])
    # print(all)
    return (all)


def alter(array, position, count, result, y, z, n):

    """
    print("array:")
    for i in array:
        print(i, "\n")
    """
    # print("count={}".format(count))


if __name__ == "__main__":
    """
    Find all possible locations of queens
    in a n*n board
    Return the queens cordinations
    """
    if len(argv) < 1:
        print("Usage: nqueens N\n")
        exit(1)
    if int(argv[1]) < 4:
        print("N must be at least 4\n")
        exit(1)
    n = int(argv[1])

    array = [[0 for i in range(n)] for i in range(n)]
    position = []
    result = []

    for x in range(n):
        array[0][x] = 1
        position.append([0, x])
        count = 1

        # print("positions: {}".format(position))
        for i in range(1, n):
            for j in range(n):
                if (check(position, i, j, n)):
                    array[i][j] = 1
                    count += 1
                    position.append([i, j])

        if count == n:
            print([[i, j] for i in range(n) for j in range(n) if array[i][j] == 1])
        array = [[0 for i in range(n)] for i in range(n)]
        position = []
        result = []




