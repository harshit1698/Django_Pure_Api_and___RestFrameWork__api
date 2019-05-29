import requests
import json
import os

BASE_URL = "http://127.0.0.1:8000/rest/all/"
img = os.path.join(os.getcwd(),"yo.jpg")


def do(method='get',data={},is_json=True,img_path=None):
    headers = {}
    if is_json:
        headers['content-type']="application/json"
        data = json.dumps(data)
    if img_path is not None:
        with open(img,'rb') as image:
            file_data={"image":image}
            r = requests.request(method,BASE_URL,data=data,files=file_data)
            return r


print(do(method='post',data={"name":"YoBoy22","age":22},is_json=False,img_path=img))


