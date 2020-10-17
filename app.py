from flask import Flask,render_template
import requests
app = Flask(__name__)



@app.route('/<movie_q>')
def hello_world(movie_q):
    movie_q=movie_q.lower()
    resp = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key=b1a92c686f2982862df95e0cdf1b9c38&language=en-US&query={movie_q}&page=1&include_adult=false')
    resp_json = resp.json()
    poster = resp_json['results'][0]["poster_path"]
    overview = resp_json['results'][0]["overview"]
    #movie_id = resp_json['results'][0]["id"]
    #print(poster)
    posterquery = 'http://image.tmdb.org/t/p/w500'+poster

    return render_template(
        'one-movie.html',
        overview=overview,
        poster_query=posterquery,
    )
