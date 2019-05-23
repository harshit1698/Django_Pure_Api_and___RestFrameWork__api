import requests
import json

from django.core.serializers import serialize

# from pure_api.models import RK

FRONT_END = "http://127.0.0.1:8000/"
END_POINT = "pure/get/"


def get(id=None):
    if id is None:
        r = requests.get(FRONT_END + END_POINT)
        return r.json()
    else:
        E_P = "pure/get/" + str(id) + "/"
        r = requests.get(FRONT_END + E_P)
        return r.json()


def post():
    data = {"name": "Hey harshit", "rship": 22}
    E_P = "pure/post/"
    r = requests.post(FRONT_END + E_P, data=data)
    return type(r.json())


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


print(put(12))
