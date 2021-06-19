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




db = {
    0:{
        'title':'Вечериночка',
        'data':'12/07/2020',
        'type':'ТУСА'
    },
    1:{
        'title':'Футбик',
        'data':'12/07/2020',
        'type':'СПОРТ'
    },
    2:{
        'title':'Рыбалочка',
        'data':'25/07/2020',
        'type':'ОТДЫХ'
    }
}

@app.route('/api/v0.1/get_block', methods=['POST', "GET"])
def iget_blockdex():
    # asd
    if(request.data):
        f = json.loads(request.data.decode())
        print(f)
        if('count' in f):
            print(f['count'])
            m_end = []
            q = 0
            for el in range(f['count']):
                try:
                    m_end.append(db[q])
                    q += 1
                except:
                    q = 0
                    m_end.append(db[q])
                    q += 1
                # q += 1
            print(len(m_end))
        # jwts = tokin_service.generateTokins({"dq":'qwe'})
        return {
            'mass_data':m_end
        }
    return('false')
