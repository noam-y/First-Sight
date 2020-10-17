from flask import Flask
import requests
app = Flask(__name__)

HTML ="""<!DOCTYPE HTML>
     <html>
        <head></head>
        <body>
            <h1>A page title.</h1>
            <div><img src="@@@poster@@@" alt="movie poster"></div>
        </body>
    </html>

"""

@app.route('/<movie_q>')
def hello_world(movie_q):
    movie_q=movie_q.lower()
    response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key=b1a92c686f2982862df95e0cdf1b9c38&language=en-US&query=2067&page=1&include_adult=false')
    resp_json = response.json()
    #poster = resp_json['results'][0]['poster_path']
    #return HTML.replace("@@@poster@@@", poster)
    return HTML
