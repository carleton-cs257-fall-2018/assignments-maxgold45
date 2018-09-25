#!/usr/bin/env python3

import csv

'''
    booksdatasource.py
    Jeff Ondich, 18 September 2018

    For use in some assignments at the beginning of Carleton's
    CS 257 Software Design class, Fall 2018.

    Max Goldberg and Daniel Busis
'''

class BooksDataSource:
    '''
    A BooksDataSource object provides access to data about books and authors.
    The particular form in which the books and authors are stored will
    depend on the context (i.e. on the particular assignment you're
    working on at the time).

    Most of this class's methods return Python lists, dictionaries, or
    strings representing books, authors, and related information.

    An author is represented as a dictionary with the keys
    'id', 'last_name', 'first_name', 'birth_year', and 'death_year'.
    For example, Jane Austen would be represented like this
    (assuming her database-internal ID number is 72):

        {'id': 72, 'last_name': 'Austen', 'first_name': 'Jane',
         'birth_year': 1775, 'death_year': 1817}

    For a living author, the death_year is represented in the author's
    Python dictionary as None.

        {'id': 77, 'last_name': 'Murakami', 'first_name': 'Haruki',
         'birth_year': 1949, 'death_year': None}

    Note that this is a simple-minded representation of a person in
    several ways. For example, how do you represent the birth year
    of Sophocles? What is the last name of Gabriel García Márquez?
    Should we refer to the author of "Tom Sawyer" as Samuel Clemens or
    Mark Twain? Are Voltaire and Molière first names or last names? etc.

    A book is represented as a dictionary with the keys 'id', 'title',
    and 'publication_year'. For example, "Pride and Prejudice"
    (assuming an ID of 132) would look like this:

        {'id': 193, 'title': 'A Wild Sheep Chase', 'publication_year': 1982}

    '''

    def __init__(self, books_filename, authors_filename, books_authors_link_filename):
        ''' Initializes this data source from the three specified  CSV files, whose
            CSV fields are:

                books: ID,title,publication-year
                  e.g. 6,Good Omens,1990
                       41,Middlemarch,1871
                    

                authors: ID,last-name,first-name,birth-year,death-year
                  e.g. 5,Gaiman,Neil,1960,NULL
                       6,Pratchett,Terry,1948,2015
                       22,Eliot,George,1819,1880

                link between books and authors: book_id,author_id
                  e.g. 41,22
                       6,5
                       6,6
                  
                  [that is, book 41 was written by author 22, while book 6
                    was written by both author 5 and author 6]

            Note that NULL is used to represent a non-existent (or rather, future and
            unknown) year in the cases of living authors.

            NOTE TO STUDENTS: I have not specified how you will store the books/authors
            data in a BooksDataSource object. That will be up to you, in Phase 3.
        '''

        self.books_list = self._set_up_csv_books(books_filename)        
        self.authors_list = self._set_up_csv_authors(authors_filename)        
        self.books_authors_list = self._set_up_csv_books_authors(books_authors_link_filename)

        self.max_book_id = len(self.books_list) - 1
        self.max_author_id = len(self.authors_list) - 1
        
    def _set_up_csv_books(self, books_input_file):
        ''' Turns the books_input_file into an output_array of dictionaries.
        '''
        
        unix_dialect = csv.get_dialect("unix")
        with open(books_input_file, newline='', encoding='UTF-8') as csvfile:
            reader = csv.reader(csvfile, dialect="unix")
            books_array = [] 
            for entry in reader:
                next_book = self._convert_csv_line_to_book(entry)
                if next_book is not None:
                    books_array.append(next_book)
        return books_array

    #NOTE: Currently, I'm handling non-existent publish year by throwing out the entry
    #This comment should be deleted before turn-in
    def _convert_csv_line_to_book(self, book_line):
        for book_property in book_line:
            if book_property == '':
                return None
        return {'id': int(book_line[0]), 'title': book_line[1], 'publication_year': int(book_line[2])}

    def _set_up_csv_authors(self, authors_input_file):        
        unix_dialect = csv.get_dialect("unix")
        with open(authors_input_file, newline='', encoding='UTF-8') as csvfile:
            reader = csv.reader(csvfile, dialect="unix")
            authors_array = [] 
            for entry in reader:
                next_author = self._convert_csv_line_to_author(entry)
                authors_array.append(next_author)
        return authors_array

    def _convert_csv_line_to_author(self, author_line):
        author_death_year = author_line[4]
        if author_line[4] == "NULL":
            author_death_year = None
        else:
            author_death_year = int(author_death_year)
        return {'id': int(author_line[0]), 'last_name': author_line[1], 'first_name': author_line[2], 'birth_year': int(author_line[3]), 'death_year': author_death_year}

    def _set_up_csv_books_authors(self, books_authors_input_file):
        unix_dialect = csv.get_dialect("unix")
        with open(books_authors_input_file, newline='', encoding='UTF-8') as csvfile:
            reader = csv.reader(csvfile, dialect="unix")
            books_authors_array = []
            for entry in reader:
                next_book_author_link = self._convert_csv_line_to_book_author_link(entry)
                books_authors_array.append(next_book_author_link)
        return books_authors_array

    def _convert_csv_line_to_book_author_link(self, book_author_line):
        return {'book_id': int(book_author_line[0]), 'author_id': int(book_author_line[1])}


    def book(self, book_id):
        ''' Returns the book with the specified ID. (See the BooksDataSource comment
            for a description of how a book is represented.)
        
            Raises ValueError if book_id is not a valid book ID.
        '''

        list_of_books_with_id = [book for book in self.books_list if book['id']==book_id]
        if type(book_id) != int:
            raise ValueError("book_id type must be an int!")
        elif len(list_of_books_with_id) == 0:
            raise ValueError("Book ID requested does not exist! ID requested: " + str(book_id))
        else:
            return list_of_books_with_id[0]

        
    #NOTE: I haven't error-checked for if there are multiple books with the same ID. Might be worth implementing?
    #      But if we do implement something about that, it's probably better off in the initial data input section.
    #This comment should be deleted before turn-in.
    

    def _is_not_valid(self, book_id):
        return (book_id < 0) or (book_id > self.max_book_id) or (not type(book_id) == type(int))

    def books(self, *, author_id=None, search_text=None, start_year=None, end_year=None, sort_by='title'):
        ''' Returns a list of all the books in this data source matching all of
            the specified non-None criteria.

                author_id - only returns books by the specified author
                search_text - only returns books whose titles contain (case-insensitively) the search text
                start_year - only returns books published during or after this year
                end_year - only returns books published during or before this year

            Note that parameters with value None do not affect the list of books returned.
            Thus, for example, calling books() with no parameters will return JSON for
            a list of all the books in the data source.

            The list of books is sorted in an order depending on the sort_by parameter:

                'year' -- sorts by publication_year, breaking ties with (case-insenstive) title
                default -- sorts by (case-insensitive) title, breaking ties with publication_year
                
            See the BooksDataSource comment for a description of how a book is represented.

            QUESTION: Should Python interfaces specify TypeError?
            Raises TypeError if author_id, start_year, or end_year is non-None but not an integer.
            Raises ` if search_text or sort_by is non-None, but not a string.

            QUESTION: How about ValueError? And if so, for which parameters?
            Raises ValueError if author_id is non-None but is not a valid author ID.
        '''

        searched_books = [book for book in self.books_list if
                          (author_id is None or author_id in self._author_ids_for_book(book['id']))
                          and (search_text is None or search_text.lower() in book['title'].lower())
                          and (start_year is None or book['publication_year']>=start_year)
                          and (end_year is None or book['publication_year']<=end_year)
                          ]
        
        searched_books = self._sort_books_by_title(searched_books)

        return searched_books
    #NOTE/TODO: If we want an exception to be thrown for invalid author IDs in the books() method,
    #           we have to make this throw an exception manually

    

    def _sort_books_by_title(self, list_of_books):
        return list_of_books
    #NOTE/TODO: Make this sorting method work (breaking ties appropriately), as well as another for sorting by year

    def author(self, author_id):
        ''' Returns the author with the specified ID. (See the BooksDataSource comment for a
            description of how an author is represented.)
        
            Raises ValueError if author_id is not a valid author ID.
        '''
        list_of_authors_with_id = [author for author in self.authors_list if author['id']==author_id]

        if type(author_id) != int:
            raise ValueError("author_id type must be an int!")
        elif len(list_of_authors_with_id) == 0:
            raise ValueError("Author ID requested does not exist! ID requested: "+str(author_id))
        else:
            return list_of_authors_with_id[0]

    #def _is_not_valid(self, author_id):
    #     return (author_id < 0) or (author_id > self.max_author_id) or (not type(author_id) == type(int))
    #NOTE: Pretty sure this method has become redundant, along with max and min author id.
    #They, along with this method, should probably be deleted before turn-in.

    def authors(self, *, book_id=None, search_text=None, start_year=None, end_year=None, sort_by='birth_year'):
        ''' Returns a list of all the authors in this data source matching all of the
            specified non-None criteria.

                book_id - only returns authors of the specified book
                search_text - only returns authors whose first or last names contain
                    (case-insensitively) the search text
                start_year - only returns authors who were alive during or after
                    the specified year
                end_year - only returns authors who were alive during or before
                    the specified year

            Note that parameters with value None do not affect the list of authors returned.
            Thus, for example, calling authors() with no parameters will return JSON for
            a list of all the authors in the data source.

            The list of authors is sorted in an order depending on the sort_by parameter:

                'birth_year' - sorts by birth_year, breaking ties with (case-insenstive) last_name,
                    then (case-insensitive) first_name
                any other value - sorts by (case-insensitive) last_name, breaking ties with
                    (case-insensitive) first_name, then birth_year
        
            See the BooksDataSource comment for a description of how an author is represented.
        '''

        searched_authors = [author for author in self.authors_list if
                            (book_id is None or book_id in self._book_ids_for_author(author['id']))
                            and (search_text is None or search_text.lower() in author['first_name'].lower()
                                 or search_text.lower() in author['last_name'].lower())
                            and (start_year is None or author['death_year'] is None
                                 or author['death_year'] >= start_year)
                            and (end_year is None or author['birth_year'] <= end_year)
                            ]
        
        return searched_authors
    


    # Note for my students: The following two methods provide no new functionality beyond
    # what the books(...) and authors(...) methods already provide. But they do represent a
    # category of methods known as "convenience methods". That is, they provide very simple
    # interfaces for a couple very common operations.
    #
    # A question for you: do you think it's worth creating and then maintaining these
    # particular convenience methods? Is books_for_author(17) better than books(author_id=17)?

    def books_for_author(self, author_id):
        ''' Returns a list of all the books written by the author with the specified author ID.
            See the BooksDataSource comment for a description of how an book is represented. '''
        book_ids = self._book_ids_for_author(author_id)
        return [self.book(book_id) for book_id in book_ids]

    def _book_ids_for_author(self, author_id):
        return [book_author_link['book_id'] for book_author_link in self.books_authors_list
                    if book_author_link['author_id'] == author_id]

    def authors_for_book(self, book_id):
        ''' Returns a list of all the authors of the book with the specified book ID.
            See the BooksDataSource comment for a description of how an author is represented. '''
        author_ids = self._author_ids_for_book(book_id)
        return [self.author(author_id) for author_id in author_ids]

    def _author_ids_for_book(self, book_id):
        return [book_author_link['author_id'] for book_author_link in self.books_authors_list
                    if book_author_link['book_id'] == book_id]    

    #NOTE/TODO: The authors_for_book() and vice versa method could be simplified to call books() and authors()
