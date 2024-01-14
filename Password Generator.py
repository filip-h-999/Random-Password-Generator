import random
import string
from tkinter import *
from tkinter import Tk, Button, Text

win = Tk()
Output = Text(win, height=2, width=35, bg="light cyan")


def window():
    win.title("Password Generator")
    win.geometry('395x198')
    win.resizable(False, False)
    win["background"] = "black"

    img = PhotoImage(file=r"img\rick.png")
    background_label = Label(win, image=img)
    background_label.place(x=-2, y=0)

    button()
    label()
    copyBtn()

    win.eval('tk::PlaceWindow . center')
    win.mainloop()


def button():
    btn = Button(win, text="Generate", width=13, height=2, font=('Arial', 10, 'bold'), command=lambda: newPwd())
    btn.place(x=86, y=110)
    btn["background"] = "#FFB266"


def copyBtn():
    cBtn = Button(win, text="Copy", width=10, height=2, font=('Arial', 10, 'bold'), command=lambda: copy_select())
    cBtn.place(x=220, y=110)
    cBtn["background"] = "#FFB266"


def generateCode():
    password = ''.join(random.choice(string.digits + string.ascii_letters
                                     + string.ascii_uppercase + string.ascii_lowercase
                                     + string.punctuation) for _ in range(20))
    return password


pwd = ""


def copy_select():
    Output = Text(win, height=2, width=35, bg="light cyan")
    Output.tag_add("sel", "1.0", "end")
    try:
        if Output.selection_get():
            win.clipboard_append(pwd)
    except:
        print("nothing Copied")


def label():
    global Output
    Output = Label(win, height=2, width=27, text=pwd, bg="#99FF99", font=('Arial', 10, 'bold'))
    Output.place(x=86, y=50)
    # Output.insert(tkinter.END, pwd)


def newPwd():
    global pwd
    pwd = generateCode()
    label()


def main():
    window()


main()
