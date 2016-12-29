#!/usr/bin/env python
# encoding: utf-8

"""
@author: mx
@software: PyCharm
@file: Calulator.py
@time: 16/12/28 16:15
"""

name = "whole global name"


class Calulator(object):
    # define class to simulate a simple calculator

    def __init__(self, newName):
        # start with zero
        self.current = 0
        self.name = newName

    def add(self, amount):
        # add number to current
        self.current += amount

    def getCurrent(self):
        return self.current

    def sayYourName(self):
        print('My name is %s' % self.name)


def selfAndInitDemo():
    persionInstance = Calulator('Gavin.')
    persionInstance.sayYourName()


if __name__ == '__main__':
    selfAndInitDemo()
