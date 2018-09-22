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
        self.assertRaises(ValueError, self.data_source.book, "This should not fail")

    def test_book_negative(self):
        self.assertRaises(ValueError, self.data_source.book, -5)

    def test_book_float(self):
        self.assertRaises(ValueError, self.data_source.book, 5.2)

    def test_book_overly_large(self):
        self.assertRaises(ValueError, self.data_source.book, 9999)
        #self.assertEqual(self.data_source.book(9999), {})
    
    def test_book_0(self):
        book_0 = ['0', 'All Clear', '2010']
        self.assertEqual(self.data_source.book(0), book_0)

    def test_book_37(self):
        book_37 = ['37', 'The Fifth Season', '2015']
        self.assertEqual(self.data_source.book(37), book_37)

### books tests:

    # Test books for several search_texts:
    def test_books_text_woosters_lowercase(self):
        books_woosters = ['23', 'The Code of the Woosters', '1938']
        self.assertEqual(self.data_source.books(search_text = "woosters"), books_woosters)

    def test_books_text_woosters_uppercase(self):
        books_woosters = ['23', 'The Code of the Woosters', '1938']
        self.assertEqual(self.data_source.books(search_text = "WOOSTERS"), books_woosters)

    def test_books_text_woosters_propercase(self):
        books_woosters = ['23', 'The Code of the Woosters', '1938']
        self.assertEqual(self.data_source.books(search_text = "Woosters"), books_woosters)

    def test_books_text_woosters_weirdcase(self):
        books_woosters = ['23', 'The Code of the Woosters', '1938']
        self.assertEqual(self.data_source.books(search_text = "wOoStErS"), books_woosters)

    # Test books for random author_id
    def test_authors_text_nonexistent(self):
        self.assertRaises(ValueError, self.data_source.books, author_id = 9999 )

    # Test books for correct answer
    def test_books_author_id_21(self):
        books_21 = ['40', 'Three Men in a Boat (to Say Nothing of the Dog)', '1889']
        self.assertEqual(self.data_source.books(author_id=21), books_21)

    def test_books_1990_to_1990(self):
        books_1990 = ['6', 'Good Omens', '1990']
        self.assertEqual(self.data_source.books(start_year=1990, end_year = 1990), books_1990)

    def test_books_1989_to_1991(self):
        books_1990 = ['6', 'Good Omens', '1990']
        self.assertEqual(self.data_source.books(start_year=1989, end_year = 1991), books_1990)

    def test_books_1991_to_1989(self):
        self.assertEqual(self.data_source.books(start_year=1991, end_year = 1989), [])

    def test_books_1988_to_1990(self):
        books_1988_1990 = ['6', 'Good Omens', '1990']
        self.assertEqual(self.data_source.books(start_year=1988, end_year = 1990), [])

    def test_books_1988_to_1990_sort_year(self):
        books_1988_1990 = ['24', 'The Satanic Verses', '1988'], ['6', 'Good Omens', '1990']
        self.assertEqual(self.data_source.books(start_year=1988, end_year = 1990, sort_by='year'), [])

### author tests:

    # Test author for random string
    def test_author_string(self):
        self.assertRaises(ValueError, self.data_source.author, "This should not fail")

    # Test author for negative
    def test_author_negative(self):
        self.assertRaises(ValueError, self.data_source.author, -5)

    # Test author for float id
    def test_author_float(self):
        self.assertRaises(ValueError, self.data_source.author, 5.2)

    # Test author for huge id
    def test_author_overly_large(self):
        self.assertRaises(ValueError, self.data_source.author, 9999)
        #self.assertEqual(self.data_source.author(9999), {})

    # Test author for id=0
    def test_author_0(self):
        author_0 = ['0', 'Willis', 'Connie', '1945', 'none']
        self.assertEqual(self.data_source.author(0), author_0)

    # Test author for id=23
    def test_author_23(self):
        author_23 = ['23', 'Dickens', 'Charles', '1812', '1870']
        self.assertEqual(self.data_source.author(23), author_23)


### authors tests:

    # Test authors for a one-author book
    def test_authors_book_id_0(self):
        authors_0 = ['0', 'Willis', 'Connie', '1945', 'none']
        self.assertEqual(self.data_source.authors(book_id=0), authors_0)

    # Test authors for a two-author book
    def test_authors_book_id_6(self):
        authors_5_and_6 = ['5', 'Gaiman', 'Neil', '1960', 'none'],['6', 'Pratchett', 'Terry', '1948', '2015']
        self.assertEqual(self.data_source.authors(book_id=6), authors_5_and_6)

    # Test authors for random author_id
    def test_authors_text_nonexistent(self):
        self.assertEqual(self.data_source.authors(book_id = "Dr Pepper"), [] )

    # Test authors for start year
    def test_authors_start_year(self):
        authors_18_20 = ['18', 'Alderman', 'Naomi', '1974', 'none'], ['20', 'Jemisen', 'N.K.', '1972', 'none']
        self.assertEqual(self.data_source.authors(start_year=1965), authors_18_20)

    # Test authors for start year, sorting by birth year
    def test_authors_start_year(self):
        authors_18_20 = ['20', 'Jemisen', 'N.K.', '1972', 'none'], ['18', 'Alderman', 'Naomi', '1974', 'none']
        self.assertEqual(self.data_source.authors(start_year=1965, sort_by='birth_year'), authors_18_20)

    # Test authors for end year
    def test_authors_end_year(self):
        authors_4_23 = ['4', 'Austen', 'Jane', '1775', '1817'], ['23', 'Dickens', 'Charles', '1812', '1870']
        self.assertEqual(self.data_source.authors(end_year=1815), authors_4_23)

    # Test authors for several search_texts:
    def test_authors_text_jerome_lowercase(self):
        authors_jerome = ['21', 'Jerome', 'Jerome K.', '1859', '1927']
        self.assertEqual(self.data_source.authors(search_text = "jerome"), authors_jerome)

    def test_authors_text_jerome_uppercase(self):
        authors_jerome = ['21', 'Jerome', 'Jerome K.', '1859', '1927']
        self.assertEqual(self.data_source.authors(search_text = "JEROME"), authors_jerome)

    def test_authors_text_jerome_propercase(self):
        authors_jerome = ['21', 'Jerome', 'Jerome K.', '1859', '1927']
        self.assertEqual(self.data_source.authors(search_text = "Jerome"), authors_jerome)

    def test_authors_text_jerome_weirdcase(self):
        authors_jerome = ['21', 'Jerome', 'Jerome K.', '1859', '1927']
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
        author_10 = ['10', 'Lewis', 'Sinclair', '1885', '1951']
        self.assertEqual(self.data_source.authors_for_book(10), author_10)

    # Test two-author book
    def test_authors_for_book_6(self):
        authors_5_6 = ['5', 'Gaiman', 'Neil', '1960', 'None'], ['6', 'Pratchett', 'Terry', '1948', '2015']
        self.assertEqual(self.data_source.authors_for_book(6), authors_5_6)

### books_for_author tests:

    def test_books_for_author_21(self):
        books_21 = ('40', 'Three Men in a Boat (to Say Nothing of the Dog)', '1889')
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
        book_10 = ['10', 'Main Street', '1920']
        self.assertEqual(self.data_source.books_for_author(10), book_10)

    #Test two-book author
    def test_authors_for_book(self):
        books_11_24 = ['11', 'Midnight\'s Children', '1981'], ['24', 'The Satanic Verses', '1988']
        self.assertEqual(self.data_source.books_for_author(11), books_11_24)


if __name__ == '__main__':
    unittest.main()

