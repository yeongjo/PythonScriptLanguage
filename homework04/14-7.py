import tkinter as tk
import urllib
import urllib.request

g_text = ""


# The variables below size the bar graph
y_stretch = 15  # The highest y = max_data_value * y_stretch
y_gap = 20  # The gap between lower canvas edge and x axis
x_stretch = 10  # Stretch x wide enough to fit the variables
x_width = 20  # The width of the x-axis
x_gap = 20  # The gap between left canvas edge and y axis


def printToListBox(idx, char, count):
    listbox.insert(idx, str(f"{char} - {count}번 나타납니다."))

def openurl():
    global g_text
    link = pathEntry.get()
    f = urllib.request.urlopen(link)
    g_text = f.read().decode('utf-8')
    print(g_text)
    dict = {}
    for t in g_text:
        if t in dict:
            dict[t] += 1
        else:
            dict[t] = 1

    print(dict)
    c.delete("all")
    # A quick for loop to calculate the rectangle
    for x, y in enumerate(dict.items()):
        print(y," ", y[0], " ", y[1])
        # coordinates of each bar
        # Bottom left coordinate
        x0 = x * x_stretch + x * x_width + x_gap
        # Top left coordinates
        y0 = c_height - (y[1] * y_stretch + y_gap)
        # Bottom right coordinates
        x1 = x * x_stretch + x * x_width + x_width + x_gap
        # Top right coordinates
        y1 = c_height - y_gap
        # Draw the bar
        c.create_rectangle(x0, y0, x1, y1, fill="red")
        # Put the y value above the bar
        c.create_text(x0 + 2, y0, anchor=tk.SW, text=str(y[0]))

window = tk.Tk()
window.title("Bar Graph")

c_width = 800  # Define it's width
c_height = 400  # Define it's height
c = tk.Canvas(window, width=c_width, height=c_height, bg='white')
c.grid(row=0,column=0)



label = tk.Label(window, text="URL을 입력하세요: ")
label.grid(row=1,column=0)
pathEntry = tk.Entry(window, text="https://stackoverflow.com/questions/15138614/how-can-i-read-the-contents-of-an-url-with-python")
pathEntry.grid(row=1, column=1)
button = tk.Button(window, text="open",command=openurl)
button.grid(row=1,column=2)

window.mainloop()