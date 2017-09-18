import tkinter
import threading
from tkinter import *
from tkinter import messagebox
import time
from random import randint

top = tkinter.Tk()
top.geometry("1300x550")

store = Canvas(top, bg = "blue", height = 500, width = 1200)
store.pack()

x1,y1,x2,y2 = 30,60,50,60
count = 0
rand = 400
command = 'right'

store.create_oval(rand, rand, rand, rand,fill="blue", outline="#DDD", width=4,tag="oval")

def linecreation():
    while True:
        store.delete("line")
        global x1
        global y1
        global x2
        global y2
        if(command == 'right'):
            x1 = x1 + 5
            x2 = x2 + 5
        elif(command == 'left'):
            x1 = x1 - 5
            x2 = x2 - 5
        elif(command == 'up'):
            y1 = y1 - 5
            y2 = y2 - 5
        elif(command == 'down'):
            y1 = y1 + 5
            y2 = y2 + 5
        store.create_line(x1, y1, x2, y2,fill = 'black',tag="line")
        time.sleep(0.1)
        check(x1,y1,x2,y2)

t = threading.Thread(target=linecreation)
t.start()

def check(x1,y1,x2,y2):
    if((x1 == rand and y1 == rand) or (x2 == rand and y2 == rand)):
        messagebox.showinfo("Congratulation", "Done")
        store.delete("oval")
        global rand
        global count
        count = count + 1
        rand = randint(1,99) * 5;
        print (rand)
        store.create_oval(rand, rand, rand, rand,fill="blue", outline="#DDD", width=4,tag="oval")
        points.config(text=count)
        return

def rigthside(event):
    global command
    command = 'right'
		
def leftside(event):
    global command
    command = 'left'
		
def upside(event):
    global command
    command = 'up'

def downside(event):
    global command
    command = 'down'


top.bind("<Right>", rigthside)
top.bind("<Left>", leftside)
top.bind("<Up>", upside)
top.bind("<Down>", downside)

points = Label(top, text=count)
points.pack()

top.mainloop()
