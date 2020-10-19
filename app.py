from flask import Flask,render_template,request,redirect,url_for
import requests,json


app = Flask(__name__)

@app.route("/")
def base():
    return render_template("extender.html")

@app.route('/search/<movie_q>')
def movie_search(movie_q):
    movie_q=movie_q.lower()
    resp = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key=b1a92c686f2982862df95e0cdf1b9c38&language=en-US&query={movie_q}&page=1&include_adult=false')
    resp_json = resp.json()
    json_movie_list=[]
    for movie in resp_json['results']:
        json_movie_details = {'title':movie["original_title"], 'overview':movie['overview'], 'poster':'http://image.tmdb.org/t/p/w500'+movie["poster_path"]}
        json_movie_list.append(json_movie_details)

    return render_template( 
        'recommended-movies.html',
        mvlist = json_movie_list,
    )


@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user",usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == "__main__":
    app.run(debug=True)


