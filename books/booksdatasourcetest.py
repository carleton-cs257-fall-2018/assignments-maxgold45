'''
    booksdatasourcetest.py
    Daniel Busis and Max Goldberg, Sept. 19
'''

# TODO: Finish implementing tests below (labeled with TODO)
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

### general tests:

    def test_data_source_exists(self):
        self.assertTrue(self.data_source is not None)

### book tests:
    
    def test_book_string(self):
        self.assertRaises(TypeError, self.data_source.book, "This should not fail")

    def test_book_negative(self):
        self.assertRaises(ValueError, self.data_source.book, -5)

    def test_book_float(self):
        self.assertRaises(TypeError, self.data_source.book, 5.2)

    def test_book_overly_large(self):
        self.assertRaises(ValueError, self.data_source.book, 9999)
        #self.assertEqual(self.data_source.book(9999), {})
    
    def test_book_0(self):
        book_0 = {'id': 0, 'title': 'All Clear', 'publication_year': 2010}
        self.assertEqual(self.data_source.book(0), book_0)

    def test_book_37(self):
        book_37 = {'id': 37, 'title': 'The Fifth Season', 'publication_year': 2015}
        self.assertEqual(self.data_source.book(37), book_37)

### books tests:

    # Test books for several search_texts:
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

    # Test books for random author_id
    def test_authors_text_nonexistent(self):
        self.assertEqual(self.data_source.books(author_id = "Dr Pepper"), [] )

    # Test books for correct answer
    def test_books_author_id_21(self):
        books_21 = ({'id': 40, 'title': 'Three Men in a Boat (to Say Nothing of the Dog)', 'publication_year': 1889})
        self.assertEqual(self.data_source.books(author_id=21), books_21)

### author tests:

    # Test author for random string
    def test_author_string(self):
        self.assertRaises(TypeError, self.data_source.author, "This should not fail")

    # Test author for negative
    def test_author_negative(self):
        self.assertRaises(ValueError, self.data_source.author, -5)

    # Test author for float id
    def test_author_float(self):
        self.assertRaises(TypeError, self.data_source.author, 5.2)

    # Test author for huge id
    def test_author_overly_large(self):
        self.assertRaises(ValueError, self.data_source.author, 9999)
        #self.assertEqual(self.data_source.author(9999), {})

    # Test author for id=0
    def test_author_0(self):
        author_0 = ({'id': 0, 'last_name': 'Willis', 'first_name': 'Connie', 'birth_year': 1945, 'death_year': 'none'})
        self.assertEqual(self.data_source.author(0), author_0)

    # Test author for id=23
    def test_author_23(self):
        author_23 = ({'id': 23, 'last_name': 'Dickens', 'first_name': 'Charles', 'birth_year': 1812, 'death_year': 1870})
        self.assertEqual(self.data_source.author(37), author_23)


### authors tests:

    # Test authors for a one-author book
    def test_authors_book_id_0(self):
        authors_0 = ({'id': 0, 'last_name': 'Willis', 'first_name': 'Connie', 'birth_year': 1945, 'death_year': 'none'})
        self.assertEqual(self.data_source.authors(book_id=0), authors_0)

    # Test authors for a two-author book
    def test_authors_book_id_6(self):
        authors_5_and_6 = ({'id': 5, 'last_name': 'Gaiman', 'first_name': 'Neil', 'birth_year': 1960, 'death_year': 'none'},{'id': 6, 'last_name': 'Pratchett', 'first_name': 'Terry', 'birth_year': 1948, 'death_year': 2015} )
        self.assertEqual(self.data_source.authors(book_id=6), authors_5_and_6)

    # Test authors for random author_id
    def test_books_text_nonexistent(self):
        self.assertEqual(self.data_source.authors(book_id = "Dr Pepper"), [] )

    # Test authors for start year
    def test_authors_start_year(self):
        authors_18_20 = ({'id': 18, 'last_name': 'Alderman', 'first_name': 'Naomi', 'birth_year': 1974, 'death_year': 'none'}, {'id': 20, 'last_name': 'Jemisen', 'first_name': 'N.K.', 'birth_year': 1972, 'death_year': 'none'})
        self.assertEqual(self.data_source.authors(start_year=1965), authors_18_20)

    # Test authors for end year
    def test_authors_end_year(self):
        authors_4_23 = ({'id': 4, 'last_name': 'Austen', 'first_name': 'Jane', 'birth_year': 1775, 'death_year': 1817}, {'id': 23, 'last_name': 'Dickens', 'first_name': 'Charles', 'birth_year': 1812, 'death_year': 1870})
        self.assertEqual(self.data_source.authors(start_year=1815), authors_4_23)


### authors_for book tests: TODO



### books_for_author tests: TODO

    def test_books_for_author_21(self):
        books_21 = ({'id': 40, 'title': 'Three Men in a Boat (to Say Nothing of the Dog)', 'publication_year': 1889})
        self.assertEqual(self.data_source.books_for_author(21), books_21)


if __name__ == '__main__':
    unittest.main()

