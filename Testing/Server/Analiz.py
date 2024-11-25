import json


class Analiz:
    result_user = []

    @classmethod
    def Estimation(cls, correctAnswer, answer):
        a = 0
        for i in range(len(correctAnswer)):
            if correctAnswer[i] == answer[i]:
                a += 1
        return a


    @classmethod
    def Qustions(cls,group,name):
        #Tk().withdraw()
        #filename = askopenfilename()

        filename = 'C:/Users/MACTECTBO/Desktop/result.txt'

        try:
            f = open(filename, 'r')
            data = f.readlines()

            send_data = []
            recv_data = []

            s1,s2 = [],[]

            for s in data:
                s1.append(json.loads(s)[0])
                s2.append(json.loads(s)[1])

                recv_data.append(json.loads(s)[2])

            send_data.append([s1,s2])
            cls.result_user.append([group,name,recv_data])

            print(send_data)

            return send_data

        except FileNotFoundError:
            print('путь не выбран')


if __name__ == '__main__':
    print(json.dumps([['Вопрос №1'], ['1', '2', '3', '4'],['1']]))
    print(json.dumps([['Вопрос №2'], ['1', '2', '3', '4'], ['2']]))
    print(json.dumps([['Вопрос №3'], ['1', '2', '3', '4'], ['3']]))
    print(json.dumps([['Вопрос №4'], ['1', '2', '3', '4'], ['4']]))

    Analiz.Qustions(42215,'Egor')
    print(Analiz.result_user)