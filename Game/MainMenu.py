import tkinter as tk
from PIL import Image, ImageTk
import os
from User import User
import sys
from network import Network


class MainMenu:

    @classmethod
    def create(cls, window):
        cls.window = window

    @classmethod
    def show(cls):
        cnt = 0
        for widget in cls.window.winfo_children():
            if cnt != 0:
                widget.destroy()
            else:
                cnt = 1

        window = cls.window
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        middle_x = int(width / 2)
        distance_y = int(height / 3)

        score_lab = tk.StringVar()
        score_lab.set(User.score)
        score_label = tk.Label(window, textvariable=score_lab, font=('normal', 20))
        score_label.place(x=middle_x - 40, y=distance_y + 50, height=40)

        start_button = tk.Button(window, text="START", font=('calibri', 25, 'bold'), bg="#F8E832", fg="black", bd=1)
        start_button.bind('<Button-1>',lambda event: start())
        start_button.place(x=middle_x - 120, y=distance_y + 240, width=240, height=60)

        end_button = tk.Button(window, text="Exit", font=('calibri', 14, 'bold'), fg="black", bd=0)
        end_button.bind('<Button-1>', lambda event: end())
        end_button.place(x=0, y=0, width=60, height=20)


def start():
    print("start game")


def end():
    sys.exit(1)

