from flask import Flask
import requests
app = Flask(__name__)

HTML ="""<!DOCTYPE HTML>
     <html>
        <head><title>Movie by search</title></head>
        <body>
            <h1>A page title.</h1>
            <div>@@@overview@@@ </div>
            <div><img src="@@@poster_img@@@" alt="movie poster"></div>
        </body>
    </html>

"""

@app.route('/<movie_q>')
def hello_world(movie_q):
    movie_q=movie_q.lower()
    resp = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key=b1a92c686f2982862df95e0cdf1b9c38&language=en-US&query={movie_q}&page=1&include_adult=false')
    resp_json = resp.json()
    poster = resp_json['results'][0]["poster_path"]
    overview = resp_json['results'][0]["overview"]
    #movie_id = resp_json['results'][0]["id"]
    #print(poster)
    poster2 = requests.get(f'http://image.tmdb.org/t/p/w500/{poster}')

    result = HTML.replace("@@@poster_img@@@", poster)
    result =HTML.replace("@@@overview@@@", overview)
    return result
    
