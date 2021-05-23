from tkinter import *

class MainGUI:
    def up(self):
        if self.y <= 0:
            return
        self.y -= 5
        self.canvas.move('ball',0,-5)
    def down(self):
        if self.y >= self.height:
            return
        self.y += 5
        self.canvas.move('ball',0,5)
    def left(self):
        self.x -= 5
        if self.x < 0:
            self.x += 5
            return
        self.canvas.move('ball',-5,0)
    def right(self):
        self.x += 5
        if self.x > self.height:
            self.x -= 5
            return
        self.canvas.move('ball',5,0)
    def __init__(self):
        window = Tk()
        window.title("moveball")
        self.width=200
        self.height=100
        self.x = 10
        self.y = 10
        self.canvas=Canvas(window, bg="white",width=self.width,height=self.height)
        self.canvas.pack()
        self.canvas.create_oval(10,10,20,20,fill='red',tags='ball')
        frame=Frame(window)
        frame.pack()
        Button(frame, text='u',command=self.up).pack(side=LEFT)
        Button(frame, text='d',command=self.down).pack(side=LEFT)
        Button(frame, text='l',command=self.left).pack(side=LEFT)
        Button(frame, text='r',command=self.right).pack(side=LEFT)

        window.mainloop()

MainGUI()