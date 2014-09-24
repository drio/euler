#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: set ts=4 noet ft=python:
#

'''
// Problem 33
//
//    Published on Friday, 20th December 2002, 06:00 pm; Solved by 37928
//
//    The fraction ^49/[98] is a curious fraction, as an inexperienced
//    mathematician in attempting to simplify it may incorrectly believe that
//    ^49/[98] = ^4/[8], which is correct, is obtained by cancelling the 9s.
//
//    We shall consider fractions like, ^30/[50] = ^3/[5], to be trivial
//    examples.
//
//    There are exactly four non-trivial examples of this type of fraction,
//    less than one in value, and containing two digits in the numerator and
//    denominator.
//
//    If the product of these four fractions is given in its lowest common
//    terms, find the value of the denominator.
//
'''

def curious(n, d):
    ns, ds = str(n), str(d)
    def check(i, j):
        if n < d and n != d and ds[i] != '0' and ns[i] == ds[j]:
            if (int(ns[j]) + 0.0) / int(ds[i]) == (n + 0.0) / d:
                return True
    if check(0, 1) or check(1, 0):
        return True
    return False

num , dem = 1, 1
for n in range(10, 100):
    for d in range(10, 100):
        if curious(n, d):
            num *= n
            dem *= d

print "%s/%d" % (num, dem)
