"""
Ide kerülnek grafikai felülettel kapcsolattal dolgok
"""
from tkinter import *
from tkinter import ttk
win = Tk()
win.title('Adatbázis demo')
win.geometry("1020x640") #ablak méret
win.resizable(False, False) #nem méretezhető horizontálisan és vertikálisan


Label(win, text="name", font="Helvetica 12 bold ").grid(row=0, column=0)
name = Entry(win, font="Helvetica 12 bold")
name.grid(row=0, column=1, padx=5, pady=5)


Label(win, text="age", font="Helvetica 12 bold ").grid(row=1, column=0)
age = Entry(win, font="Helvetica 12 bold")
age.grid(row=1, column=1, padx=5, pady=5)


Label(win, text="gender", font="Helvetica 12 bold ").grid(row=2, column=0)
gender = StringVar(win)
gender.set("Select your gender")
genders = OptionMenu(win, gender, "male", "female")
genders.grid(row=2, column=1, padx=5, pady=5)


Label(win, text="score", font="Helvetica 12 bold ").grid(row=3, column=0)
score = Entry(win, font="Helvetica 12 bold")
score.grid(row=3, column=1, padx=5, pady=5)


Button(win, text="Insert data", font="Helvetica 12 bold ").grid(row=4, column=0, columnspan=2, padx=5, pady=5)

#tree view
cols = ("id", "name", "Age", "Gender", "Score")
table = ttk.Treeview(win, columns=cols, show="headings")
for col in cols:
    table.heading(col, text=col)
table.grid(row=5, column=0, columnspan=2, padx=5, pady=5)


Button(win, text="query data", font="Helvetica 12 bold ").grid(row=6, column=0, columnspan=2, padx=5, pady=5)
Button(win, text="export to CSV", font="Helvetica 12 bold ").grid(row=7, column=0, columnspan=2, padx=5, pady=5)


win.mainloop()


