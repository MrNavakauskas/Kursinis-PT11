from tkinter import *
import tkinter as tk
import a

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("G.Navakausko PT11 kursinis darbas")
root.eval('tk::PlaceWindow . center')
img = PhotoImage(file="covidPNG.png")
label = Label(root, image=img)
label.place(x=0, y=0)
button = tk.Button(root, fg='red', text="Pradėti", width=10, command=lambda: pradeti())
button.place(rely=0.80, relx=0.75)


def pradeti():
    root.destroy()
    a.main()

root.mainloop()
