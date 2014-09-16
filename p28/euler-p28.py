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

class Spiral(object):
    def __init__(self, size):
        self.size = size
        self.init_matrix()
        self.row, self.col = size/2, size/2
        self.moves_rd = 1
        self.moves_lu = 2
        self.val = 1

        matrix, val, row, col, size = self.matrix, self.val, self.row, self.col, self.size
        moves_rd, moves_lu = self.moves_rd, self.moves_lu
        check = self.check

    def init_matrix(self):
        self.matrix = []
        for row in range(0, self.size):
            self.matrix.append([0] * self.size)

    def check(self):
        if self.row >= self.size or self.col >= self.size or self.matrix[self.row][self.col] > 1:
            return False
        return True

    def build(self):
        self.matrix[self.row][self.col] = self.val
        while self.val < (self.size * self.size):
            for _ in range(0, self.moves_rd):
                self.col += 1
                self.val += 1
                if not self.check(): break
                self.matrix[self.row][self.col] = self.val

            for _ in range(0, self.moves_rd):
                self.row += 1
                self.val += 1
                if not self.check(): break
                self.matrix[self.row][self.col] = self.val

            for _ in range(0, self.moves_lu):
                self.col -= 1
                self.val += 1
                if not self.check(): break
                self.matrix[self.row][self.col] = self.val

            for _ in range(0, self.moves_lu):
                self.row -= 1
                self.val += 1
                if not self.check(): break
                self.matrix[self.row][self.col] = self.val

            self.moves_rd += 2
            self.moves_lu += 2

        return self

    def dump(self):
        for r in range(0, self.size):
            print self.matrix[r]

Spiral(5).build().dump()

