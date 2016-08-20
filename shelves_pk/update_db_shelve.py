#!/usr/bin/env python
# encoding: utf-8

"""
@author: mx
@software: PyCharm
@file: update_db_shelve.py
@time: 16/8/21 00:58
"""
from  initdata import tom
import shelve

db = shelve.open('people-shelve')
sue = db['sue']
sue['pay'] *= 1.50
db['sue'] = sue
db['tom'] = tom
db.close()
