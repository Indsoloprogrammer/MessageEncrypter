import tkinter
import tkinter.font as font
import tkinter.messagebox


class FrontendPass():
    def __init__(self):
        self.PASSWORD = ""
        self.USERNAME = ""
        self.KEY = ""
        self.root = tkinter.Tk()
        self.root.configure(bg='#303030')

        self.font = font.Font(size=12)

        self.user_label = tkinter.Label(text="Username: ", fg='white', bg='#303030')
        self.user_label['font'] = self.font
        self.user_label.grid(row=0, column=0)

        self.user_entry = tkinter.Entry(fg="white")
        self.user_entry.config({"background": "#303030"})
        self.user_entry.grid(row=0, column=1)

        self.pwd_label = tkinter.Label(text="Password: ", fg='white', bg='#303030')
        self.pwd_label['font'] = self.font
        self.pwd_label.grid(row=1, column=0)

        self.pwd_entry = tkinter.Entry(fg="white")
        self.pwd_entry.config({"background": "#303030"})
        self.pwd_entry.grid(row=1, column=1)

        self.key_label = tkinter.Label(text="Key: ", fg='white', bg='#303030')
        self.key_label['font'] = self.font
        self.key_label.grid(row=2, column=0)

        self.key_entry = tkinter.Entry(fg="white")
        self.key_entry.config({"background": "#303030"})
        self.key_entry.grid(row=2, column=1)

        self.submit = tkinter.Button(text="submit", width=10, bg='#303030', fg='white', command=self.get_info)
        self.submit.grid(row=3, column=1)

    def get_info(self):
        user = self.user_entry.get()
        pwd = self.pwd_entry.get()
        key = self.key_entry.get()

        if user == "" or pwd == "" or key == "":
            tkinter.messagebox.showwarning(title="Warning", message="Please fill the fields") 

        elif user == "1234" and pwd == "1234":
            self.root.destroy()
            self.PASSWORD = pwd
            self.USERNAME = user
            self.KEY = key           
        else:
            tkinter.messagebox.showerror(title="Error", message="Incorrect Username or password")
            self.pwd_entry.delete(0, 'end')
