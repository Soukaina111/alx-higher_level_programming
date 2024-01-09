#!/usr/bin/python3
"""Pascal's Triangle function Module"""


def pascal_triangle(n):
    """ Pascal's Triangle of width n
    """
    if n <= 0:
        return []

    trgls = [[1]]
    while len(trgls) != n:
        tris = trgls[-1]
        ptm = [1]
        for j in range(len(tris) - 1):
            ptm.append(tris[j] + tris[j + 1])
        ptm.append(1)
        trgls.append(ptm)
    return trgls
