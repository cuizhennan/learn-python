#!/usr/bin/env python
# encoding: utf-8

"""
@author: mx
@software: PyCharm
@file: test.py
@time: 16/12/28 14:55
"""

import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

r.set('foo', '1231')

print((r.get('foo')).decode('ascii'))

# pipe = rs.pipeline()
# pipe.set('foo','bar')
# pipe.get('bing')

# print(pipe.execute())
