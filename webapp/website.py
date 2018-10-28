#!/usr/bin/env python3
'''
    website.py
    Max Goldberg and Alexis Engel
    10/30/2018
'''
import sys
import flask

app = flask.Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/') 
def get_main_page():
    global api_port
    return flask.render_template('index.html', api_port=api_port)

@app.route('/movie')
def get_movie_page():
    global api_port
    return flask.render_template('movie.html', api_port=api_port)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: {0} host port api-port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    api_port = sys.argv[3]
    app.run(host=host, port=port)

