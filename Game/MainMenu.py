import tkinter as tk
from PIL import Image, ImageTk
import os
from UserDataBase import UserDataBase


class MainMenu:

    @classmethod
    def create(cls, window):
        cls.window = window

    @classmethod
    def show(cls):
        print("show")

