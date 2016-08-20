#!/usr/bin/env python
# encoding: utf-8

"""
@author: mx
@software: PyCharm
@file: dump_db_pickle.py
@time: 16/8/21 00:24
"""
import pickle
dbfile = open('people-pickle','rb')
db = pickle.load(dbfile)
for key in db:
    print(key,'=>\n',db[key])
print(db['sue']['name'])