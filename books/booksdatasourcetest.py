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
    def test_books_text_woosters_lowercase(self):
        books_woosters = {'id': 23, 'title': 'The Code of the Woosters', 'publication_year': 1938}
        self.assertEqual(self.data_source.books(search_text = "woosters"), books_woosters)

    def test_books_text_woosters_uppercase(self):
        books_woosters = {'id': 23, 'title': 'The Code of the Woosters', 'publication_year': 1938}
        self.assertEqual(self.data_source.books(search_text = "WOOSTERS"), books_woosters)

    def test_books_text_woosters_propercase(self):
        books_woosters = {'id': 23, 'title': 'The Code of the Woosters', 'publication_year': 1938}
        self.assertEqual(self.data_source.books(search_text = "Woosters"), books_woosters)

    def test_books_text_woosters_weirdcase(self):
        books_woosters = {'id': 23, 'title': 'The Code of the Woosters', 'publication_year': 1938}
        self.assertEqual(self.data_source.books(search_text = "wOoStErS"), books_woosters)

    # Test books for random author_id
    def test_authors_text_nonexistent(self):
        self.assertEqual(self.data_source.books(author_id = "Dr Pepper and the Heart Club Band"), [] )

    # Test books for correct answer
    def test_books_author_id_21(self):
        books_21 = [{'id': 40, 'title': 'Three Men in a Boat (to Say Nothing of the Dog)', 'publication_year': 1889}]
        self.assertEqual(self.data_source.books(author_id=21), books_40)

    def test_books_1990_to_1990(self):
        books_1990 = [{'id': 6, 'title': 'Good Omens', 'publication_year': 1990}]
        self.assertEqual(self.data_source.books(start_year=1990, end_year = 1990), books_1990)

    def test_books_1989_to_1991(self):
        books_1990 = [{'id': 6, 'title': 'Good Omens', 'publication_year': 1990}]
        self.assertEqual(self.data_source.books(start_year=1989, end_year = 1991), books_1990)

    def test_books_1991_to_1989(self):
        self.assertEqual(self.data_source.books(start_year=1991, end_year = 1989), [])

    def test_books_1988_to_1990(self):
        books_1988_1990 = [{'id': 6, 'title': 'Good Omens', 'publication_year': 1990}, {'id': 24, 'title': 'The Satanic Verses', 'publication_year': 1988}]
        self.assertEqual(self.data_source.books(start_year=1988, end_year = 1990), [])

    def test_books_1988_to_1990_sort_year(self):
        books_1988_1990 = [{'id': 24, 'title': 'The Satanic Verses', 'publication_year': 1988}, {'id': 6, 'title': 'Good Omens', 'publication_year': 1990}]
        self.assertEqual(self.data_source.books(start_year=1988, end_year = 1990, sort_by='year'), [])

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
        author_0 = [{'id': 0, 'last_name': 'Willis', 'first_name': 'Connie', 'birth_year': 1945, 'death_year': 'none'}]
        self.assertEqual(self.data_source.author(0), author_0)

    # Test author for id=23
    def test_author_23(self):
        author_23 = [{'id': 23, 'last_name': 'Dickens', 'first_name': 'Charles', 'birth_year': 1812, 'death_year': 1870}]
        self.assertEqual(self.data_source.author(37), author_23)


