import asyncio
import threading
from tkinter import *
from Testing.Client.Client import Client


class GUI:
    def __init__(self):
        self.CorrectAnswers = 0

        self.root = Tk()
        self.root.geometry('750x750')

        self.buttonNewTest = Button(text='Запустить',command=self.StartAsync)
        self.buttonNewTest.place(x=250,y=250)

        self.client = Client('127.0.0.1',3000)

        self.root.mainloop()


    def StartAsync(self):
        asyncio.run(self.client.Connect())
        self.Start()


    def Start(self):
        self.buttonNewTest.destroy()
        data = self.client.data

        print(data[0][0])

        self.enabled1 = IntVar()
        self.enabled2 = IntVar()
        self.enabled3 = IntVar()
        self.enabled4 = IntVar()


        self.Button_Continie = Button(text='Продолжить', command=self.SaveAnswer, width=30)

        self.question = Text(wrap='word', width=88, height=7)
        self.question.insert('1.0',data[0])
        self.question.config(state=DISABLED)

        self.answer1 = Text(wrap='word', width=60, height=7)
        self.answer1.insert('1.0',data[1][0])
        self.answer1.config(state=DISABLED)

        self.answer2 = Text(wrap='word', width=60, height=7)
        self.answer2.insert('1.0', data[1][1])
        self.answer2.config(state=DISABLED)

        self.answer3 = Text(wrap='word', width=60, height=7)
        self.answer3.insert('1.0', data[1][2])
        self.answer3.config(state=DISABLED)

        self.answer4 = Text(wrap='word', width=60, height=7)
        self.answer4.insert('1.0', data[1][3])
        self.answer4.config(state=DISABLED)


        self.option1 = Checkbutton(text="1", variable=self.enabled1, wraplength=150)
        self.option1.place(x=520,y=200)

        self.option2 = Checkbutton(text="2", variable=self.enabled2, wraplength=150)
        self.option2.place(x=520, y=300)

        self.option3 = Checkbutton(text="3", variable=self.enabled3, wraplength=150)
        self.option3.place(x=520, y=400)

        self.option4 = Checkbutton(text="4", variable=self.enabled4, wraplength=150)
        self.option4.place(x=520, y=500)


        self.question.place(x=20,y=20)

        self.answer1.place(x=20,y=170)
        self.answer2.place(x=20,y=270)
        self.answer3.place(x=20, y=370)
        self.answer4.place(x=20, y=470)

        self.Button_Continie.place(x=300,y=650)


    def SaveAnswer(self):
        if self.enabled1.get() == self.client.data[2][0] and self.enabled2.get() == self.client.data[2][1] and self.enabled3.get() == self.client.data[2][2] and  self.enabled4.get() == self.client.data[2][3]:
              self.CorrectAnswers += 1



        '''print(self.enabled1.get(),self.enabled2.get(),self.enabled3.get(),self.enabled4.get())
        print(self.client.data)
        print(self.enabled1.get() == self.client.data[2][0] and
              self.enabled2.get() == self.client.data[2][1] and
              self.enabled3.get() == self.client.data[2][2] and
              self.enabled4.get() == self.client.data[2][3])
        '''




if __name__ == '__main__':
    GUI()