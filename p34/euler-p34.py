#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: set ts=4 noet ft=python:
#

'''
// Problem 34
//
//    Published on Friday, 3rd January 2003, 06:00 pm; Solved by 50376
//
//    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
//
//    Find the sum of all numbers which are equal to the sum of the factorial
//    of their digits.
//
//    Note: as 1! = 1 and 2! = 2 are not sums they are not included.
//
'''

df = {}

def fact(n):
    f = None
    if n-1 in df:
        f = n * df[n-1]
        return f
    else:
        f = 1
        for i in xrange(1, n+1):
            f *= i

    df[n] = f
    return f

def main():
    ss = 0
    for n in xrange(10, 1000000):
        fsum = 0

        for c in str(n):
            fr = fact(int(c))
            if fr > n:
                break
            fsum += fr

        if fsum == n:
            ss += n
            print n

    print ">> %s"  % ss

main()
