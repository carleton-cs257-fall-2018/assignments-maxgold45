'''
    booksdatasourcetest.py
    Daniel Busis and Max Goldberg, Sept. 19
'''

import booksdatasource
import unittest

class BooksDataSourceTest(unittest.TestCase):
    def setUp(self):
        self.data_source = booksdatasource.BooksDataSource("books.csv", "authors.csv", "books_authors.csv")

    def tearDown(self):
        pass
    
    def test_something(self):
        self.assertTrue(self.data_source is not None)
