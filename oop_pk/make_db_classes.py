#!/usr/bin/env python
# encoding: utf-8

"""
@author: mx
@software: PyCharm
@file: make_db_classes.py
@time: 16/8/21 10:36
"""
import shelve
from person_alternative import Person, Manager

bob = Person('Bob Smith', 42, 30000, 'software')
sue = Person('Sue Jones', 45, 40000, 'hardware')
tom = Manager('Tom Doe', 50, 50000)

db = shelve.open('class-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()
