from flask import Flask, render_template
import random
from datetime import date
import requests

URL_GENDER = 'https://api.genderize.io?name'
URL_AGE = 'https://api.agify.io?name'
app = Flask(__name__)

@app.route('/')
def home():
    num = random.randint(1, 12)
    year = date.today().year
    return render_template('index.html', num=num, year=year)

@app.route('/guess/<name>')
def guess(name):
    response_gender = requests.get(f'{URL_GENDER}={name}')
    response_age = requests.get(f'{URL_AGE}={name}')
    return render_template('guess.html', gender=response_gender.json()['gender'], age=response_age.json()['age'])

if __name__ == "__main__":
    app.run(debug=True)