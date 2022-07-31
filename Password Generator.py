import random
import string
import tkinter
from tkinter import Tk, Button, Text

win = Tk()
Output = Text(win, height=2, width=35, bg="light cyan")


def window():
    win.title("Password Generator")
    win.geometry('400x200')
    win.resizable(False, False)
    win["background"] = "#263445"
    win.eval('tk::PlaceWindow . center')
    win.mainloop()


def button():
    btn = Button(win, text="Generate", width=15, height=2, command=lambda: newPwd())
    btn.place(x=149, y=50)
    btn["background"] = "#9FC5E8"


def copyBtn():
    cBtn = Button(win, text="C", width=2, height=1, command=lambda: copy_select())
    cBtn.place(x=355, y=125)
    cBtn["background"] = "#9FC5E8"


def generateCode():
    password = ''.join(random.choice(string.digits + string.ascii_letters
                                     + string.ascii_uppercase + string.ascii_lowercase
                                     + string.punctuation) for _ in range(20))
    return password


pwd = ""


def copy_select():
    Output.tag_add("sel", "1.0", "end")
    try:
        if Output.selection_get():
            win.clipboard_append(pwd)
    except:
        print("nothing Copied")


def label():
    global Output
    Output = Text(win, height=2, width=35, bg="light cyan")
    Output.place(x=60, y=120)
    Output.insert(tkinter.END, pwd)


def newPwd():
    global pwd
    pwd = generateCode()
    label()


def main():
    button()
    label()
    copyBtn()
    window()


main()
