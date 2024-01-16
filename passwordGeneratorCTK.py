import customtkinter
import random
import string

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()

def window():
    app.title("Password Generator")
    app.geometry('400x500')
    app.resizable(False, False)

    name = customtkinter.CTkLabel(master=app, text="Password Generator", font=('Arial', 20, 'bold'))
    name.place(relx=0.27, rely=0.025)

    button()
    label()
    copyBtn()
    funktions()

    app.mainloop()


def button():
    btn = customtkinter.CTkButton(master=app, text="Generate", width=100, command=lambda: newPwd())
    btn.place(relx=0.19, rely=0.85)


def funktions():
    global varDigits, varUpper, varLower, varAscii, varNumbers, varPunctuation
    varDigits = customtkinter.IntVar()
    digits = customtkinter.CTkSlider(master=app, from_=0, to=30, width=250, variable=varDigits)
    digits.place(relx=0.2, rely=0.21)

    slideValue = customtkinter.CTkLabel(master=app, textvariable=varDigits)
    slideValue.place(relx=0.84, rely=0.2)

    varUpper = customtkinter.StringVar(value=string.ascii_uppercase)
    upper = customtkinter.CTkSwitch(master=app, text="Upper Case", onvalue=string.ascii_uppercase, variable=varUpper)
    upper.place(relx=0.2, rely=0.3)

    varLower = customtkinter.StringVar(value=string.ascii_lowercase)
    lover = customtkinter.CTkSwitch(master=app, text="Lover Case", onvalue=string.ascii_lowercase, variable=varLower)
    lover.place(relx=0.2, rely=0.4)

    varAscii = customtkinter.StringVar(value=string.ascii_letters)
    asciiL = customtkinter.CTkSwitch(master=app, text="ASCII", onvalue=string.ascii_letters, variable=varAscii)
    asciiL.place(relx=0.2, rely=0.5)

    varNumbers = customtkinter.StringVar(value=string.digits)
    numbers = customtkinter.CTkSwitch(master=app, text="Numbers", onvalue=string.digits, variable=varNumbers)
    numbers.place(relx=0.2, rely=0.6)

    varPunctuation = customtkinter.StringVar(value=string.punctuation)
    punctuation = customtkinter.CTkSwitch(master=app, text="Punctuation", onvalue=string.punctuation, variable=varPunctuation)
    punctuation.place(relx=0.2, rely=0.7)


def copyBtn():
    cBtn = customtkinter.CTkButton(master=app, text="Copy", width=100, command=lambda: copy_select())
    cBtn.place(relx=0.55, rely=0.85)


def generateCode():
    password = ''.join(random.choice(varNumbers.get() + varAscii.get() + varUpper.get() + varLower.get() + varPunctuation.get()) for _ in range(int(varDigits.get())))
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
    Output = customtkinter.CTkLabel(master=app, width=250, height=30 , text=pwd, bg_color="#444444")
    Output.place(relx=0.2, rely=0.11)


def newPwd():
    global pwd
    pwd = generateCode()
    label()


if __name__ == '__main__':
    window()