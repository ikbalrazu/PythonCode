import requests
import json

URL = "http://127.0.0.1:8000/teachertable/"
def get_data(id=None):
    data = {}
    if id is None:
        data = {'id':id}
    json_data = json.dumps(data)
    print("json data")
    r = requests.get(url=URL,data=json_data)
    print("not worked")

    data = r.json()
    print(data)
get_data()
