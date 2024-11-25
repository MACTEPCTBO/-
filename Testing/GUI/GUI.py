import json

from tkinter import *
from Client.Client import Connect,Send



class GUI:
    your_answer = []

    answer = []
    option = []
    CorrectAnswer = 0

    def __init__(self):
        self.your_answer = []

        self.answer = []
        self.option = []

        self.data = []

        self.num_quetion = 0
        self.len_question = 0

        self.root = Tk()
        self.root.geometry('750x750')

        self.Name = Entry()
        self.Name.place(x=250,y=280)

        self.buttonNewTest = Button(text='Запустить',command=self.Start)
        self.buttonNewTest.place(x=250,y=250)

        self.root.mainloop()


    def Start(self):
        self.buttonNewTest.destroy()
        data = Connect('http://127.0.0.1:5000/connect/42215/egor/')
        self.len_question = len(data[0][0])


        self.enabled = []

        self.Button_Continie = Button(text='Продолжить', command= self.SaveAnswer, width=30)

        self.question = Text(wrap='word', width=88, height=7)

        self.question.insert('1.0',data[0][0][self.num_quetion])
        self.question.config(state=DISABLED)

        for i,text in enumerate(data[0][1][self.num_quetion]):
            self.enabled.append(IntVar())

            answer = Text(wrap='word', width=60, height=7)
            answer.insert('1.0', text)
            answer.config(state=DISABLED)

            option = Checkbutton(text=i+1, variable=self.enabled[i], wraplength=150)

            option.place(x=520, y=200 + i * 100)
            answer.place(x=20,y=200 + i * 100)

            self.option.append(option)
            self.answer.append(answer)



        self.question.place(x=20,y=20)

        self.Button_Continie.place(x=300,y=650)


    def SaveAnswer(self):
        print([self.answer[i].get("1.0",END) if self.enabled[i].get() == 1 else [] for i in range(len(self.enabled))])
        self.data.append([self.enabled[i].get() for i in range(len(self.enabled))])
        self.num_quetion += 1


        if (self.num_quetion == self.len_question):
            data = Send(self.data)
            self.Result(data)
        else:
            for i in range(len(self.option)):
                self.option[0].destroy()
                self.option.pop(0)

            for i in range(len(self.answer)):
                self.answer[0].destroy()
                self.answer.pop(0)

            self.question.destroy()
            self.Button_Continie.destroy()

            self.Start()



    def Result(self,data):
        self.Button_Continie.destroy()
        self.question.destroy()
        self.Name.destroy()

        for i in range(len(self.option)):
            self.option[0].destroy()
            self.option.pop(0)


        for i in range(len(self.answer)):
            self.answer[0].destroy()
            self.answer.pop(0)

        self.lbl1 = Label(text=f'ваш результат {data} баллов')
        self.lbl1.place(x=350,y=350)

        self.Button_return = Button(text='Назад',command=self.Delete)
        self.Button_return.place(x=350,y=400)

    def Delete(self):
        self.root.destroy()
        GUI()

if __name__ == '__main__':
    GUI()