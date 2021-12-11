import datetime
import random
import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    get_date = datetime.datetime.now().year
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, current_date=get_date)


@app.route("/guess/<name>")
def name_guess(name):
    age = requests.get(f"https://api.agify.io?name={name}").json()['age']
    gender = requests.get(f"https://api.genderize.io?name={name}").json()['gender']

    return render_template("guess.html", name=name, age=age, gender=gender)


@app.route("/blog")
def get_blog():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blog.html", post=response)


if __name__ == "__main__":
    app.run(debug=True)
