#!/usr/bin/env python
# encoding: utf-8

"""
@author: mx
@software: PyCharm
@file: make_db_pickle.py
@time: 16/8/21 00:21
"""

from initdata import db
import pickle

dbfile = open('people-pickle','wb')
pickle.dump(db,dbfile)
dbfile.close()