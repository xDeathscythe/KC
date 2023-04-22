
import tkinter as tk
import sqlite3
import KCFINAL
from KCFINAL import SeatingProgram



def open_root():
    selection = listbox.curselection()
    if selection:
        option = listbox.get(selection[0])
        seating_program = SeatingProgram(option)
        seating_program.event_name(option)
        seating_program.run(option)

# window
window = tk.Tk()
window.configure(bg="black")
window.attributes("-fullscreen", True)
window.propagate(False)

def exit_window():
    window.destroy()




title_lable = tk.Label(
    master=window, 
    text="P L A N E R   D O G A Đ A J A", 
    font="Calibri 24 bold",
    fg="white",
    bg="black")

title_lable.place(x=60,y=1)

title_lable = tk.Label(
    master=window, 
    text="Unesi ime događaja", 
    font="Calibri 24 bold",
    fg="white",
    bg="black")
title_lable.place(x=60,y=70)
#entry
Događaj_int=tk.StringVar()
Događaj=tk.Entry(
    window,
    textvariable=Događaj_int, 
    font="Calibri 24 bold",
    fg="white",
    bg="black")
Događaj.place(x=60,y=140)

#kreiraj event
kreirajevent=tk.Button(
    master=window,
    fg="white",
    bg="black", 
    text="Kreiraj event",
    command=lambda: save_input(Događaj, listbox))
kreirajevent.place(x=185, y=200)

def save_input(Događ, listbox):
    input_text = Događaj.get()
    listbox.insert(tk.END, input_text)
    Događaj.delete(0, tk.END)

title_lable = tk.Label(
    master=window, 
    text="Izaberi događaj", 
    font="Calibri 24 bold",
    fg="white",
    bg="black")
title_lable.place(x=60,y=270)


#kreiraj event
buttonx = tk.Button(window,fg="white",
    bg="black", text="         Otvori raspored sedenja za selektovani događaj         ", command=open_root)

buttonx.place(x=60, y=752)

options = []
listbox =tk.Listbox(window, height=10,font="Calibri 24 bold",fg="white",
    bg="black")
for option in options:
    listbox.insert(tk.END, option)
listbox.place(x=60, y=340)










#kreiraj event
exit=tk.Button(
    master=window,fg="white",
    bg="black", 
    text="Zatvori program",
    command=exit_window)
exit.place(x=60, y=1000)




# Run
window.mainloop()

