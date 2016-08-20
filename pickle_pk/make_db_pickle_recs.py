#!/usr/bin/env python
# encoding: utf-8

"""
@author: mx
@software: PyCharm
@file: make_db_pickle_recs.py
@time: 16/8/21 00:33
"""
from initdata import bob, sue, tom
import pickle
for (key,record) in [('bob',bob),('tom',tom),('sue',sue)]:
    recfile = open(key+'.pkl','wb')
    pickle.dump(record,recfile)
    recfile.close()
