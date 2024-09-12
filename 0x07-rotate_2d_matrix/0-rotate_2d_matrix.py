#!/usr/bin/python3
"""
2d Rotation
"""
def rotate_2d_matrix(mat):
    """ Transpose and swap """

    for i in range(len(mat)):
        for j in range(i, len(mat)):

            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    for i in range(len(mat)):
        mat[i].reverse()
