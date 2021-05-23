import tkinter
import tkinter.filedialog

window=tkinter.Tk()
window.title("hi")
window.geometry("640x480+100+100")

frame = tkinter.Frame(window)


def openfile():
    name = tkinter.filedialog.askopenfilename()
    pathEntry.delete(0,'end')
    pathEntry.insert(0,name)
    return name

def printToListBox(idx, char, count):
    listbox.insert(idx, str(f"{char} - {count}번 나타납니다."))

def recalculate():
    listbox.delete(0, listbox.size()-1)
    filepath = pathEntry.get()
    if filepath == '':
        return
    file = open(filepath,'r')
    dict = {}
    while True:
        line = file.readline()
        if not line: break
        for t in line:
            if t in dict:
                dict[t] += 1
            else:
                dict[t] = 1

    i = 0
    for t in dict.items():
        i+=1
        printToListBox(i, t[0], t[1])
    file.close()


label = tkinter.Label(window, text="파일명을 입력하세요: ")
label.grid(row=1,column=0)
pathEntry = tkinter.Entry(window, text="경로")
pathEntry.grid(row=1, column=1)
button = tkinter.Button(window, text="open",command=openfile)
button.grid(row=1,column=2)
resultbutton = tkinter.Button(window, text="결과보기",command=recalculate)
resultbutton.grid(row=1,column=3)






scrollbar=tkinter.Scrollbar(frame)
listbox = tkinter.Listbox(frame, yscrollcommand = scrollbar.set)
#scrollbar.grid(row=0,column=1)
scrollbar.pack(side="right", fill="both", expand=True)

for i in range(20):
    listbox.insert(i, str(i)+"1번")

#listbox.delete(1, 2)
#listbox.grid(row=0,column=0)
listbox.pack()

scrollbar["command"]=listbox.yview
frame.grid(row=0,column=0)

window.mainloop()