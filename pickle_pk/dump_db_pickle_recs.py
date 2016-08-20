#!/usr/bin/env python
# encoding: utf-8

"""
@author: mx
@software: PyCharm
@file: dump_db_pickle_recs.py
@time: 16/8/21 00:37
"""
import pickle,glob
for filename in glob.glob('*.pkl'):
    recfile = open(filename,'rb')
    record = pickle.load(recfile)
    print(filename,'=>\n',record)

suefile = open('sue.pkl','rb')
print(pickle.load(suefile)['name'])