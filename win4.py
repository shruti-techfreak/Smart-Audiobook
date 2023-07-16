from msilib.schema import ComboBox
from tkinter import *
from tkinter import font
from tkinter.font import BOLD
from tkinter.ttk import Style
from tkinter import ttk
def nextpage():
    win4.destroy()
    import win5

win4 = Tk()
win4.title('Audiobook')
win4.configure(bg="light blue")
win4.geometry('850x500')
# frame = Frame(win4, width=750, height=400, highlightbackground='Black', highlightthickness=10, bg="light blue")
# frame.grid(row=0, column=0, padx=40, pady=40, ipadx=0, ipady=0)

l = Label(win4, text="Select voice mode,set volume range and also set speed of voice", font="calibri 15 italic",
          fg="red", bg="light blue")
l.place(x=30, y=20)

L1 = Label(win4, text="Voice:", font='times 25 bold', fg="Navy Blue", bg="Light Blue")
L1.place(x=30, y=70)

rlist=["male","female"]
Combo0 = ttk.Combobox(win4, values=rlist, font="calibri 20 italic")
Combo0.set("Select voice mode")
Combo0.place(x=250, y=70)

# R1 = Radiobutton(frame, text="Male", font='times 20 bold', value=1, bg="Light Blue")
# R1.place(x=200, y=70)
# R2 = Radiobutton(frame, text="Female", font='times 20 bold', value=0, bg="Light Blue")
# R2.place(x=400, y=70)

L2 = Label(win4, text="Volume:", font='times 25 bold', fg="Navy Blue", bg="Light Blue")
L2.place(x=30, y=140)
vlist = ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1"]

Combo1 = ttk.Combobox(win4, values=vlist, font="calibri 20 italic")
Combo1.set("Select volume range")
Combo1.place(x=250, y=140)

L3 = Label(win4, text="Speed:", font='times 25 bold', fg="Navy Blue", bg="Light Blue")
L3.place(x=30, y=210)
slist = ["100", "200", "300", "400", "500", "600", "700", "800", "900", "1000"]

Combo2 = ttk.Combobox(win4, values=slist, font="calibri 20 italic")
Combo2.set("Select Speed")
Combo2.place(x=250, y=220)

def get(cmb):
    c=cmb.get()
    return c
m=get(Combo0) #mode
v=get(Combo1) #rate
s=get(Combo2) #speed


enter = Button(win4, text="Enter", fg="Dark Green", bg="Light green", font='Times 20 bold', command=nextpage)
enter.place(x=300, y=290)
win4.mainloop()