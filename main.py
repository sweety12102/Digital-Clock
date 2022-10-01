from tkinter import Tk
from tkinter import Label
import time
import sys

master = Tk()
master.title("DIGITAL CLOCK")

Label(master, font=("Arial", 30), text="DIGITAL CLOCK", fg="white", bg="black").pack()
clock = Label(master, font=("Arial", 80), bg="black", fg="white")
clock.pack()

def get_time():
    timeVar = time.strftime("%d-%m-%Y,%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200, get_time)

get_time()
master.mainloop()


