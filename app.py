from datetime import timedelta
from time import sleep

from flask import Flask



def create_app():
    from jobs import rq
    app = Flask(__name__)
    rq.init_app(app)
    return app


app = create_app()


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/add/<int:x>/<int:y>')
def add(x, y):
    from jobs import calculate
    job = calculate.queue(x, y)
    return "ok!"

if __name__ == '__main__':
    app.run()