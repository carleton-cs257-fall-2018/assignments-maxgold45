import unittest

class webAppTester(unittest.TestCase):
    def setUp(self):
        self.movie_tester = moviesdatasource.MoviesDataSource(movies_info.csv, movies_people.csv)

    def tearDown(self):
        pass

    # movie

    def test_right_movie_id(self):
        self.assertEqual(self.movie_tester.movie(278), "The Shawshank Redemption")

    def test_wrong_movie_id_big(self):
        self.assertRaises(ValueError,self.movie_tester.movie, 279999999999998)

    def test_wrong_movie_id_negative(self):
        self.assertRaises(ValueError,self.movie_tester.movie, -5)

    def test_wrong_movie_id_decimal(self):
        self.assertRaises(ValueError,self.movie_tester.movie, 5.2)

    def test_wrong_movie_id_string(self):
        self.assertRaises(ValueError,self.movie_tester.movie, "hey")

    # person

    def test_person_id(self):
        self.assertEqual(self.movie_tester.person(65731), "Sam Worthington")

    def test_wrong_person_id_big(self):
        self.assertRaises(ValueError,self.movie_tester.person, 279999999999998)

    def test_wrong_person_id_negative(self):
        self.assertRaises(ValueError,self.movie_tester.person, -1234)

    def test_wrong_person_id_decimal(self):
        self.assertRaises(ValueError,self.movie_tester.person, 7.8)

    def test_wrong_person_id_string(self):
        self.assertRaises(ValueError,self.movie_tester.person, "hi")

#top ten titles
    #no boundary because there are no parameters
    def test_top_ten_titles(self):
        self.assertEqual(self.movie_tester.top_ten_titles(),
                    [{"title":"The Shawshank Redemption", "id":278},
                     {"title":"The Godfather", "id":238},
                     {"title":"Whiplash", "id":244786},
                     {"title":"Pulp Fiction", "id":680},
                     {"title":"Fight Club", "id":550},
                     {"title":"Schindler's List", "id":424},
                     {"title":"The Godfather: Part II", "id":240},
                     {"title":"Spirited Away", "id":129},
                     {"title":"Howl's Moving Castle", "id":4935},
                     {"title":"The Empire Strikes Back","id":1891}])

#movies with parameters

    def test_release_date_before_and_language(self):
        self.assertEqual(self.movie_tester.movies(release_date_before=1928,language="en"),
                    [{"title":"Intolerance","id":3059},
                    {"title":"The Big Parade","id":3060}])

    def movies_date_too_early(self):
        self.assertEquals(self.movie_tester.movies(release_date_before_1850),[])

    def movies_date_too_late(self):
        self.assertEquals(self.movie_tester.movies(release_date_after_2020),[])

    def movies_fake_person(self):
        self.assertEquals(self.movie_tester.movies(person="Alexis Engel"),[])

    def movies_fake_keyword(self):
        self.assertEquals(self.movie_tester.movies(keyword="sasydglas2"),[])

    #Counts the movies in english (instead of listing them)
    def movies_in_english(self):
        self.assertEquals(len(self.movie_tester.movies(language="en")), 4505)


#people with parameters

    def people_movie_role_name(self):
        self.assertEqual(self.movie_tester.people(movie="Avater",role="cast",name="david"),
                    [{"name":"David Van Horn","id":1207236},
                    {"name":"Joel David Moore","id":59231}])

    def people_fake_name(self):
        self.assertEqual(self.movie_tester.people(name="This is not a real person"), [])

    def people_fake_role(self):
        self.assertEqual(self.movie_tester.people(role="This is not a real role"), [])

    def people_fake_movie(self):
        self.assertEqual(self.movie_tester.people(movie="This is not a real movie"), [])




if __name__ == '__main__':
    unittest.main()
