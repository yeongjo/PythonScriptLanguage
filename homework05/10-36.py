
from tkinter import *
from tkinter.simpledialog import *

from random import *
width = 800
height= 600
barWidth = (width-20)/20

class MainGUI:
    def next(self):
        key = int(self.key.get())
        self.canvas.delete('current_bar')
        self.canvas.create_rectangle(10+self.current*barWidth,height-(height-10)*self.counts[self.current]/self.maxCount,
                                            10+(self.current+1)*barWidth,height-10,tags='current_bar',fill='red')
        if key == self.counts[self.current]:
            messagebox.showinfo("찾았다","{0}".format(key))
        else:
            self.current +=1

    def reGen(self):
        self.canvas.delete('histogram')
        self.counts = [x for x in range(1,21)]
        shuffle(self.counts)
        self.current = 0
        self.maxCount = max(self.counts)
        for i in range(20):
            self.canvas.create_rectangle(10+i*barWidth,height-(height-10)*self.counts[i]/self.maxCount,
                                            10+(i+1)*barWidth,height-10,tags='histogram')
            self.canvas.create_text(10+i*barWidth+10,height-5, text=chr(i+ord('a')),tags='histogram')
            self.canvas.create_text(10+i*barWidth+10,height-(height-10)*self.counts[i]/self.maxCount-5,
                                    text=str(self.counts[i]),tags='histogram')
    def __init__(self):
        window=Tk()
        window.title('문자의 개수 세기')
        self.canvas=Canvas(window,bg='white',width=width,height=height)
        self.canvas.pack()
        frame=Frame(window)
        frame.pack()
        Label(frame,text='키를 입력하세요: ').pack(side=LEFT)
        self.key = IntVar()
        Entry(frame,textvariable=self.key,justify=RIGHT,width=3).pack(side=LEFT)
        Button(window,text='다음단계',command=self.next).pack()
        Button(window,text='재설정',command=self.reGen).pack()
        window.mainloop()

MainGUI()