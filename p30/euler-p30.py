#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: set ts=4 noet ft=python:
#

'''
// Problem 30
//
//    Published on Friday, 8th November 2002, 06:00 pm; Solved by 57525
//
//    Surprisingly there are only three numbers that can be written as the
//    sum of fourth powers of their digits:
//
//      1634 = 1^4 + 6^4 + 3^4 + 4^4
//      8208 = 8^4 + 2^4 + 0^4 + 8^4
//      9474 = 9^4 + 4^4 + 7^4 + 4^4
//
//    As 1 = 1^4 is not a sum it is not included.
//
//    The sum of these numbers is 1634 + 8208 + 9474 = 19316.
//
//    Find the sum of all the numbers that can be written as the sum of fifth
//    powers of their digits.
//
'''

pof = 5
l = []
for d in range(2, 1000000):
    _sum = 0
    sd   = str(d)
    for i in range(0, len(sd)):
        _sum += int(sd[i])**pof
        if _sum > d: break
    if _sum == d:
        print d
        l.append(d)

print sum(l)
