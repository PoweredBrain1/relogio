#Meu IP por Nuno Alves
import socket
from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title("DICTOF")

def time():
    string = strftime('%H:%M:%S')
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=("arial", 40), background = "white", foreground = "green")
label.pack(anchor='center')


time()


mainloop()