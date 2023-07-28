from SignUpMenu import SignUpMenu
import tkinter as tk
import os


if __name__ == '__main__':
    window = tk.Tk()
    window.title("game")
    hello = SignUpMenu(window)
    # print(os.path.join(os.path.dirname(__file__)))
