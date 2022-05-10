from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap5 import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///groups.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(20), nullable=False)
    img_url = db.Column(db.String(120), nullable=False)


    def __repr__(self):
        return f'<Group {self.title}>'
# db.create_all()
#
# new_group = Group(id=1, title="MAMAMOO", year=2014, description="Mr. Ambiguous", rating=4, ranking=1, review="Their debut was considered by some critics as one of the best K-pop debuts of 2014.[4][5] They are recognized for their retro, jazz, R&B concepts and their strong vocal performances", img_url="https://i.pinimg.com/236x/e6/c2/1f/e6c21fc3f7e4012c0cdacef59b6f050d.jpg")
# db.session.add(new_group)
# db.session.commit()

@app.route("/")
def home():
    return render_template("index.html", groups=db.session.query(Group).all())

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # CREATE RECORD
        new_group = Group(
            title=request.form["title"],
            year=request.form["year"],
            description=request.form["description"],
            rating=request.form["rating"],
            ranking=request.form["ranking"],
            review=request.form["review"],
            img_url=request.form["img_url"],

        )
        db.session.add(new_group)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")

if __name__ == '__main__':
    app.run(debug=True)
