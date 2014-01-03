.. corrector documentation master file, created by
   sphinx-quickstart on Thu Jan  2 23:01:37 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to corrector's documentation!
=====================================


.. toctree::
   :maxdepth: 2


Install
==========

pip install corrector

Usage
==========

.. code::

    import json
    from corrector import Corrector

    if __name__ == '__main__':
        corrector = Corrector('example.txt')
        print 'words:', json.dumps(corrector.nwords, ensure_ascii=False, indent=4)

        for word in [u'刘弱英', u'陈牵强', u'刘若华', u'hel', u'helle']:
            print 'word:', word
            print 'corrected:', corrector.correct(word)
            print 'possibilities:', json.dumps(corrector.possibilities(word),  ensure_ascii=False, indent=4)
            print '\n'

.. code::

    words: {
        "刘德华": 5,
        "hell": 2,
        "陈百强": 2,
        "刘若英": 4,
        "hello": 3
    }


    word: 刘弱英
    corrected: 刘若英
    possibilities: [
        "刘若英"
    ]


    word: 陈牵强
    corrected: 陈百强
    possibilities: [
        "陈百强"
    ]


    word: 刘若华
    corrected: 刘德华
    possibilities: [
        "刘若英",
        "刘德华"
    ]


    word: hel
    corrected: hell
    possibilities: [
        "hell"
    ]


    word: helle
    corrected: hello
    possibilities: [
        "hell",
        "hello"
    ]


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

