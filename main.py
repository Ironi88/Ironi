from flask import Flask
from flask import render_template
from flask import url_for
import random

app = Flask(__name__)

@app.route("/")
def hello():

    names = ['Fabian', "Wolfgang", "Michael", "Cristina", "Meret"]
    name_choice = random.choice(names)
    about_link = url_for("about")
    return render_template("index.html", name=name_choice, link=about_link)


@app.route("/about")
def about():
    return "About test"


if __name__ == "__main__":
    app.run(debug=True, port=5000)

