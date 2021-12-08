from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def bye():
    return "Bye!"

@app.route('/<name>')
def greet(name):
    return f'Hello dear {name} welcome!'


if __name__ == "__main__":
    app.run(debug=True)
