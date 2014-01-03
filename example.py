#!/usr/bin/env python
#coding=utf-8

import json
from corrector import Corrector

if __name__ == '__main__':
    corrector = Corrector('example.txt')
    print 'words:', json.dumps(corrector.nwords, ensure_ascii=False, indent=4)

    print '\n'

    for word in [u'刘弱英', u'陈牵强', u'刘若华', u'hel', u'helle']:
        print 'word:', word
        print 'corrected:', corrector.correct(word)
        print 'possibilities:', json.dumps(corrector.possibilities(word),
                                           ensure_ascii=False, indent=4)
        print '\n'
