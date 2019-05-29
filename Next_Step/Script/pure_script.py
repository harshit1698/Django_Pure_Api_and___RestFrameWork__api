import json

import requests

FROND_END="http://127.0.0.1:8000/pure/"


def get(id=None):
    if id is None:
        URL=FROND_END+"get/"
        res = requests.get(URL)
        return res.json()
    URL=FROND_END+"yo/"+str(id)+"/"
    res = requests.get(URL)
    return res.json()


def post():
    data={"name":"Harshit Trivedi" , "rship":16}
    Url="http://127.0.0.1:8000/pure/post/"
    res=requests.post(Url,data=json.dumps(data))
    return res.json()


def delete(id):
    if id is not None:
        E_P = "pure/del/" + str(id) + "/"
        r = requests.delete(FRONT_END + E_P)
        return r.json()


def put(id=None):
    # data = {"name": "Harshit_Pihu", "rship": 6}
    E_P = "http://127.0.0.1:8000/pure/del/" + str(id) + "/"
    r = requests.delete(E_P)
    return r.json()


# print(post())

