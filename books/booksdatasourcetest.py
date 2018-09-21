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

    def test_data_source_exists(self):
        self.assertTrue(self.data_source is not None)
    
    def test_book_string(self):
        self.assertRaises(TypeError, self.data_source.book, "This should not fail")

    def test_book_negative(self):
        self.assertRaises(ValueError, self.data_source.book, -5)

##    def test_book_zero(self):
##        self.assertRaises(ValueError, self.data_source.book, 0)
## Since book id's start at 0, pretty sure the test_book_0 method is correct implementation

    def test_book_overly_large(self):
        self.assertRaises(ValueError, self.data_source.book, 9999)
        #self.assertEqual(self.data_source.book(9999), {})
    
    def test_book_0(self):
        book_0 = {'id': 0, 'title': 'All Clear', 'publication_year': 2010}
        self.assertEqual(self.data_source.book(0), book_0)

    def test_book_37(self):
        book_37 = {'id': 37, 'title': 'The Fifth Season', 'publication_year': 2015}
        self.assertEqual(self.data_source.book(37), book_37)

    def test_authors_text_jerome_lowercase(self):
        authors_jerome = [{'id': 21, 'last_name': 'Jerome', 'first_name': 'Jerome K.','birth_year': 1859, 'death_year': 1927}]
        self.assertEqual(self.data_source.books(search_text = "jerome"), authors_jerome)

    def test_authors_text_jerome_uppercase(self):
        authors_jerome = [{'id': 21, 'last_name': 'Jerome', 'first_name': 'Jerome K.','birth_year': 1859, 'death_year': 1927}]
        self.assertEqual(self.data_source.books(search_text = "JEROME"), authors_jerome)

    def test_authors_text_jerome_propercase(self):
        authors_jerome = [{'id': 21, 'last_name': 'Jerome', 'first_name': 'Jerome K.','birth_year': 1859, 'death_year': 1927}]
        self.assertEqual(self.data_source.books(search_text = "Jerome"), authors_jerome)

    def test_authors_text_jerome_weirdcase(self):
        authors_jerome = [{'id': 21, 'last_name': 'Jerome', 'first_name': 'Jerome K.','birth_year': 1859, 'death_year': 1927}]
        self.assertEqual(self.data_source.books(search_text = "jErOmE"), authors_jerome)

    def test_authors_text_nonexistent(self):
        self.assertEqual(self.data_source.books(author_id = "Dr Pepper"), [] )

    def test_books_for_author_21(self):
        books_21 = ({'id': 40, 'title': 'Three Men in a Boat (to Say Nothing of the Dog)', 'publication_year': 1889})
        self.assertEqual(self.data_source.books_for_author(21), books_21)

    def test_books_author_id_21(self):
        books_21 = ({'id': 40, 'title': 'Three Men in a Boat (to Say Nothing of the Dog)', 'publication_year': 1889})
        self.assertEqual(self.data_source.books(author_id=21), books_21)

# Max added the following:

    # Test authors for a one-author book
    def test_authors_book_id_0(self):
        authors_0 = ({'id': 0, 'last_name': 'Willis', 'first_name': 'Connie', 'birth_year': 1945, 'death_year': 'none'})
        self.assertEqual(self.data_source.authors(book_id=0), authors_0)

    # Test authors for a two-author book
    def test_authors_book_id_6(self):
        authors_5_and_6 = ({'id': 5, 'last_name': 'Gaiman', 'first_name': 'Neil', 'birth_year': 1960, 'death_year': 'none'},{'id': 6, 'last_name': 'Pratchett', 'first_name': 'Terry', 'birth_year': 1948, 'death_year': 2015} )
        self.assertEqual(self.data_source.authors(book_id=6), authors_5_and_6)

    # Test authors for start year
    def test_authors_start_year(self):
        authors_18_20 = ({'id': 18, 'last_name': 'Alderman', 'first_name': 'Naomi', 'birth_year': 1974, 'death_year': 'none'}, {'id': 20, 'last_name': 'Jemisen', 'first_name': 'N.K.', 'birth_year': 1972, 'death_year': 'none'})
        self.assertEqual(self.data_source.authors(start_year=1965), authors_18_20)

    # Test authors for end year
    def test_authors_end_year(self):
        authors_4_23 = ({'id': 4, 'last_name': 'Austen', 'first_name': 'Jane', 'birth_year': 1775, 'death_year': 1817}, {'id': 23, 'last_name': 'Dickens', 'first_name': 'Charles', 'birth_year': 1812, 'death_year': 1870})
        self.assertEqual(self.data_source.authors(start_year=1815), authors_4_23)

    #TODO test books
    #TODO test authors_for_book



if __name__ == '__main__':
    unittest.main()

