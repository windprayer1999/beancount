from datetime import date
import unittest
import re

from beancount.parser import printer
from beancount.core import data
from beancount.core import balance


FILELOC = data.FileLocation('beancount/core/testing.beancount', 12345)


class TestPrinter(unittest.TestCase):

    def test_render_fileloc(self):
        fileloc_str = printer.render_fileloc(FILELOC)
        self.assertTrue(isinstance(fileloc_str, str))
        self.assertTrue(re.search('12345', fileloc_str))
        self.assertTrue(re.search(FILELOC.filename, fileloc_str))

    def test_format_errors(self):
        entry = data.Open(FILELOC, date(2014, 1, 15), 'Assets:Bank:Checking', [])
        errors = [balance.BalanceError(FILELOC, "Example balance error", entry)]
        errors_str = printer.format_errors(errors)
        self.assertTrue(isinstance(errors_str, str))

    def test_string_quote(self):
        self.assertEqual('"something"', printer.string_quote("something"))
        self.assertEqual('"5"', printer.string_quote(5))
        self.assertEqual('', printer.string_quote(None))

    def __test_format_entry(self):
        ## FIXME: TODO
        pass


__incomplete__ = True