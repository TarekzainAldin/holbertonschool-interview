#!/usr/bin/python3
"""Function to rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """rotation 2D Matrix"""
    rotated = list(map(list, zip(*matrix[::-1])))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = rotated[i][j]
