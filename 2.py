from tkinter import *

root = Tk()
root.title("My First GUI app!")
root.iconbitmap(default="tree.ico")
root.geometry("300x250")

label = Label(text="Hello world")
label.pack()
root.mainloop()