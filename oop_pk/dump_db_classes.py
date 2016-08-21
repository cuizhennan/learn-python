#!/usr/bin/env python
# encoding: utf-8

"""
@author: mx
@software: PyCharm
@file: dump_db_classes.py
@time: 16/8/21 10:40
"""
import shelve

db = shelve.open("class-shelve")
for key in db:
    print(key, '=>\n', db[key].name, db[key].pay)

bob = db['bob']
print(bob.lastName())
print(db['tom'].lastName())
