import tkinter as tk


class SqlLangas():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master, bg="light blue", height=1024, width=1024)  # this is the background
        self.frame.pack(fill="both", expand="true", anchor="c")
        master.geometry("626x431")
        master.resizable(0, 0)
        master.title("Čia gali būti bet kokia .py programa")
        master.iconbitmap(r'1.ico')
        self.frame_login = tk.Frame(master, bg="light grey", relief="groove", bd=2)  # prisijungimo detales/mygtukai...
        self.frame_login.place(rely=0.30, relx=0.17, height=120, width=400)
        self.lbl = tk.Label(master, text="You can never understand everything.")
        self.lbl1 = tk.Label(master, text="But you should push yoursef to understand the system")
        self.lbl2 = tk.Label(master, text="Ryan Dahl (Creator of Node.is) ")
        self.lbl.place(rely=0.37, relx=0.25)
        self.lbl1.place(rely=0.42, relx=0.25)
        self.lbl2.place(rely=0.47, relx=0.45)
        # button = tk.Button(master, fg='red', text="Pradėti", width=10, command=lambda: pradeti())
        # button.place(rely=0.80, relx=0.75)

# def pradeti():
#     pass

def main():
    root = tk.Tk()
    app = SqlLangas(root)
    root.mainloop()

if __name__ == "__main__":
    main()
