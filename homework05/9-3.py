﻿
from tkinter import *
width = 300
height= 50
class MainGUI:
    def display(self):
        self.canvas.delete('shape')
        if self.filled.get() == 1:
            if self.v.get() == 1:
                self.canvas.create_rectangle(width/2-width*0.4, height/2-height*0.4,
                                     width/2+width*0.4, height/2+height*0.4, tags='shape', fill='red')
            else:
                self.canvas.create_oval(width/2-width*0.4, height/2-height*0.4,
                                     width/2+width*0.4, height/2+height*0.4, tags='shape', fill='red')
        else:
            if self.v.get() == 1:
                self.canvas.create_rectangle(width/2-width*0.4, height/2-height*0.4,
                                     width/2+width*0.4, height/2+height*0.4, tags='shape')
            else:
                self.canvas.create_oval(width/2-width*0.4, height/2-height*0.4,
                                     width/2+width*0.4, height/2+height*0.4, tags='shape')

    def __init__(self):
        window=Tk()
        window.title('투자금계산')
        self.canvas=Canvas(window,bg='white',width=width,height=height)
        self.canvas.create_rectangle(width/2-width*0.4, height/2-height*0.4,
                                     width/2+width*0.4, height/2+height*0.4, tags='shape')
        self.canvas.pack()

        frame=Frame(window)
        frame.pack()
        self.v = IntVar()
        Radiobutton(frame,text='직사각형',variable=self.v, value=1,command=self.display).pack(side=LEFT)
        Radiobutton(frame,text='타원',variable=self.v, value=2,command=self.display).pack(side=LEFT)
        self.filled = IntVar()
        Checkbutton(frame,text='채우기',variable=self.filled, command=self.display).pack(side=LEFT)

        window.mainloop()

MainGUI()