'''
    booksdatasourcetest.py
    Daniel Busis and Max Goldberg, Sept. 19
'''

import booksdatasource
import unittest

class BooksDataSourceTest(unittest.TestCase):
    '''
        Test class for the provided books.csv test file
    '''

    def setUp(self):
        self.data_source = booksdatasource.BooksDataSource("books.csv", "authors.csv", "books_authors.csv")

    def tearDown(self):
        pass
    
    def test_data_source_exists(self):
        self.assertTrue(self.data_source is not None)

    def test_book_overly_large_id(self):
        self.assertRaises(ValueError, self.data_source.book, 9999)
        #self.assertEqual(self.data_source.book(9999), {})

    def test_book_negative_id(self):
        self.assertRaises(ValueError, self.data_source.book, -1)

    def test_book_string_id(self):
        self.assertRaises(TypeError, self.data_source.book, "hi")

    def test_book_0(self):
        book_0 = {'id': 0, 'title': 'All Clear', 'publication_year': 2010}
        self.assertEqual(self.data_source.book(0), book_0)

    def test_book_37(self):
        book_0 = {'id': 0, 'title': 'All Clear', 'publication_year': 2010}
        self.assertEqual(self.data_source.book(0), book_0)

