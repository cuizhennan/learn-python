#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by czn on 2017/4/16

__metaclas__ = type


class Person:
    def __init__(self, name, lang="golang", website="www.google.com"):
        self.name = name
        self.lang = lang
        self.website = website
        print self
        print type(self)
        pass

    def getName(self):
        return self.name
        pass


if __name__ == '__main__':
    laoqi = Person("czn")
    print "laoqi.name", laoqi.name
    info = Person("czn", lang="python", website="monkeycoding.xyz")
    print "info.name", info.name
    print "info.lang", info.lang
    print "info.website", info.website

    girl = Person("MX")
    print girl.getName()
    pass
