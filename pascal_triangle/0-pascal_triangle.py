#!/usr/bin/python3
"""
0-pascal_triangle.py
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the n-th row.

    Args:
        n (int): Number of rows of the triangle to generate.

    Returns:
        list of lists: Pascal's triangle represented as a list of rows.
                       Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]
        for j in range(len(prev_row) - 1):
            row.append(prev_row[j] + prev_row[j + 1])
        row.append(1)
        triangle.append(row)

    return triangle
