from SignUpMenu import SignUpMenu
import tkinter as tk
from network import Network


if __name__ == '__main__':
    Network.connect()
    window = tk.Tk()
    window.title("game")
    hello = SignUpMenu(window)
