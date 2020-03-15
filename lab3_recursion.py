#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 11:46:29 2020

@author: herrylo
"""
# http://inst.eecs.berkeley.edu/~cs61a/fa17/lab/lab03/#q3

# 问题1 AB + C

def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    if(b == 0 ):
        return c;
    else :
        return a + ab_plus_c(a, b-1 ,c);

# 问题2 GCD 计算两个数的最大公约数

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    if(a%b == 0):
        return b;
    return gcd(b, a%b);

#问题3 Hailstone

count = 0
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(int(n));
    if(n == 1):
        return count;
    if(n%2 == 0):
        return hailstone(n/2);
    else:
        return hailstone(n*3+1);
