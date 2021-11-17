import tkinter as tk
from tkinter import messagebox
import e

# my_text.delete("1.0", "end")


class PirmLangas:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master, bg="light blue", height=600, width=800)  # fonas
        self.frame.pack(fill="both", expand="true", anchor="c")
        master.geometry("600x300")
        master.resizable(0, 0)
        master.title("Kursinis darbas skirtas bendramiesčiui lektoriui Mr.Stasiui Čiviliui")
        master.iconbitmap(r'1.ico')

        frame_login = tk.Frame(master, bg="light grey", relief="groove", bd=2)  # prisijungimo detales/mygtukai...
        frame_login.place(rely=0.30, relx=0.17, height=120, width=400)
        title_style = {"font": ("Trebuchet MS Bold", 12), "background": "light grey"}
        label_title = tk.Label(frame_login, title_style, text="Prisijungimas")
        label_title.grid(row=0, column=1, columnspan=1)
        text_styles = {"font": ("Verdana", 10), "background": "light grey", "foreground": "black"}
        label_user = tk.Label(frame_login, text_styles, text="Vartotojo vardas:")
        label_user.grid(row=1, column=0)
        label_pw = tk.Label(frame_login, text_styles, text="Slaptažodis:")
        label_pw.grid(row=2, column=0, sticky="E")

        entry_user = tk.Entry(frame_login, width=35)
        entry_user.grid(row=1, column=1)
        entry_pw = tk.Entry(frame_login, width=35, show="*")
        entry_pw.grid(row=2, column=1)

        btn_login = tk.Button(frame_login, text="Prisijungti", width=10, command=lambda: prisijungti())
        btn_login.place(rely=0.68, relx=0.36)
        btn_signup = tk.Button(frame_login, text="Registruotis",  width=10, command=lambda: Registruotis())
        btn_signup.place(rely=0.68, relx=0.60)

        def prisijungti():
            username = entry_user.get()
            password = entry_pw.get()
            patvirtinimas = patvirtinti(username, password)
            if patvirtinimas:
                tk.messagebox.showinfo("Jus sėkmingai prisijungėte",
                                       "Malonu jus matyt lektoriau {}".format(username))
                e.SqlLangas(master)
#                gsql.root.mainloop()

            else:
                tk.messagebox.showerror("Atkreipkite dėmesį",
                                        "Ivestas vartotojo vardas arba slaptazodis yra neteisingas ")

        def patvirtinti(username, password):
            # Checks the text file for a username/password combination.
            try:
                with open("psw.txt", "r") as psw:
                    for line in psw:
                        line = line.split(",")
                        if line[1] == username and line[3] == password:
                            return True
                    return False
            except FileNotFoundError:
                print("Pirmiausiai prašome užsiregistruoti")
                return False

        # def registruotis():
        #     e.SqlLangas(master)


class Registruotis(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        main_frame = tk.Frame(self, bg="light grey", height=150, width=250)
        main_frame.pack(fill="both", expand="true")
        self.geometry("300x110")
        self.resizable(0, 0)
        self.title("Registracija")
        text_styles = {"font": ("Verdana", 10), "background": "light grey", "foreground": "black"}

        label_user = tk.Label(main_frame, text_styles)
        label_user.grid(row=1, column=0)
        label_user = tk.Label(main_frame, text_styles, text="Naujas vardas:")
        label_user.grid(row=2, column=0, sticky="E")
        label_pw = tk.Label(main_frame, text_styles, text="Naujas slaptažodis:")
        label_pw.grid(row=3, column=0)

        entry_user = tk.Entry(main_frame, width=25)
        entry_user.grid(row=2, column=1)
        entry_pw = tk.Entry(main_frame, width=25)
        entry_pw.grid(row=3, column=1)

        btn_create = tk.Button(main_frame, text="Sukurti paskyra",  width=15, command=lambda: sukurti())
        btn_create.place(rely=0.65, relx=0.50)

        def sukurti():
            user = entry_user.get()
            pw = entry_pw.get()
            patvirtinimas = patvirtinti(user)
            if not patvirtinimas:
                tk.messagebox.showerror("Klaida", "Toks vartotojas jau egzistuoja")
            else:
                if len(pw) > 3:
                    psw = open("psw.txt", "a")
                    psw.write(f"Vardas,{user},Slaptazodis,{pw},\n")
                    psw.close()
                    tk.messagebox.showinfo("Informacija", "Jūsų paskyra išsaugota")
                    Registruotis.destroy(self)

                else:
                    tk.messagebox.showerror("Klaida",
                                            "Slaptažodis turi būti ne trumpesnis nei 4 simboliai")

        def patvirtinti(username):
            # Checks the text file for a username/password combination.
            try:
                with open("psw.txt", "r") as psw:
                    for line in psw:
                        line = line.split(",")
                        if line[1] == username:
                            return False
                return True
            except FileNotFoundError:
                return True


def main():
    root = tk.Tk()
    app = PirmLangas(root)
    root.mainloop()


if __name__ == "__main__":
    main()
