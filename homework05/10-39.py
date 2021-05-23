﻿
from tkinter import *
from tkinter.simpledialog import *

from random import *
width = 800
height= 600
barWidth = (width-20)/20

class MainGUI:
    def refresh(self):
        shuffle(self.index)
        for i in range(4):
            self.labelList[i]['image'] = self.imageList[self.index[i]]
    def check(self):
        fourCards = []
        for i in range(4):
            fourCards.append(self.index[i]%13)
        fourCards.sort()
        fourCards = [x+1 for x in fourCards]
        ex = self.answer.get()
        ex = ex.replace('+',' ')
        ex = ex.replace('-',' ')
        ex = ex.replace('*',' ')
        ex = ex.replace('/',' ')
        ex = ex.replace('(',' ')
        ex = ex.replace(')',' ')
        numbers = ex.split()
        numbers = [eval(x) for x in numbers]
        numbers.sort()
        print(numbers)
        print(eval(self.answer.get()))
        if fourCards == numbers:
            if eval(self.answer.get())== 24:
                tkinter.messagebox.showerror("맞음", "맞았습니다.")
            else:
                tkinter.messagebox.showerror("틀림", self.answer.get()+"는 24가 아닙니다..")

        else:
                tkinter.messagebox.showerror("틀림", "보여지는 카드를 사용해야 됩니다.")

    def __init__(self):
        window=Tk()
        window.title('24점게임')
        self.index=[x for x in range(52)]
        self.imageList=[]
        for i in range(1,53):
            self.imageList.append(PhotoImage(file='card/'+str(i)+'.gif'))
        frame=Frame(window)
        frame.pack()
        Button(frame,text='새로고침',command=self.refresh).pack()
        frame2=Frame(window)
        frame2.pack()
        self.labelList=[]
        for i in range(4):
            self.labelList.append(Label(frame2, image=self.imageList[i]))
            self.labelList[i].pack(side=LEFT)
        self.refresh()

        frame3 = Frame(window)
        frame3.pack()
        Label(frame3, text="수식을 입력하세요:").pack(side=LEFT)
        self.answer=StringVar()
        Entry(frame3, textvariable=self.answer).pack(side=LEFT)
        Button(frame3,text='확인',command=self.check).pack()

        window.mainloop()

MainGUI()