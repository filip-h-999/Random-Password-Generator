import customtkinter
import random
import string

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()

def window():
    app.title("Password Generator")
    app.geometry('400x550')
    app.resizable(False, False)

    button()
    label()
    copyBtn()
    funktions()

    app.mainloop()


def button():
    btn = customtkinter.CTkButton(master=app, text="Generate", command=lambda: newPwd())
    btn.place(relx=0.1, rely=0.9)


def funktions():
    global varDigits
    varDigits = customtkinter.IntVar()
    digits = customtkinter.CTkSlider(master=app, from_=0, to=30, width=250, variable=varDigits)
    digits.place(relx=0.2, rely=0.2)

    slideValue = customtkinter.CTkLabel(master=app, textvariable=varDigits)
    slideValue.place(relx=0.84, rely=0.185)


def copyBtn():
    cBtn = customtkinter.CTkButton(master=app, text="Copy", command=lambda: copy_select())
    cBtn.place(relx=0.55, rely=0.9)


def generateCode():
    password = ''.join(random.choice(string.digits + string.ascii_letters
                                     + string.ascii_uppercase + string.ascii_lowercase
                                     + string.punctuation) for _ in range(int(varDigits.get())))
    return password


pwd = ""


def copy_select():
    Output = customtkinter.CTkTextbox(master=app)
    Output.tag_add("sel", "1.0", "end")
    try:
        if Output.selection_get():
            app.clipboard_append(pwd)
    except:
        print("nothing Copied")


def label():
    global Output
    Output = customtkinter.CTkLabel(master=app, width=250, height=30 , text=pwd, bg_color="gray")
    Output.place(relx=0.2, rely=0.1)


def newPwd():
    global pwd
    pwd = generateCode()
    label()


if __name__ == '__main__':
    window()