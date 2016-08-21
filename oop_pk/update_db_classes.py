#!/usr/bin/env python
# encoding: utf-8

"""
@author: mx
@software: PyCharm
@file: update_db_classes.py
@time: 16/8/21 10:43
"""
import shelve

db = shelve.open("class-shelve")
sue = db['sue']
sue.giveRaise(.25)
db['sue'] = sue

tom = db['tom']
tom.giveRaise(.20)
db['tom'] = tom
db.close()