### authors tests:

    # Test authors for a one-author book
    def test_authors_book_id_0(self):
        authors_0 = [{'id': 0, 'last_name': 'Willis', 'first_name': 'Connie', 'birth_year': 1945, 'death_year': 'none'}]
        self.assertEqual(self.data_source.authors(book_id=0), authors_0)

    # Test authors for a two-author book
    def test_authors_book_id_6(self):
        authors_5_and_6 = [{'id': 5, 'last_name': 'Gaiman', 'first_name': 'Neil', 'birth_year': 1960, 'death_year': 'none'},{'id': 6, 'last_name': 'Pratchett', 'first_name': 'Terry', 'birth_year': 1948, 'death_year': 2015} ]
        self.assertEqual(self.data_source.authors(book_id=6), authors_5_and_6)

    # Test authors for random author_id
    def test_authors_text_nonexistent(self):
        self.assertEqual(self.data_source.authors(book_id = "Dr Pepper"), [] )

    # Test authors for start year
    def test_authors_start_year(self):
        authors_18_20 = [{'id': 18, 'last_name': 'Alderman', 'first_name': 'Naomi', 'birth_year': 1974, 'death_year': 'none'}, {'id': 20, 'last_name': 'Jemisen', 'first_name': 'N.K.', 'birth_year': 1972, 'death_year': 'none'}]
        self.assertEqual(self.data_source.authors(start_year=1965), authors_18_20)

    # Test authors for end year
    def test_authors_end_year(self):
        authors_4_23 = [{'id': 4, 'last_name': 'Austen', 'first_name': 'Jane', 'birth_year': 1775, 'death_year': 1817}, {'id': 23, 'last_name': 'Dickens', 'first_name': 'Charles', 'birth_year': 1812, 'death_year': 1870}]
        self.assertEqual(self.data_source.authors(start_year=1815), authors_4_23)

    # Test authors for several search_texts:
    def test_authors_text_jerome_lowercase(self):
        authors_jerome = [{'id': 21, 'last_name': 'Jerome', 'first_name': 'Jerome K.','birth_year': 1859, 'death_year': 1927}]
        self.assertEqual(self.data_source.authors(search_text = "jerome"), authors_jerome)

    def test_authors_text_jerome_uppercase(self):
        authors_jerome = [{'id': 21, 'last_name': 'Jerome', 'first_name': 'Jerome K.','birth_year': 1859, 'death_year': 1927}]
        self.assertEqual(self.data_source.authors(search_text = "JEROME"), authors_jerome)

    def test_authors_text_jerome_propercase(self):
        authors_jerome = [{'id': 21, 'last_name': 'Jerome', 'first_name': 'Jerome K.','birth_year': 1859, 'death_year': 1927}]
        self.assertEqual(self.data_source.authors(search_text = "Jerome"), authors_jerome)

    def test_authors_text_jerome_weirdcase(self):
        authors_jerome = [{'id': 21, 'last_name': 'Jerome', 'first_name': 'Jerome K.','birth_year': 1859, 'death_year': 1927}]
        self.assertEqual(self.data_source.authors(search_text = "jErOmE"), authors_jerome)

    # Test author for random book_id
    def test_authors_text_nonexistent(self):
        self.assertEqual(self.data_source.authors(book_id = "Dr Pepper"), [] )


### authors_for_book tests:

    def test_authors_for_book_string(self):
        self.assertRaises(TypeError, self.data_source.authors_for_book, "This should not fail")

    def test_authors_for_book_negative(self):
        self.assertRaises(ValueError, self.data_source.authors_for_book, -5)

    def test_authors_for_book_float(self):
        self.assertRaises(TypeError, self.data_source.authors_for_book, 5.2)

    def test_authors_for_book_overly_large(self):
        self.assertRaises(ValueError, self.data_source.authors_for_book, 9999)

    # Test one-author book
    def test_authors_for_book_10(self):
        author_10 = [{'id': 10, 'last_name': 'Lewis', 'first_name': 'Sinclair', 'birth_year': 1885, 'death_year': 1951}]
        self.assertEqual(self.data_source.authors_for_book(10), author_10)

    # Test two-author book
    def test_authors_for_book_6(self):
        authors_5_6 = [{'id': 5, 'last_name': 'Gaiman', 'first_name': 'Neil', 'birth_year': 1960, 'death_year': None},{'id': 6, 'last_name': 'Pratchett', 'first_name': 'Terry', 'birth_year': 1948, 'death_year': 2015}]
        self.assertEqual(self.data_source.authors_for_book(6), books_11_24)

### books_for_author tests:

    def test_books_for_author_21(self):
        books_21 = ({'id': 40, 'title': 'Three Men in a Boat (to Say Nothing of the Dog)', 'publication_year': 1889})
        self.assertEqual(self.data_source.books_for_author(21), books_21)
    
    def test_books_for_author_string(self):
        self.assertRaises(TypeError, self.data_source.books_for_author, "Penny the Dog")

    def test_books_for_author_negative(self):
        self.assertRaises(ValueError, self.data_source.books_for_author, -1)

    def test_books_for_author_float(self):
        self.assertRaises(TypeError, self.data_source.books_for_author, -7.3)

    def test_books_for_author_overly_large(self):
        self.assertRaises(ValueError, self.data_source.books_for_author, 9999)

    #Test one-book author
    def test_books_for_author_7(self):
        book_10 = [{'id': 10, 'title': 'Main Street', 'publication_year': 1920}]
        self.assertEqual(self.data_source.books_for_author(10), book_10)

    #Test two-book author
    def test_authors_for_book(self):
        books_11_24 = ({'id': 11, 'title': 'Midnight\'s Children', 'publication_year': 1981}, {'id': 24, 'title': 'The Satanic Verses', 'publication_year': 1988})
        self.assertEqual(self.data_source.books_for_author(11), books_11_24)


if __name__ == '__main__':
    unittest.main()

