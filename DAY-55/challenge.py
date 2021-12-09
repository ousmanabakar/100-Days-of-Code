from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


def make_bold(func):
    def wrapper():
        return f"<b>{func()}</b>"

    return wrapper


def make_emphasis(func):
    def wrapper():
        return f"<em>{func()}</em>"

    return wrapper


def make_underline(func):
    def wrapper():
        return f"<u>{func()}</u>"

    return wrapper


# Different route by using @app.route decorator
@app.route('/bye')
@make_bold
@make_emphasis
@make_underline
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
