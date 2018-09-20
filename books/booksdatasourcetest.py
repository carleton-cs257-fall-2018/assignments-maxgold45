'''
    booksdatasourcetest.py
    Daniel Busis and Max Goldberg, Sept. 19
'''

# TODO: Implement a thorough collection of unit tests for the non-constructor methods in BooksDataSource.
# TODO: Include all the CSV files containing your test data books directory.
# TODO: Tag your repo with the tag books_phase2.

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
    
    def test_book_string(self):
        self.assertRaises(TypeError, self.data_source.book, "This should not fail")

    def test_book_negative(self):
        self.assertRaises(ValueError, self.data_source.book, -5)

    def test_book_overly_large(self):
        self.assertRaises(ValueError, self.data_source.book, 9999)
        #self.assertEqual(self.data_source.book(9999), {})
    
    def test_data_source_exists(self):
        self.assertTrue(self.data_source is not None)

    def test_book_0(self):
        book_0 = {'id': 0, 'title': 'All Clear', 'publication_year': 2010}
        self.assertEqual(self.data_source.book(0), book_0)

    def test_book_37(self):
        book_37 = {'id': 37, 'title': 'The Fifth Season', 'publication_year': 2015}
        self.assertEqual(self.data_source.book(37), book_37)

if __name__ == '__main__':
    unittest.main()

