import tkinter as tk
from PIL import Image, ImageTk
import os
from UserDataBase import UserDataBase
from MainMenu import MainMenu


class SignUpMenu:
    def __init__(self, window):

        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        middle_x = int(width/2)
        distance_y = int(height/3)
        widget_width = 125
        window.geometry(f"{width}x{height}")

        window.attributes("-fullscreen", True)

        # background :
        bg_image = Image.open(os.path.join(os.path.dirname(__file__), "Asset/background/background_1.png"))
        bg_image = bg_image.resize((width, height), Image.ANTIALIAS)
        bg_image = ImageTk.PhotoImage(bg_image)

        canvas = tk.Canvas(window, width=width, height=height)
        canvas.pack()
        canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)

        # sign up :
        username_var = tk.StringVar()
        password_var = tk.StringVar()
        confirm_password_var = tk.StringVar()

        username_lab = tk.StringVar()
        password_lab = tk.StringVar()
        confirm_password_lab = tk.StringVar()

        username_lab.set("Username :")
        password_lab.set("Password :")
        confirm_password_lab.set("Confirm Password :")

        # username :
        username_label = tk.Label(window, textvariable=username_lab, font=('normal',14))
        username_label.place(x=middle_x + 70, y=distance_y - 25, height=25)

        username_entry = tk.Entry(window, textvariable=username_var, font=('Arial',11), bd=1)
        username_entry.place(x=middle_x + 70, y=distance_y, width=widget_width*2, height=25)

        # password:
        password_label = tk.Label(window, textvariable=password_lab, font=('normal',14))
        password_label.place(x=middle_x + 70, y=distance_y + 50, height=25)

        password_entry = tk.Entry(window, textvariable=password_var, font=('normal',17), bd=1, show="*")
        password_entry.place(x=middle_x + 70, y=distance_y + 75, width=widget_width*2, height=25)

        confirm_password_label = tk.Label(window, textvariable=confirm_password_lab, font=('normal',14))
        confirm_password_label.place(x=middle_x + 70, y=distance_y + 125, height=25)

        confirm_password_entry = tk.Entry(window, textvariable=confirm_password_var, font=('normal',17), bd=1, show="*")
        confirm_password_entry.place(x=middle_x + 70, y=distance_y + 150, width=widget_width*2, height=25)

        # button :
        sign_up_button = tk.Button(window, text="Sign Up", font=('calibri', 16, 'bold'), bg="#2196F3", fg="white", bd=1)
        sign_up_button.bind('<Button-1>',
                            lambda event: sign_up(username_var.get(), password_var.get(), confirm_password_var.get(), window))
        sign_up_button.place(x=middle_x + 70, y=distance_y + 240, width=widget_width*2, height=30)

        # login :
        username_var2 = tk.StringVar()
        password_var2 = tk.StringVar()

        username_lab2 = tk.StringVar()
        password_lab2 = tk.StringVar()

        username_lab2.set("Username :")
        password_lab2.set("Password :")

        distance_y += 55

        # username :
        username_label = tk.Label(window, textvariable=username_lab2, font=('normal', 14))
        username_label.place(x=middle_x - (70 + 2 * widget_width), y=distance_y - 25, height=25)

        username_entry = tk.Entry(window, textvariable=username_var2, font=('Arial', 11), bd=1)
        username_entry.place(x=middle_x - (70 + 2 * widget_width), y=distance_y, width=widget_width * 2, height=25)

        # password:
        password_label = tk.Label(window, textvariable=password_lab2, font=('normal', 14))
        password_label.place(x=middle_x - (70 + 2 * widget_width), y=distance_y + 50, height=25)

        password_entry = tk.Entry(window, textvariable=password_var2, font=('normal', 17), bd=1, show="*")
        password_entry.place(x=middle_x - (70 + 2 * widget_width), y=distance_y + 75, width=widget_width * 2, height=25)

        # button :
        login_button = tk.Button(window, text="Login", font=('calibri', 16, 'bold'), bg="#2196F3", fg="white", bd=1)
        login_button.bind('<Button-1>',
                            lambda event: login(username_var2.get(), password_var2.get(), window))
        login_button.place(x=middle_x - (70 + 2 * widget_width), y=distance_y + 240 - 55, width=widget_width * 2, height=30)

        # show :
        window.mainloop()


def sign_up(username, password, confirm_password, window):
    # print("username : ", username, " password : ", password, " confirm : ", confirm_password)

    # TODO : write func to check if username exist !!
    if username == "" or password == "" or confirm_password == "" or\
            password != confirm_password or username_exist(username) != 200:
        return
    else:
        print("username : ", username, " password : ", password, " confirm : ", confirm_password)
        UserDataBase.create(username, 0)
        MainMenu.create(window)
        MainMenu.show()


def login(username, password, window):
    if username == "" or password == "" or username_exist(username) != 200:
        return
    else:
        print("username : ", username, " password : ", password)
        # get user information
        score = 0
        #
        UserDataBase.create(username, score)
        MainMenu.create(window)
        MainMenu.show()


def username_exist(username):
    # return 200 if ok
    # return 400 if password is not correct
    # return 404 if username doesn't exist
    return 200



