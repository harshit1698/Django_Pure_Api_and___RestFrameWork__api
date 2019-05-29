import requests
import json

from django.core.serializers import serialize

# from pure_api.models import RK

FRONT_END = "http://127.0.0.1:8000/rest/all/"
AUTH="http://127.0.0.1:8000/api/jwt/"
a1="http://127.0.0.1:8000/refresh/"
END_POINT = "pure/get/"


def auth():
    data = {"username":"YO","password":"abc@1234"}
    headers = {"Content-Type":"application/json"}
    r=requests.post(AUTH,data=json.dumps(data),headers=headers)
    token = r.json()
    # d1={"token":token}
    # r2=requests.post(a1,data=json.dumps(d1),headers=headers)
    return token


def get(id=None):
    if id is None:
        r = requests.get(FRONT_END + END_POINT)
        return r.json()
    else:
        E_P = "pure/get/" + str(id) + "/"
        r = requests.get(FRONT_END + E_P)
        return r.json()


def post():
    data = {"name": "Hey priyanka babe holaa", "age": 12,"image":None}
    # E_P = "pure/post/"
    data1 = {"username": "yo", "password": "abc@1234"}
    headers = {"Content-Type": "application/json"}
    r = requests.post(AUTH, data=json.dumps(data1), headers=headers)
    token = r.json()['token']
    print(token)
    # FRONT_EN FRONT_END
    head = {'content-type':'application/json',"Authorization":"JWT "+token}
    r = requests.post(FRONT_END,data=json.dumps(data),headers=head)
    return r.json()



def delete(id):
    if id is not None:
        E_P = "pure/del/" + str(id) + "/"
        r = requests.delete(FRONT_END + E_P)
        return r.json()


def put(id=None):
    data = {"name": "Harshit_Pihu", "rship": 6}
    E_P = "pure/put/" + str(id) + "/"
    r = requests.put(FRONT_END + E_P, data=data)
    return r.json()


# def yo(id):
#     o1 = RK.objects.get(id=id)
#     old = json.loads(serialize("json", [o1, ]))
#     return old


# print(put(12))
# print(auth())
print(post())
# print(auth())
