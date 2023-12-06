from tkinter  import *
import customtkinter
import random
from tkinter import Tk, Toplevel
import time
from threading import Timer

app = customtkinter.CTk()
app.title('Casino')
app.geometry('400x400')
customtkinter.set_appearance_mode('Dark')
customtkinter.set_default_color_theme("dark-blue")
app.iconbitmap('casino — копия.ico')
#app.overrideredirect(1)

number = random.randint(1, 10)
attempts = 3
balance = 100


def play():
    app_2 = Toplevel()
    app_2.title('Play')
    app_2.geometry('400x700')
    app_2.config(bg="black")
    customtkinter.set_default_color_theme("green")
    app_2.iconbitmap('chip — копия.ico')

    app_2.image = PhotoImage(file='1645222091_53-phonoteka-org-p-kartochnii-stol-fon-55 — копия.png')
    logo1 = Label(app_2, image=app_2.image)
    logo1.grid(row=0, column=0)

    frame_3 = customtkinter.CTkFrame(app_2, border_width=2, fg_color='#9d9d46', border_color='#fffcfc', width=300, height=500)
    frame_3.place(relx=.25, rely=.2)

    frame_4 = customtkinter.CTkFrame(app_2, border_width=2, fg_color='#9d9d46', border_color='#fffcfc', width=200, height=70)
    frame_4.place(relx=.20, rely=.7)

    def click():
        global balance, attempts
        attempt = int(entry_1.get())
        bet = int(entry_bet.get())

        if attempt < number:
            result = 'Number HIGH'
        elif attempt > number:
            result = 'Number LOW'
        else:
            result = 'Yeah!!!'
            winnings = bet * 10
            balance += winnings

        attempts -= 1
        if attempts == 0 and attempt != number:
            result = 'Game Over'
            balance -= bet

        label_Ret = customtkinter.CTkLabel(frame_4, text=(f'Remaining attempts: {attempts}'), font=('Arial', 15))
        label_Ret.place(relx=.10, rely=.10)
        label_Ret2 = customtkinter.CTkLabel(frame_4, text=(result), font=('Arial', 15))
        label_Ret2.place(relx=.10, rely=.45)

    label_1 = customtkinter.CTkLabel(frame_3, text='Your Number', font=('Arial', 15))
    label_1.pack(pady=10, padx=10)

    entry_1 = customtkinter.CTkEntry(frame_3, placeholder_text="number", font=('Arial', 15))
    entry_1.pack(pady=10, padx=10)

    label_bet = customtkinter.CTkLabel(frame_3, text='Bet Amount', font=('Arial', 15))
    label_bet.pack(pady=10, padx=10)

    entry_bet = customtkinter.CTkEntry(frame_3, placeholder_text="bet amount", font=('Arial', 15))
    entry_bet.pack(pady=10, padx=10)

    button_1 = customtkinter.CTkButton(frame_3, text='Ok', command=click, font=('Arial', 15), fg_color='#000000', text_color='#ffffff')
    button_1.pack(pady=10, padx=10)


def main_menu():

    def view_balance():
        balance_message = f"Your balance is: ${balance}"
        label_balance = customtkinter.CTkLabel(frame_2, text=balance_message, font = ('Arial', 15))
        label_balance.pack(pady=10)
        label_balance.place(relx=.3, rely=.1, anchor="c")

    def play_game():
        name = entry_name.get()
        greeting = f"Hello, Mr.{name} Let's play!"
        label_greeting = customtkinter.CTkLabel(frame_2, text=greeting, font=('Arial', 15))
        label_greeting.pack(pady=10)
        label_greeting.place(relx=.5, rely=.5, anchor="c")

        button_play1 = customtkinter.CTkButton(frame_2, text='Ok', command=play, font=('Arial', 15), fg_color='#fffcfc', text_color='#000000')
        button_play1.pack(pady=10)
        button_play1.place(relx=.5, rely=.6, anchor="c")

        def exit_program():
            app.destroy()

        button_exit = customtkinter.CTkButton(frame_2, text='Exit', command=exit_program, font=('Arial', 15), fg_color='#fffcfc', text_color='#000000')
        button_exit.pack(pady=10)
        button_exit.place(relx=.5, rely=.8, anchor="c")

    label_name.destroy()
    frame.destroy()
    buttonplay.destroy()

    frame_2 = customtkinter.CTkFrame(app, border_width=2, fg_color='#dd1120', border_color='#fffcfc', width=300, height=450)
    frame_2.place(relx=.13, rely=.005)

    label_welcome = customtkinter.CTkLabel(frame_2, text="Welcome to the Casino!", font=('Arial', 15))
    label_welcome.pack(pady=10)
    label_welcome.place(relx=.5, rely=.2, anchor="c")

    button_balance = customtkinter.CTkButton(frame_2, text="View Balance", command=view_balance, font=('Arial', 15),  fg_color='#fffcfc', text_color='#000000')
    button_balance.pack(pady=10)
    button_balance.place(relx=.5, rely=.3, anchor="c")


    button_play = customtkinter.CTkButton(frame_2, text='Play', command=play_game, font=('Arial', 15),  fg_color='#fffcfc', text_color='#000000')
    button_play.pack(pady=10)
    button_play.place(relx=.5, rely=.4, anchor="c")

app.image = PhotoImage(file='wallpaper2you_433401-—-копия.png')
logo = Label(app, image=app.image)
logo.grid(row=0, column=0)

frame = customtkinter.CTkFrame(app, border_width=2, fg_color='#dd1120', border_color='#fffcfc')
frame.place(relx=.25, rely=.17)

label_name = customtkinter.CTkLabel(frame, text='Enter your name:', font=('Arial', 15))
label_name.pack(pady=10)
label_name.place(relx=.5, rely=.3, anchor="c")

entry_name = customtkinter.CTkEntry(app, placeholder_text="name", font=('Arial', 15))
entry_name.place(relx=.5, rely=0.42, anchor="c")

buttonplay = customtkinter.CTkButton(frame, text='Ok', command=main_menu, font=('Arial', 15),  text_color='#000000', fg_color='#fffcfc')
buttonplay.pack(pady=10)
buttonplay.place(relx=.5, rely=.7, anchor="c")


app.mainloop()
