import json

from DataBase.DataBase import Connector
from flask import Flask

from Testing.Server.Analiz import Analiz

app = Flask(__name__)


@app.route('/connect/<GROUP>/<NAME>/')
def Connect(GROUP:int ,NAME):
    if not (Connector.Select_User("count(*)",f" WHERE Name = '{NAME}'")):
        Connector.Insert_User(GROUP,NAME)

    return Analiz.Qustions(GROUP,NAME)


@app.route('/send/<GROUP>/<NAME>/<RESULT>/')
def Send(GROUP: int, NAME, RESULT):
    print('Результат анализа')
    RESULT = json.loads(RESULT)

    for i, res in enumerate(Analiz.result_user):
        if res[0] == GROUP and res[1] == NAME:
            print(res[2], RESULT)
            return json.dumps(Analiz.Estimation(res[2], RESULT))


if __name__ == "__main__":
    app.run()