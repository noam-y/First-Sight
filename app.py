from flask import Flask,render_template,request,redirect,url_for
import requests,json
import pdb
API_KEY ='b1a92c686f2982862df95e0cdf1b9c38'
app = Flask(__name__)



suggested ={
    "Latest" : f"https://api.themoviedb.org/3/movie/latest?api_key={API_KEY}&language=en-US",
    "Upcoming" : f"https://api.themoviedb.org/3/movie/upcoming?api_key={API_KEY}&language=en-US&page=1",
    "Trending" : f"https://api.themoviedb.org/3/trending/all/day?api_key={API_KEY}"

}

@app.route('/', methods =['POST','GET'])
def homepage():
    if request.method == 'POST':
        text_search = request.form['searchtext']
        return redirect(url_for("movie_search",movie_q=text_search))
    else:
        return render_template('index.html')


@app.route('/suggested-list')
def get_suggested_lists():
    buttonclicked = request.args.get('buttonclicked')
    search_query = suggested[buttonclicked]

    if buttonclicked == 'Latest':
        resp = requests.get(search_query)
        resp_json = resp.json()
        return sort_one_movie(resp_json, single=True)
    else:
        return sort_out_movies(search_query)


    return f'<h1>{buttonclicked} </h1>'



@app.route('/name-search',methods=['POST','GET'])
def movie_search():
    if request.method == 'POST':
        movie_q = request.form.get('searchtext')
        search_query = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=en-US&query={movie_q}&page=1&include_adult=false'
        return sort_out_movies(search_query)

    else:
        return redirect(url_for('homepage'))


@app.route("/C-search",methods=['POST','GET'])
def category_search():
    if request.method == 'POST':
        genres = ','.join(request.form.getlist('genres'))
        include_adult = request.form.get('agelimit') != None
        time_limit =  request.form.get('length') 
        search_query = f'https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&include_adult={include_adult}&with_genres={genres}&page=1'

        #checks that time limit input is valid
        if time_limit != '':
            search_query = search_query+ f'&with_runtime.lte={time_limit}'

        return sort_out_movies(search_query)  

    else:
        return '<p>Try again.!!!</p>'






def sort_out_movies(search_query):
        resp = requests.get(search_query)
        resp_json = resp.json()

        json_movie_list=[]
        for movie in resp_json['results']:
            json_movie_list.append(sort_one_movie(movie))

        return render_template( 
            'recommended-movies.html',
            mvlist = json_movie_list,
        )


def sort_one_movie(movie, single = False):
    if 'title' in movie:
        try:
            json_movie_details = {'title':movie["title"], 'overview':movie['overview'], 'poster':'http://image.tmdb.org/t/p/w500'+movie["poster_path"]}
        except(TypeError):
            json_movie_details = {'title':movie["title"], 'overview':movie['overview'], 'poster':'https://www.onlygfx.com/wp-content/uploads/2017/11/grunge-question-mark-2-148x300.png'}

    else:
        try:
            json_movie_details = {'title':movie["name"], 'overview':movie['overview'], 'poster':'http://image.tmdb.org/t/p/w500'+movie["poster_path"]}
        except(TypeError):
            json_movie_details = {'title':movie["name"], 'overview':movie['overview'], 'poster':'https://www.onlygfx.com/wp-content/uploads/2017/11/grunge-question-mark-2-148x300.png'}


    if single:
        return render_template(
            'onemovie.html',
            mv =json_movie_details,
        )
    else:
        return json_movie_details
            





if __name__ == "__main__":
    app.run(debug=True)
