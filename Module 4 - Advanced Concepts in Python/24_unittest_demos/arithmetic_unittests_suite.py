import unittest
from arithmetic_unittests import TestAdd


def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestAdd))
    runner = unittest.TextTestRunner()
    runner.run(suite)

my_suite()
