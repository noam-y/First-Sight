from flask import Flask,render_template
import requests
app = Flask(__name__)

html =""" <!DOCTYPE HTML>
     <html>
        <head><title>Movie by search</title></head>
        <body >
            <h1>movie list</h1>

            <div style="display:grid; grid-template-columns: 1fr 1fr 1fr;">@@@mvlist@@@</div>

        </body>
    </html>
"""


@app.route('/<movie_q>')
def movie_search(movie_q):
    movie_q=movie_q.lower()
    resp = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key=b1a92c686f2982862df95e0cdf1b9c38&language=en-US&query={movie_q}&page=1&include_adult=false')
    resp_json = resp.json()
    #movie_title = resp_json['results'][0]["original_title"]

    all_movie_details = ''
    for movie in resp_json['results']:
        movie_details = render_template(
                'one-movie.html',
                movie_poster = 'http://image.tmdb.org/t/p/w500'+movie["poster_path"],
                movie_overview = movie["overview"],
            
        )

        print(movie_details)

        all_movie_details = all_movie_details + movie_details

    #all_movie_details = """{% extends "./templates/movie-list.html" %}
    #{% block themovies %}""" + all_movie_details + """ {% endblock %}"""
    toprint = html.replace("@@@mvlist@@@", all_movie_details)
    return toprint
    return render_template(
        'movie-list.html',
        mvlist = all_movie_details,
    )




