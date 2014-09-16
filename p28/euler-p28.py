#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: set ts=4 noet ft=python:
#

'''
// Problem 28
//
//    Published on Friday, 11th October 2002, 06:00 pm; Solved by 59507
//
//    Starting with the number 1 and moving to the right in a clockwise
//    direction a 5 by 5 spiral is formed as follows:
//
//    21 22 23 24 25
//    20  7  8  9 10
//    19  6  1  2 11
//    18  5  4  3 12
//    17 16 15 14 13
//
//    It can be verified that the sum of the numbers on the diagonals is 101.
//
//    What is the sum of the numbers on the diagonals in a 1001 by 1001
//    spiral formed in the same way?
//
'''

size = 5

def init_matrix(size):
    matrix = []
    for row in range(0, size):
        matrix.append([0] * size)
    return matrix

def check(m, r, c):
    if r >= size or c >= size or m[r][c] > 1:
        return False
    return True

def main():
    matrix = init_matrix(size)
    matrix[size/2][size/2] = 1

    row, col = size/2, size/2
    moves_rd = 1
    moves_lu = 2
    val = 1
    while val < (size * size):
        for _ in range(0, moves_rd):
            col += 1
            val += 1
            if not check(matrix, row, col): break
            print row, col, val
            matrix[row][col] = val

        for _ in range(0, moves_rd):
            row += 1
            val += 1
            if not check(matrix, row, col): break
            print row, col, val
            matrix[row][col] = val

        for _ in range(0, moves_lu):
            col -= 1
            val += 1
            if not check(matrix, row, col): break
            print row, col, val
            matrix[row][col] = val

        for _ in range(0, moves_lu):
            row -= 1
            val += 1
            if not check(matrix, row, col): break
            print row, col, val
            matrix[row][col] = val

        moves_rd += 2
        moves_lu += 2

    for r in range(0, size):
        print matrix[r]

main()

