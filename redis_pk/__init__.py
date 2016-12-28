#!/usr/bin/env python
# encoding: utf-8

"""
@author: mx
@software: PyCharm
@file: __init__.py.py
@time: 16/12/28 14:35
"""



def somefunction(b, str):
    while b < 10:
        print(b)
        b += 1
        print('------------')
        print(str.strip())
        print(str.__len__())
        print('------------')


somefunction(1, ' c z n ')
