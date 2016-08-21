# !/usr/bin/env python3
# encoding: utf-8

"""
@author: mx
@software: PyCharm
@file: peopleinteract_update.py
@time: 16/8/21 11:07
"""
import shelve
from person_alternative import Person

fieldnames = ('name', 'age', 'job', 'pay')
db = shelve.open("class-shelve")
while True:
    key = input('\n Key => ')
    if not key: break
    if key in db:
        record = db[key]
    else:
        record = Person(name='?', age='?', job='?', pay="?")

    for field in fieldnames:
        currval = getattr(record, field)
        newtext = input('\t[%s]=%s\n\t\tnew?=>' % (field, currval))
        if newtext:
            setattr(record, field, newtext)
    db[key] = record
db.close()
