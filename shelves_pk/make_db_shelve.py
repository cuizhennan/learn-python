#!/usr/bin/env python
# encoding: utf-8

"""
@author: mx
@software: PyCharm
@file: make_db_shelve.py
@time: 16/8/21 00:54
"""
from initdata import bob, sue
import shelve

db = shelve.open('people-shelve')
db['bob'] = bob
db['sue'] = sue
db.close()

