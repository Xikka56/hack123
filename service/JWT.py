import jwt
import json
import base64
import time

# from settings import env

# JWT_ACCESS_SECRET = env.JWT_ACCESS_SECRET
# JWT_REFRESH_SECRET = env.JWT_REFRESH_SECRET


class tokinService():
    def __init__(self, env):
        """ Конструктор 
        
        При создание принимает ключ шифровки
        """
        self.JWT_ACCESS_SECRET = env.JWT_ACCESS_SECRET
        self.JWT_REFRESH_SECRET = env.JWT_REFRESH_SECRET


    def generateTokins(self, payload) -> json:
        data = { "payload":{
            'data': payload,
            'expiresIn': '30m',
            'time_create': time.time()
        }}
        ACCESS = jwt.encode(data, self.JWT_ACCESS_SECRET, algorithm="HS256")

        data['payload']['expiresIn'] = '30d'
        
        REFRESH = jwt.encode(data, self.JWT_REFRESH_SECRET, algorithm="HS256")


        return(ACCESS, REFRESH)


    
    def decodeTokins(self, type_sc:str = 'ACCESS', JWT_cod:str = '') -> json:
        if(type_sc =="ACCESS"):
            q = jwt.decode(JWT_cod, self.JWT_ACCESS_SECRET, algorithms=["HS256"])
        else:
            q = jwt.decode(JWT_cod, self.JWT_REFRESH_SECRET, algorithms=["HS256"])
        return(q)
        

# accessToken = tokinService.generateTokins(None, {'data':{'dasq':{'dqw'}}})

# print(accessToken)
# q = tokinService.decodeTokins(None, 'ACCESS', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXlsb2FkIjoiZXlKa2NTSTZJQ0p4ZDJVaWZRPT0iLCJleHBpcmVzSW4iOiIzMGQiLCJ0aW1lX2NyZWF0ZSI6MTYyMzY5OTY3MS4zNDUxMjIzfQ.1wigEtcyDOJLDQr3-pr9tTpfGF_q9iwO71GPSsTGpZk')

# print(q)