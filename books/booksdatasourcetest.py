'''
    booksdatasourcetest.py
    Daniel Busis and Max Goldberg, Sept. 19
'''

# TODO: Implement a thorough collection of unit tests for the non-constructor methods in BooksDataSource.
# TODO: Include all the CSV files containing your test data books directory.
# TODO: Put a Makefile in your books directory, and include in it a test target
# TODO: Tag your repo with the tag books_phase2.

import booksdatasource
import unittest

class BooksDataSourceTest(unittest.TestCase):
    def setUp(self):
        self.data_source = booksdatasource.BooksDataSource("books.csv", "authors.csv", "books_authors.csv")

    def tearDown(self):
        pass
    
    def test_book_string(self):
        self.assertRaises(ValueError, self.data_source.book, "This should not fail")

    def test_book_negative(self):
        self.assertRaises(ValueError, self.data_source.book, -5)

    def test_something(self):
        self.assertTrue(self.data_source is not None)

    def test_something(self):
        self.assertTrue(self.data_source is not None)	

if __name__ == '__main__':
    unittest.main()

