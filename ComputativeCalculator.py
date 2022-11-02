# Run Window
from tkinter import *
from tkinter import ttk
import re

string = ""

def addzero():
    global string
    string += "0"
    text.config(text=string)
    

def addone():
    global string
    string += "1"
    text.config(text=string)
    

def addtwo():
    global string
    string += "2"
    text.config(text=string)
    

def addthree():
    global string
    string += "3"
    text.config(text=string)
    

def addfour():
    global string
    string += "4"
    text.config(text=string)
    

def addfive():
    global string
    string += "5"
    text.config(text=string)
    

def addsix():
    global string
    string += "6"
    text.config(text=string)
    

def addseven():
    global string
    string += "7"
    text.config(text=string)
    

def addeight():
    global string
    string += "8"
    text.config(text=string)
    

def addnine():
    global string
    string += "9"
    text.config(text=string)
    

def multiply():
    global string
    string += "*"
    text.config(text=string)
    

def divide():
    global string
    string += "/"
    

def add():
    global string
    string += "+"
    text.config(text=string)
    

def subtract():
    global string
    string += "-"
    text.config(text=string)
    

def percent():
    global string
    string += ""
    text.config(text=string)
   

def swapsign():
    global string
    string += ""
    text.config(text=string)
    

def decimal():
    global string
    string += "."
    text.config(text=string)

def mnd(func, string):
    pass
def ans(func):
    pass

def calculate():
    global string

    if "+" in string:
        y, z = string.split("+")
        string =  str(float(y) + float(z))
        #text.config(text=string)
    if "-" in string:
        y, z = string.split("-")
        string =  str(float(y) - float(z))
        #text.config(text=string)
    if "*" in string:
        y, z = string.split("*")
        string =  str(float(y) * float(z))
        #text.config(text=string)
    if "/" in string:
        y, z = string.split("/")
        string =  str(float(y) / float(z))
        #text.config(text=string)
    if len(string) > 9:
        string = string[0:8]
    
    text.config(text=string)

def erase():
    global string
    string = ""
    print(string)

def main():
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    root.title("Calculator")
    root.iconbitmap("favicon.ico")
    #lbl_value = ttk.Label(master=root, text="")
    #lbl_value.grid(row=0, column=6)
    
    #ttk.Button(frm, text="X", command=root.destroy).grid(column=1, row=0)

    ttk.Button(frm, text="AC", command=erase).grid(column=1, row=1)
    ttk.Button(frm, text="+/-", command=swapsign).grid(column=2, row=1)
    ttk.Button(frm, text="%", command=percent).grid(column=3, row=1)
    ttk.Button(frm, text="/", command=divide).grid(column=4, row=1)
    ttk.Button(frm, text="7", command=addseven).grid(column=1, row=2)
    ttk.Button(frm, text="8", command=addeight).grid(column=2, row=2)
    ttk.Button(frm, text="9", command=addnine).grid(column=3, row=2)
    ttk.Button(frm, text="*", command=multiply).grid(column=4, row=2)
    ttk.Button(frm, text="4", command=addfour).grid(column=1, row=3)
    ttk.Button(frm, text="5", command=addfive).grid(column=2, row=3)
    ttk.Button(frm, text="6", command=addsix).grid(column=3, row=3)
    ttk.Button(frm, text="-", command=subtract).grid(column=4, row=3)
    ttk.Button(frm, text="1", command=addone).grid(column=1, row=4)
    ttk.Button(frm, text="2", command=addtwo).grid(column=2, row=4)
    ttk.Button(frm, text="3", command=addthree).grid(column=3, row=4)
    ttk.Button(frm, text="+", command=add).grid(column=4, row=4)
    ttk.Button(frm, text="0", command=addzero).grid(column=1, row=5)
    ttk.Button(frm, text=".", command=decimal).grid(column=2, row=5)
    ttk.Button(frm, text="=", command=calculate).grid(column=3, row=5)
    global string
    global text
    text = ttk.Label(frm, text="")
    text.grid(column=0, row=0)
    root.mainloop()

main()