#!/usr/bin/env python
# encoding: utf-8

"""
@author: mx
@software: PyCharm
@file: Calulator.py
@time: 16/12/28 16:15
"""


class Calulator(object):
    # define class to simulate a simple calculator

    def __init__(self):
        # start with zero
        self.current = 0

    def add(self, amount):
        # add number to current
        self.current += amount

    def getCurrent(self):
        return self.current
