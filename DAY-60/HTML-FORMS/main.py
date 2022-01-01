from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def get_data():
    name = request.form['username']
    password = request.form['password']
    return f"<h1> Name: {name}, Password: {password}</h1>"


if __name__ == "__main__":
    app.run(debug=True)


# NOTE: The action attribute of the form can be set to "/login" e.g.
#
# <form action="/login" method="post">
# or it can be dynamically generated with url_for e.g.
# <form action="{{ url_for('receive_data') }}" method="post">
# Depending on where your server is hosted, the "/login" path may change.
# So it's usually a better idea to use url_for to dynamically generate ' \
#'the url for a particular function in your Flask server.



