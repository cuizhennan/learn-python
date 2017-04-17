#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by czn on 2017/4/17

class Person:

    def speak(self):
        print "I love you"
        pass

    def setHeight(self):
        print "The height is: 1.60m"
        pass

    def breast(self, n):
        print "My breast is:", n
        pass


class Girl(Person):
    def setHeight(self):
        print "The height is:1.70m"
        pass


if __name__ == '__main__':
    cang = Girl()
    cang.setHeight()
    cang.speak()
    cang.breast(90)
    pass
