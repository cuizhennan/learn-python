#!/usr/bin/env python
# encoding: utf-8

"""
@author: mx
@software: PyCharm
@file: manager.py
@time: 16/8/21 09:45
"""
from person_one import Person


class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')

    def giveRasise(self, percent, bonus=0.1):
        self.pay *= (1.0 + percent + bonus)


if __name__ == '__main__':
    tom = Manager('Tom Doe', 50, 5000)
    print(tom)
    tom.giveRasise(.20)
    print(tom.pay)
