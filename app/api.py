from app import app

from service import JWT
from app import *

from settings import env
tokin_service = JWT.tokinService(env)


# resp.set_cookie('sessionID', '', expires=0)   #Сбросить куки



@app.route('/api/v0.1/login', methods=['POST', "GET"])
def api_jwt_get():
    
    if request.cookies.get('refreshToken'):
        abort(405)
    if not request.cookies.get('refreshToken'):
        f = json.loads(request.data.decode())
        jwts = tokin_service.generateTokins({"dq":'qwe'})
        res = make_response({'accessToken' : jwts[0]})
        res.set_cookie('refreshToken', jwts[1], 60*24*30)

        # sql Обновить refreshToken в базе

    return res

@app.route('/api/v0.1/users', methods=['POST', "GET"])
def test():  
    f = json.loads(request.data.decode())
    if('refreshToken' in f):
        jwts = tokin_service.decodeTokins('REFRESH', f['refreshToken'])
    # print('qq', f['accessToken'])
    elif('accessToken' in f):
        jwts = tokin_service.decodeTokins('ACCESS', f['accessToken'])
    else:
        abort(400)
    # print(jwts)
    return(jwts)