#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: set ts=4 noet ft=python:
#

'''
// Problem 27
//
//    Published on Friday, 27th September 2002, 06:00 pm; Solved by 45018
//
//    Euler discovered the remarkable quadratic formula:
//
//    n² + n + 41
//
//    It turns out that the formula will produce 40 primes for the
//    consecutive values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 =
//    40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41
//    + 41 is clearly divisible by 41.
//
//    The incredible formula  n² - 79n + 1601 was discovered, which produces
//    80 primes for the consecutive values n = 0 to 79. The product of the
//    coefficients, -79 and 1601, is -126479.
//
//    Considering quadratics of the form:
//
//      n² + an + b, where |a| < 1000 and |b| < 1000
//
//    where |n| is the modulus/absolute value of n
//    e.g. |11| = 11 and |-4| = 4
//
//    Find the product of the coefficients, a and b, for the quadratic
//    expression that produces the maximum number of primes for consecutive
//    values of n, starting with n = 0.
//
'''

import sys
from drdmath import is_prime, abs_val

def create_form(a, b):
    def q_form(n):
        return (n**2) + (a*n) + b
    return q_form

def max_conseq(qf, max_n=50, best=-1):
    cons_primes = 0
    for n in range(0, max_n + 1, 1):
        if not is_prime(abs_val(qf(n))):
            if cons_primes > best:
                best = cons_primes

            if (max_n - n) <= best:
                break
            else:
                cons_primes = 0
                continue
        cons_primes += 1

    if cons_primes > best:
        best = cons_primes

    return best

def run():
    r_min, r_max = -1000, 1000
    best = [None, None, -1] # coef a, coef b, n (# of consecutive primes)
    for a in range(r_min, r_max+1, 1):
        for b in range(r_min, r_max+1, 1):
            p_best = max_conseq(create_form(a, b), 1000, best[2])
            if p_best > best[2]:
                best = [a, b, p_best]

    print best

run()
