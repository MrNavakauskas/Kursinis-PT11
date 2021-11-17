from tkinter import *
from tkinter import Tk
import tkinter as tk
from tkinter import ttk
import sqlite3


def atnaujinti(eiles):
    tr_view.delete(*tr_view.get_children())
    for i in eiles:
        tr_view.insert("", "end", values=i)


def surasti():
    s2 = s.get()
    query1 = "SELECT id, vardas, pavarde, amzius, skiepijimasis FROM darbuotojai WHERE vardas LIKE '%"+s2+"%' " \
                            "OR pavarde LIKE '%"+s2+"%' OR amzius LIKE '%"+s2+"%' OR skiepijimasis LIKE '%"+s2+"%'"
    cursor.execute(query1)
    eiles = cursor.fetchall()
    atnaujinti(eiles)


def grazinti_db():
    query = "SELECT id, vardas, pavarde, amzius, skiepijimasis FROM darbuotojai"
    cursor.execute(query)
    eiles = cursor.fetchall()
    atnaujinti(eiles)


def ikelti(event):  # 2 click get data
#    rowid = trv.identify_row(event.y) #  row ID will return
    item = tr_view.item(tr_view.focus())
    t1.set(item['values'][0])
    t2.set(item['values'][1])
    t3.set(item['values'][2])
    t4.set(item['values'][3])
    t5.set(item['values'][4])


def atnaujinti_ir():
    id1 = t1.get()
    vard = t2.get()
    pav = t3.get()
    amz = t4.get()
    skiep = t5.get()
    query = "UPDATE darbuotojai SET vardas = ?, pavarde = ?, amzius = ?, skiepijimasis = ? WHERE id = ?"
    cursor.execute(query, (vard, pav, amz, skiep, id1))
    duombaze.commit()
    grazinti_db()


# https://www.w3schools.com/python/showpython.asp?filename=demo_mysql_insert_id
def add_new():
    id1 = t1.get()
    vard = t2.get()
    pav = t3.get()
    amz = t4.get()
    skiep = t5.get()
    query = "INSERT INTO darbuotojai (id, vardas, pavarde, amzius, skiepijimasis) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(query, (id1, vard, pav, amz, skiep))
    duombaze.commit()
    grazinti_db()


def istrint_ir():
    ir_id = t1.get()
    query = "DELETE FROM darbuotojai WHERE id = " + ir_id
    cursor.execute(query)
    duombaze.commit()
    grazinti_db()


duombaze = sqlite3.connect("duombaze5.db")
cursor = duombaze.cursor()

root = Tk()
s = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()

sektorius1 = LabelFrame(root, text="Pasiskiepijusių sąrašas")
sektorius2 = LabelFrame(root, text="Paieška")
sektorius3 = LabelFrame(root, text="Duomenys")
sektorius1.pack(fill="both", expand="yes", padx=20, pady=10)
sektorius2.pack(fill="both", expand="yes", padx=20, pady=10)
sektorius3.pack(fill="both", expand="yes", padx=20, pady=10)

tr_view = ttk.Treeview(sektorius1, columns=(1, 2, 3, 4, 5), show="headings", height="10")
tr_view.pack()

tr_view.heading(1, text="Nr.", anchor="w")
tr_view.heading(2, text="Vardas", anchor="w")
tr_view.heading(3, text="Pavardė", anchor="w")
tr_view.heading(4, text="Amžius", anchor="w")
tr_view.heading(5, text="Skiepų sk.", anchor="w")

tr_view.bind('<Double 1>', ikelti)

query = "SELECT * FROM darbuotojai"
cursor.execute(query)
eiles = cursor.fetchall()
atnaujinti(eiles)

lbl_sek2 = Label(sektorius2, text="Paieška")
lbl_sek2.pack(side=tk.LEFT, padx=10)
ent_sek2 = Entry(sektorius2, textvariable=s)
ent_sek2.pack(side=tk.LEFT, padx=6)
btn_sek2a = Button(sektorius2, text="Paieška", command=surasti)
btn_sek2a.pack(side=tk.LEFT, padx=6)
btn_sek2b = Button(sektorius2, text="Atgal", command=grazinti_db)
btn_sek2b.pack(side=tk.LEFT, padx=6)

lbl1_sek3 = Label(sektorius3, text="Id")
lbl1_sek3.grid(row=0, column=0, padx=5, pady=3)
ent_sek3 = Entry(sektorius3, textvariable=t1)
ent_sek3.grid(row=0, column=1, padx=5, pady=3)

lbl2_sek3 = Label(sektorius3, text="Vardas")
lbl2_sek3.grid(row=1, column=0, padx=5, pady=3)
ent2_sek3 = Entry(sektorius3, textvariable=t2)
ent2_sek3.grid(row=1, column=1, padx=5, pady=3)

lbl3_sek3 = Label(sektorius3, text="Pavardė")
lbl3_sek3.grid(row=2, column=0, padx=5, pady=3)
ent3_sek3 = Entry(sektorius3, textvariable=t3)
ent3_sek3.grid(row=2, column=1, padx=5, pady=3)

lbl4_sek3 = Label(sektorius3, text="Amžius")
lbl4_sek3.grid(row=3, column=0, padx=5, pady=3)
ent4_sek3 = Entry(sektorius3, textvariable=t4)
ent4_sek3.grid(row=3, column=1, padx=5, pady=3)

lbl5_sek3 = Label(sektorius3, text="Skiep.sk.")
lbl5_sek3.grid(row=4, column=0, padx=5, pady=3)
ent5_sek3 = Entry(sektorius3, textvariable=t5)
ent5_sek3.grid(row=4, column=1, padx=5, pady=3)

btn_sek3a = Button(sektorius3, text="Atnaujinti", command=atnaujinti_ir)
btn_sek3a.grid(row=5, column=0, padx=5, pady=3)
btn_sek3b = Button(sektorius3, text="Pridėti", command=add_new)
btn_sek3b.grid(row=5, column=1, padx=5, pady=3)
btn_sek3c = Button(sektorius3, text="Ištrinti", command=istrint_ir)
btn_sek3c.grid(row=5, column=2, padx=5, pady=3)


root.geometry("1050x540")
root.resizable(0, 0)
root.title("COVID19 duombazė")
root.iconbitmap(r'1.ico')

root.mainloop()

# def main():
#     root = tk.Tk()
#     # app = grazinti_db()
#     root.mainloop()
#
# if __name__ == "__main__":
#     main()