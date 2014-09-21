#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: set ts=4 noet ft=python:
#
import sys

'''
// Problem 31
//
//    Published on Friday, 22nd November 2002, 06:00 pm; Solved by 42670
//
//    In England the currency is made up of pound, £, and pence, p, and there
//    are eight coins in general circulation:
//
//      1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
//
//    It is possible to make £2 in the following way:
//
//      1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
//
//    How many different ways can £2 be made using any number of coins?
//
'''

coins = [ 1, 2, 5, 10, 20, 50, 100, 200 ]
target = 200
#coins = [1, 3, 5]
#target = 7

# x: coin, y: target
# m[y,x] = number of ways to return target with up to that number of coins
matrix = {}

for y in range(1, target + 1): # only using 1st coin
    matrix[y, 0] = coins[0]
for x in range(0, len(coins)): # target 0
    matrix[0, x] = 1

for y in range(1, target + 1):
    print y, ":", 1,
    for x in range(1, len(coins)):
        if coins[x] > y: # I can't use that coin
            matrix[y,x] = matrix[y, x-1]
        else: # I can use that coin so the number of ways to form the target is:
              # the number of ways without that coin plus ...
              # the number of ways once I have used that coin (target - coin)
            matrix[y,x] = matrix[y, x-1] + matrix[y - coins[x], x]
        print matrix[y,x],
    print

