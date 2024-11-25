import json
import requests


def Connect(data: str):
    reasponse = requests.get(data)

    data = json.loads(reasponse.text)
    return data


def Send(data: tuple):
    data = json.dumps(data)
    reasponse = requests.get(f'http://127.0.0.1:5000/send/42215/egor/{data}')

    print(reasponse.status_code)

    return json.dumps(reasponse.text)



if __name__ == '__main__':
    Connect('http://127.0.0.1:5000/connect/42215/egor/')