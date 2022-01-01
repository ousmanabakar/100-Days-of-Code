from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Hello contact</h1>"


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/contact", methods=["GET", "POST"])
def get_data():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


if __name__ == "__main__":
    app.run(debug=True)