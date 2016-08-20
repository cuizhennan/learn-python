#!/usr/bin/env python
# encoding: utf-8

"""
@author: mx
@software: PyCharm
@file: update_db_pickle_recs.py
@time: 16/8/21 00:41
"""
import pickle

suefile = open('sue.pkl', 'rb')
sue = pickle.load(suefile)
suefile.close()

sue['pay'] *= 1.10
suefile = open('sue.pkl', 'wb')
pickle.dump(sue, suefile)
suefile.close()
