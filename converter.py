import tkinter
import os
import tkinter.messagebox as messagebox
from encrypter import full_encyption, full_decryption


class App():
    def __init__(self, key):
        self.root = tkinter.Tk()
        self.root.title('Message Encrypter and Decrypter')
        self.root.configure(bg="white")
        # scroll bar
        self.scrollbar = tkinter.Scrollbar(self.root)
        self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        # text area
        self.txtarea = tkinter.Text(self.root, height=25, width=60, bg="white", yscrollcommand=True, xscrollcommand=True)
        self.txtarea['font'] = 6
        # scroll bar functional
        self.txtarea.pack()
        self.txtarea.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.txtarea.yview)
        # buttons
        self.btn_encrypt = tkinter.Button(text="Encrypt", width=22, bg='white', activebackground='white', command=lambda: self.encrypt(key))
        self.btn_encrypt.pack(side=tkinter.LEFT)
        self.btn_decrypt = tkinter.Button(text="Decrypt", width=22, bg='white', activebackground='white', command=lambda: self.decrypt(key))
        self.btn_decrypt.pack(side=tkinter.LEFT)
        self.btn_exit = tkinter.Button(text="Exit", width=22, bg='white', activebackground='white' ,command=self.close)
        self.btn_exit.pack(side=tkinter.LEFT)

    def close(self):
        self.root.destroy()

    def encrypt(self, key):
        text = self.txtarea.get("1.0", tkinter.END)
        if text != ' ' or text != '   ' or text != '' or text != None:
            try:
                encrypted = full_encyption(key, text)
                win = Win(encrypted, "Encrypted")
                win.root.mainloop()
            except:
                messagebox.showerror(title="Encryption error", message="Key mismatch")
        else:
            messagebox.showwarning(title="Warning!!", message="Please enter a text to encrypt")

    def decrypt(self, key):
        B64 = self.txtarea.get("1.0", tkinter.END)
        try:
            decrypted = full_decryption(key, B64)
            win = Win(decrypted, "Decrypted")
            win.root.mainloop()
        except:
            messagebox.showerror(title="Decryption error", message="Make sure that the text is Encrypted and the key is correct")


class Win():
    def __init__(self, text, title):
        """
        text: text to be displayed 
        title: Title of the window
        """
        self.root = tkinter.Tk()
        self.root.configure(bg='white')
        self.root.title(title)
        self.txtbox = tkinter.Text(self.root, height=25, width=60, bg="white", yscrollcommand=True, xscrollcommand=True)
        self.txtbox.pack()
        self.txtbox.insert(tkinter.END, text)
        # buttons
        self.btn_save = tkinter.Button(self.root, width=27, text="Save text", bg='white', fg='black', command=self.save)
        self.btn_save.pack(side=tkinter.LEFT)
        self.btn_exit = tkinter.Button(self.root, width=27, text="Close", bg='white', fg='black', command=self.close)
        self.btn_exit.pack(side=tkinter.LEFT)

    def close(self):
        self.root.destroy()

    def save(self):
        text = self.txtbox.get("1.0", tkinter.END)
        with open('messages.txt', 'a') as f:
            f.write(text + "\n")
        messagebox.showinfo(title="Success!!", message="File saved to " + os.getcwd() + "/messages.txt")


