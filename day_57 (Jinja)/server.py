import datetime
import requests
from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def hello():
    years = datetime.date.today().year
    return render_template('index-demo.html', year=years)
@app.route("/guess/<name>")
def guessing(name):
    link = "https://api.genderize.io"
    parameter = {
        'name': name
    }
    response = requests.get(link, params=parameter)
    gender = response.json()['gender']
    return render_template('index.html', gender=gender)
    # return gender['gender']

if __name__ == "__main__":
    app.run(debug=True)
