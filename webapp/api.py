#!/usr/bin/env python3
'''
    api.py
    Max Goldberg
    Alexis Engel
'''
import sys
import flask
import json
import psycopg2
import config

app = flask.Flask(__name__)

def get_connection():
    '''
    Returns a connection to the database described
    in the config module. Returns None if the
    connection attempt fails.
    '''
    connection = None
    try:
        connection = psycopg2.connect(database=config.database,
                                      user=config.user,
                                      password=config.password)
    except Exception as e:
        print(e, file=sys.stderr)
    return connection
def get_select_query_results(connection, query, parameters=None):
    '''
    Executes the specified query with the specified tuple of
    parameters. Returns a cursor for the query results.
    Raises an exception if the query fails for any reason.
    '''
    cursor = connection.cursor()
    if parameters is not None:
        cursor.execute(query, parameters)
    else:
        cursor.execute(query)
    return cursor

@app.after_request
def set_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/movies/toptentitles')
def get_top_ten_titles():
    ''' Returns a list of the top ten movies' title by vote_average with a
    minimum of 100 vote_count. '''

    query = 'SELECT id, title, release_date FROM movies WHERE vote_count>100 ORDER BY vote_average DESC limit 10;'
    movie_list = []
    connection = get_connection()
    if connection is not None:
        try:
            for row in get_select_query_results(connection, query):
                movie = {'id':row[0], 'title':row[1], 'release_date':row[2]}
                movie_list.append(movie)
        except Exception as e:
            print(e, file=sys.stderr)
        connection.close()

    return json.dumps(movie_list)

@app.route('/actor/<actor_id>')
def get_actor(actor_id):
    query = '''select movies_actors.actor_id, actors.name, character_name,
    movie_id, title from actors, movies, movies_actors where actors.id = %s
    and actor_id = actors.id and movies.id = movies_actors.movie_id;'''
    info_list = []
    connection = get_connection()
    if connection is not None:
        try:
            cursor = get_select_query_results(connection, query, (actor_id,))
            for row in cursor:
                if row is not None:
                    info = {'actor_id':row[0], 'name':row[1],'character_name':row[2], 'movie_id':row[3], 'title':row[4]}
                    info_list.append(info)
        except Exception as e:
            print(e, file=sys.stderr)
            connection.close()

        return json.dumps(info_list)

@app.route('/crew/<crew_id>')
def get_one_crew(crew_id):
    query = '''select movies_crew.crew_id, crew.name, job, movie_id, title from
    crew, movies, movies_crew, jobs where crew.id = %s and crew_id = crew.id
    and movies.id = movies_crew.movie_id and jobs.id = job_id;'''
    info_list = []
    connection = get_connection()
    if connection is not None:
        try:
            cursor = get_select_query_results(connection, query, (crew_id,))
            for row in cursor:
                if row is not None:
                    info = {'crew_id':row[0], 'name':row[1],
                            'job':row[2],'movie_id':row[3], 'title':row[4]}
                    info_list.append(info)
        except Exception as e:
            print(e, file=sys.stderr)
            connection.close()

        return json.dumps(info_list)

@app.route('/movie/<movie_id>')
def get_movie(movie_id):
    ''' Get one movie given its id.
    '''
    query = 'select * from movies where movies.id = %s;'
    info = {}
    connection = get_connection()
    if connection is not None:
        try:
            cursor = get_select_query_results(connection, query, (movie_id,))
            row = next(cursor)
            if row is not None:
                info = {'id':row[0], 'title':row[1], 'budget':row[2],
                'genres':row[3], 'keywords':row[4], 'language_code':row[5],
                'overview':row[6], 'popularity':row[7], 'vote_average':row[8],
                'release_date':row[9], 'revenue':row[10], 'runtime':row[11],
                'tagline':row[12], 'vote_count':row[13]}
        except Exception as e:
            print(e, file=sys.stderr)
            connection.close()

        return json.dumps(info)

@app.route('/movies/<title>')
def get_movies(title):
    ''' Returns a list of movies given a search limited to 50.
        You are able to sort by title, popularity, or vote_average.
        Search by title.
    '''
    query = 'select title, id, release_date from movies where UPPER(title) LIKE\'%%\' || UPPER(%s) || \'%%\''

    # Sort parameters
    sort_argument = flask.request.args.get('sort')
    if sort_argument == 'title':
        query += 'ORDER BY title'
    elif sort_argument == 'popularity':
        query += 'ORDER BY popularity'
    elif sort_argument == 'vote_average':
        query += 'ORDER BY vote_average'

    asc_argument = flask.request.args.get('asc')
    if asc_argument == 'desc':
        query += ' DESC'
    elif sort_argument == 'asc':
        query += ' ASC'

    movie_list = []
    connection = get_connection()
    if connection is not None:
        try:
            for row in get_select_query_results(connection, query, (title,)):
                movie = {'title':row[0],'id':row[1], 'release_date':row[2]}
                movie_list.append(movie)
        except Exception as e:
            print(e, file=sys.stderr)
        connection.close()

    return json.dumps(movie_list)

@app.route('/actors/<name>')
def get_actors(name):
    query = 'select id, name from actors where UPPER(name) LIKE\'%%\' || UPPER(%s) || \'%%\' ORDER BY name;'

    actor_list = []
    connection = get_connection()
    if connection is not None:
        try:
            for row in get_select_query_results(connection, query, (name,)):
                actor = {'id':row[0], 'name':row[1]}
                actor_list.append(actor)
        except Exception as e:
            print(e, file=sys.stderr)
        connection.close()

    return json.dumps(actor_list)

@app.route('/crew/<name>/<job>')
def get_crew(name, job):
    query = 'SELECT DISTINCT crew.id, name from crew, jobs, movies_crew where UPPER(name) LIKE \'%%\' || UPPER(%s) || \'%%\' and UPPER(job) LIKE \'%%\' || UPPER(%s) || \'%%\' and job_id = jobs.id and crew_id = crew.id'

    crew_list = []
    connection = get_connection()
    if connection is not None:
        try:
            for row in get_select_query_results(connection, query, (name, job,)):
                crew = {'id':row[0], 'name':row[1]}
                crew_list.append(crew)
        except Exception as e:
            print(e, file=sys.stderr)
        connection.close()

    return json.dumps(crew_list)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]))
        print('  Example: {0} perlman.mathcs.carleton.edu 5101'.format(sys.argv[0]))
        exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
    app.run(host=host, port=port, debug=True)
