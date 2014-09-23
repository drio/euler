#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: set ts=4 noet ft=python:
#

'''
// Problem 32
//
//    Published on Friday, 6th December 2002, 06:00 pm; Solved by 36776
//
//    We shall say that an n-digit number is pandigital if it makes use of
//    all the digits 1 to n exactly once; for example, the 5-digit number,
//    15234, is 1 through 5 pandigital.
//
//    The product 7254 is unusual, as the identity, 39 × 186 = 7254,
//    containing multiplicand, multiplier, and product is 1 through 9
//    pandigital.
//
//    Find the sum of all products whose multiplicand/multiplier/product
//    identity can be written as a 1 through 9 pandigital.
//    HINT: Some products can be obtained in more than one way so be sure to
//    only include it once in your sum.
//
'''

def is_pandigital(a, b, m):
    s = set([])
    for d_str in str(a), str(b), str(m):
        for c in d_str:
            if c == '0' or c in s:
                return False
            s.add(c)
    return True

s = set([])
for a in range(1, 1000):
    for b in range(1, 10000):
        len_ab = len(str(a)) + len(str(b))
        m = a * b
        if (len_ab + len(str(m))) != 9:
            continue
        if is_pandigital(a, b, m):
            s.add(m)

print sum(s)
