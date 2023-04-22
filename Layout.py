import tkinter as tk


from tkinter import ttk
import ttkbootstrap as ttk
import Sedista


def sedista1():
    Sedista.sedista()




def open_root():
    
    sedista1()

# window
window = ttk.Window(themename="darkly")
window.title("KCZ Event Menager")
window.attributes("-fullscreen", True)
window.propagate(False)

def exit_window():
    window.destroy()





    




title_lable = ttk.Label(
    master=window, 
    text="P L A N E R   D O G A Đ A J A", 
    font="Calibri 24 bold")
title_lable.place(x=60,y=1)

title_lable = ttk.Label(
    master=window, 
    text="Unesi ime događaja", 
    font="Calibri 24 bold")
title_lable.place(x=60,y=70)
#entry
Događaj_int=tk.StringVar()
Događaj=ttk.Entry(
    window,
    textvariable=Događaj_int, 
    font="Calibri 24 bold")
Događaj.place(x=60,y=140)

#kreiraj event
kreirajevent=ttk.Button(
    master=window, 
    text="Kreiraj event",
    command=lambda: save_input(Događaj, listbox))
kreirajevent.place(x=185, y=200)

def save_input(Događ, listbox):
    input_text = Događaj.get()
    listbox.insert(tk.END, input_text)
    Događaj.delete(0, tk.END)

title_lable = ttk.Label(
    master=window, 
    text="Izaberi događaj", 
    font="Calibri 24 bold")
title_lable.place(x=60,y=270)

buttonx_font = ("Calibri", 24, "bold")
buttonx = ttk.Button(window, text="         Otvori raspored sedenja za selektovani događaj         ", command=open_root)
buttonx.place(x=60, y=752)


options = []
listbox =tk.Listbox(window, height=10,font="Calibri 24 bold")
for option in options:
    listbox.insert(tk.END, option)
listbox.place(x=60, y=340)










#kreiraj event
exit=ttk.Button(
    master=window, 
    text="Zatvori program",
    command=exit_window)
exit.place(x=60, y=1000)




# Run
window.mainloop()

