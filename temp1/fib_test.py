#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by czn on 2017/4/16

def fibs(n):
    """
    This is a Fibonacci requence.
    """

    result = [0, 1]
    for i in range(n - 2):
        result.append(result[-2] + result[-1])
    return result


def fib(n):
    """
    This is Fibonacci by Recursion
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


meno = {0: 0, 1: 1}


def fibm(n):
    if not n in meno:
        meno[n] = fib(n - 1) + fib(n - 2)
    return meno[n]


if __name__ == '__main__':
    print fibs(10)
    print fibm(10)
    lst = fib(10)
    print lst
    pass
