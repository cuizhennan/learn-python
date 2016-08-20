#!/usr/bin/env python
# encoding: utf-8

"""
@author: mx
@software: PyCharm
@file: dump_db_shelve.py
@time: 16/8/21 00:56
"""

import shelve

db = shelve.open('people-shelve')
for key in db:
    print(key,'=>\n',db[key])
print(db['sue']['name'])
db.close()
