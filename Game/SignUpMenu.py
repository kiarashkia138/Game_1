import tkinter as tk


class SignUpMenu():
    def __init__(self, window):
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()

        middle_x = int(width/2)
        distance_y = int(height/4)

        window.geometry(f"{width}x{height}")

        username_var = tk.StringVar()
        password_var = tk.StringVar()
        confirm_password_var = tk.StringVar()

        username_lab = tk.StringVar()
        password_lab = tk.StringVar()
        confirm_password_lab = tk.StringVar()

        #
        username_lab.set("Username :")
        password_lab.set("Password :")
        confirm_password_lab.set("Confirm Password :")
        #

        widget_width = 125

        # username :
        username_label = tk.Label(window, textvariable=username_lab, font=('normal',14))
        username_label.place(x=middle_x - widget_width, y=distance_y - 25, height=25)

        username_entry = tk.Entry(window, textvariable=username_var, font=('Arial',11), bd=1)
        username_entry.place(x=middle_x - widget_width, y=distance_y, width=widget_width*2, height=25)

        # password:
        password_label = tk.Label(window, textvariable=password_lab, font=('normal',14))
        password_label.place(x=middle_x - widget_width, y=distance_y + 50, height=25)

        password_entry = tk.Entry(window, textvariable=password_var, font=('normal',17), bd=1, show="*")
        password_entry.place(x=middle_x - widget_width, y=distance_y + 75, width=widget_width*2, height=25)

        confirm_password_label = tk.Label(window, textvariable=confirm_password_lab, font=('normal',14))
        confirm_password_label.place(x=middle_x - widget_width, y=distance_y + 125, height=25)

        confirm_password_entry = tk.Entry(window, textvariable=confirm_password_var, font=('normal',17), bd=1, show="*")
        confirm_password_entry.place(x=middle_x - widget_width, y=distance_y + 150, width=widget_width*2, height=25)

        # button :
        sign_up_button = tk.Button(window, text="Sign Up", font=('calibri', 16, 'bold'), bg="#2196F3", fg="white", bd=1)
        sign_up_button.bind('<Button-1>', lambda event: sign_up())
        sign_up_button.place(x=middle_x - widget_width, y=distance_y + 240, width=widget_width*2, height=30)

        window.mainloop()


def sign_up():
    print("sign up")