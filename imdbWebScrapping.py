from flask import Flask, render_template, request, url_for
from bs4 import BeautifulSoup
import requests
from werkzeug.utils import redirect

app = Flask(__name__)

# @app.route('/')
# def inputMovieNumber():
#     # if(request.method)
#     return render_template('imdbScrapping.html')

@app.route('/', methods=["GET", "POST"])
def search():
    if request.method == "POST":
        inputNumber = request.form["mNumber"]
        sourceUrl = "https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&count="
        details = requests.get(sourceUrl + inputNumber)
        soup = BeautifulSoup(details.text, 'lxml')
        movies_list = soup.find_all("div", {"class": "lister-item mode-advanced"})

        # return redirect(url_for("inputNumber", movieNumber=inputNumber))
        return render_template("display.html", allMovies=movies_list)
    else:
        return render_template('imdbScrapping.html')

# @app.route('/<movieNumber>')
# def inputNumber(movieNumber):
#     return f'<h1> {movieNumber} </h1>'

# @app.route('/display', methods=["GET", "POST"])
# def display(inputNumber):
#     # return f'<h1> {movieNumber} </h1>'
#     return render_template('display.html', value=inputNumber)

if __name__ == '__main__':
  app.run()