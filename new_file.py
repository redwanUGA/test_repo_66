from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hi():
    return 'hi'

if __name__ == '__main__':
    app.run()
