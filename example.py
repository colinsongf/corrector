#!/usr/bin/env python
#coding=utf-8

from corrector import Corrector

if __name__ == '__main__':
    corrector = Corrector('example.txt')
    print corrector.correct(u'刘弱英')
    print corrector.correct(u'陈牵强')
    print corrector.correct(u'刘若华')
    print corrector.correct(u'hel')
    print corrector.correct(u'helle')
