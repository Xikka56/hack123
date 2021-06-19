from app import *

from service import JWT

from settings import env
tokin_service = JWT.tokinService(env)


@app.route('/')
def index():
    # asd
    # jwts = tokin_service.generateTokins({"dq":'qwe'})
    return render_template('dq.html')


@app.route('/main')
def maps():
    print(request.remote_addr)
    # asd
    # jwts = tokin_service.generateTokins({"dq":'qwe'})
    return render_template('swiper.html')

