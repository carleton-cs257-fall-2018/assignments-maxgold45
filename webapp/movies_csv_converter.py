#!/usr/bin/env python3
# By Max Goldberg and Alexis Engel

import sys
import re
import csv
import json

def load_from_movies_csv_file(movies_csv_file_name,credits_csv_file_name):

    movies = {}
    genres = {}

    actors = {}
    crew = {}
    jobs = {}
    movies_actors = []
    movies_crew = []

    movies_csv_file = open(movies_csv_file_name)
    movies_reader = csv.reader(movies_csv_file)

    for movie_row in movies_reader:
        # Make movies table
        movie = {'title': movie_row[1], 'budget': movie_row[2], 'genres': movie_row[3],
                'keywords': movie_row[4], "language": movie_row[5], "overview": movie_row[6],
                "popularity": movie_row[7], "vote_average": movie_row[8], "release_date": movie_row[9],
                "revenue": movie_row[10], "runtime": movie_row[11], "tagline": movie_row[12],
                "vote_count":movie_row[13]}
        movies[movie_row[0]] = movie

        # Make genres table
        genre_ids = []
        print(movies[movie_row[0]])
        for genre in movies[movie_row[0]['genres']]:
            genre_data = json.loads(genre)
            for i in genre_data:
                if genre_data[i]['id'] not in genres:
                    genres[genre_data[i]['id']] = {'genre': genre_data[i]['name']}
                    genre_ids.append(genre_data[i]['id'])
        movies['genres'] = genre_ids

    credits_csv_file = open(credits_csv_file_name)
    credits_reader = csv.reader(credits_csv_file)

    for credit_row in credits_reader:
        actor_data = json.loads(credit_row[2])
        for i in actor_data:
            # Make actor table
            if actor_data[i]['id'] not in actors:
                actors[actor_data[i]['id']] = {'name': actor_data[i]['name']}

            # Make movies_actor linking table
            movie_actor = {'movie_id': credit_row[0], 'actor_id': actor_data[i]['id'],
                        'character_name': actor_data[i]['character']}
            movies_actors.append(movie_actor)

        crew_data = json.loads(credit_row[3])
        for j in crew_data:
            # Make crew table
            if crew_data[i]['id'] not in crew:
                crew[crew_data[i]['id']] = {'name': crew_data[i]['name']}

            # Make jobs table
            if crew_data[i]['job'] not in jobs:
                jobs.append(crew_data[i]['job'])

            # Make movies_crew table
            job_index = 0
            for k in range(len(jobs)):
                if jobs[k] == crew_data[i]['job']:
                    job_index = k

            movie_crew = {'movie_id': credit_row[0], 'crew_id': crew_data[i]['id'], 'job_id': job_index}
            movies_crew.append(movie_crew)


    movies_csv_file.close()
    return (movies, genres, actors, crew, jobs, movies_actors, movies_crew)



def save_movies_table(movies, csv_file_name):
    ''' Save the movies in CSV form, with each row containing
        (id, title, budget, genres, keywords, language_code, overview, popularity, vote_average, release_date,
        revenue, runtime, tagline, vote_count). '''
    output_file = open(csv_file_name, 'w')
    writer = csv.writer(output_file)
    for movie in movies:
        movie_row = [movie['id'], movie['title'], movie['budget'], movie['genres'], movie['keywords'],
                    movie['language_code'], movie['overview'], movie['popularity'], movie['vote_average'],
                    movie['release_date'], movie['revenue'], movie['runtime'], movie['tagline'], movie['vote_count']]
        writer.writerow(movie_row)
    output_file.close()

def save_genres_table(genres, csv_file_name):
    ''' Save the genres in CSV form, with each row containing
        (id, genre)'''
    output_file = open(csv_file_name, 'w')
    writer = csv.writer(output_file)
    for genre in genres:
        genre_row = [genre['id'], genre['genre']]
        writer.writerow(genre_row)
    output_file.close()

def save_actors_table(actors, csv_file_name):
    ''' Save the actors in CSV form, with each row containing
        (id, name)'''
    output_file = open(csv_file_name, 'w')
    writer = csv.writer(output_file)
    for actor in actors:
        actor_row = [actor['id'], actor['name']]
        writer.writerow(actor_row)
    output_file.close()

def save_crew_table(crew, csv_file_name):
    ''' Save the crew in CSV form, with each row containing
        (id, name)'''
    output_file = open(csv_file_name, 'w')
    writer = csv.writer(output_file)
    for person in crew:
        person_row = [crew['id'], crew['name']]
        writer.writerow(person_row)
    output_file.close()

def save_jobs_table(jobs, csv_file_name):
    ''' Save the jobs in CSV form, with each row containing
        (id, job)'''
    output_file = open(csv_file_name, 'w')
    writer = csv.writer(output_file)
    for i in range(len(jobs)):
        job_row = [i, jobs[i]]
        writer.writerow(job_row)
    output_file.close()

def save_movies_actors_table(movies_actors, csv_file_name):
    ''' Save the movies and actors in CSV form, with each row containing
        (movie_id, actor_id, character_name). '''
    output_file = open(csv_file_name, 'w')
    writer = csv.writer(output_file)
    for movie_actor in movies_actors:
        movie_actor_row = [movie_actor['movie_id'], movie_actor['actor_id'], movie_actor['character_name']]
        writer.writerow(movie_actor_row)
    output_file.close()

def save_movies_crew_table(movies_crew, csv_file_name):
    ''' Save the movies and actors in CSV form, with each row containing
        (movie_id, crew_id, job_id). '''
    output_file = open(csv_file_name, 'w')
    writer = csv.writer(output_file)
    for movie_crew in movies_crew:
        movie_crew_row = [movie_crew['movie_id'], movie_crew['crew_id'], movie_crew['job_id']]
        writer.writerow(movie_crew_row)
    output_file.close()

if __name__ == '__main__':
    movies, genres, actors, crew, jobs, movies_actors, movies_crew = load_from_movies_csv_file('tmdb_5000_movies.csv', 'tmdb_5000_credis.csv')

    save_movies_table(movies, 'movies.csv')
    save_genres_table(genres, 'genres.csv')
    save_actors_table(actors, 'actors.csv')
    save_crew_table(crew, 'crew.csv')
    save_jobs_table(jobs, 'jobs.csv')
    save_movies_actors_table(movies_actors, 'movies_actors.csv')
    save_movies_crew_table(movies_crew, 'movies_crew.csv')
