from app import app

from service import JWT
from app import *
import pymysql

from settings import env
tokin_service = JWT.tokinService(env)


class DB():
    """Работа с Базой данных
    получить данные::

        DB.GET('Текст запроса SQL')
    отправить данные::

        DB.POST('Текст запроса SQL')
    """

    def GET(self):
        """Получает данные с Базы данных
        """
        connection = pymysql.connect(host="31.31.196.245", user='u0981115',
                                     password='qwert5656', database='u0981115_hack123', charset="utf8mb4")
        cursor = connection.cursor()
        cursor.execute(self)
        OTV = cursor.fetchall()
        return(OTV)

    def POST(self):
        """Отправляет данные в Базу данных
        """
        connection = pymysql.connect(host="31.31.196.245", user='u0981115',
                                     password='qwert5656', database='u0981115_hack123', charset="utf8")
        cursor = connection.cursor()
        cursor.execute(self)
        connection.commit()
        return('True')

# resp.set_cookie('sessionID', '', expires=0)   #Сбросить куки


@app.route('/api/v0.1/login', methods=['POST', "GET"])
def api_jwt_get():
    if request.cookies.get('refreshToken'):
        abort(405)
    if not request.cookies.get('refreshToken'):
        f = json.loads(request.data.decode())
        jwts = tokin_service.generateTokins({"dq": 'qwe'})
        res = make_response({'accessToken': jwts[0]})
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
    0: {
        'title': 'Вечериночка',
        'data': '12/07/2020',
        'type': 'ТУСА'
    },
    1: {
        'title': 'Футбик',
        'data': '12/07/2020',
        'type': 'СПОРТ'
    },
    2: {
        'title': 'Рыбалочка',
        'data': '25/07/2020',
        'type': 'ОТДЫХ'
    }
}


@app.route('/api/v0.1/get_slides', methods=['POST', "GET"])
def get_slides():
    # asd
    if(request.data):
        data = json.loads(request.data.decode())
        print("data", data)
        if(data["count"] != 0):
            m_end = []
            get_by_type = ""
            if(data["type"]):
                print(data["type"])
                get_by_type = f"""WHERE`type` = '{data["type"]}' """

            for el in range(data['count']):
                m_end.append(
                    DB.GET(f"""SELECT * FROM `slides` {get_by_type}""")[0])
        # jwts = tokin_service.generateTokins({"dq":'qwe'})
        return {
            'mass_data': m_end
        }
    return('false')


# @app.route('/api/v0.1/get_slides', methods=['POST'])
# def get_slides():
#     f = json.loads(request.data.decode())

#     slide = DB.GET("""SELECT * FROM `slides`""")[0]
#     print(slide)
#     f = {slide[0]}
#     print(f)
#     return f, 200
