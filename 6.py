from tkinter import *
from tkinter import ttk

clicks = 0

def click_button():
    global clicks
    clicks += 1
    # изменяем текст на кнопке
    btn["text"] = f"clicks {clicks}"

root = Tk()
root.title("school")
root.geometry("250x150")

btn = ttk.Button(text="Click Me", command=click_button)
btn.pack()

root.mainloop()