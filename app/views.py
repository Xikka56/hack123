from app import app

from service import JWT

@app.route('/')
@app.route('/index')
def index():
    JWT.q()
    return "Hello, World!"