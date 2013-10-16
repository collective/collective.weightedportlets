from collective.weightedportlets.testing import WPORTLETS_FUNCTIONAL_TESTING

from plone.testing import layered

import doctest
import unittest2 as unittest

optionflags = (doctest.NORMALIZE_WHITESPACE
               | doctest.ELLIPSIS
               | doctest.REPORT_NDIFF
               | doctest.REPORT_ONLY_FIRST_FAILURE)


normal_testfiles = ['weights.txt', ]


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests(
        [layered(doctest.DocFileSuite(test,
                                      optionflags=optionflags),
                 layer=WPORTLETS_FUNCTIONAL_TESTING)
         for test in normal_testfiles])
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
