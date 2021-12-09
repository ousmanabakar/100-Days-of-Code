from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style ="text-align:center" >Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media.giphy.com/media/K1wjOn6HImv7y/giphy.gif" width="200">' \
           ''


# Different route by using @app.route decorator
@app.route('/bye')
def bye():
    return "Bye!"


# Creating variable path and converting the path to a specific data  type
@app.route('/<name>')
def greet1(name):
    return f'Hello dear {name} welcome!'


@app.route('/<name>/<int:number>')
def greet2(name, number):
    return f'Hello {name} you are {number} years old!'


if __name__ == "__main__":
    app.run(debug=True)
