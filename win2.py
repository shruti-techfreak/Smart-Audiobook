# from tkinter import *
# from tkinter import font
# from tkinter.font import BOLD
# from tkinter.ttk import Style
#
# def nextpage():
#     # name = e1.get()
#     # mail = e2.get()
#     # name = get(e1)
#     # mail = get(e2)
#     # print(n)
#     # print(m)
#     win2.destroy()
#     import win3
#
# win2 = Tk()
# win2.title('Audiobook')
# win2.geometry('850x500')
# frame = Frame(win2, width=750, height=400, highlightbackground='Black', highlightthickness=10, bg="light blue")
# frame.grid(row=0, column=0, padx=40, pady=40, ipadx=0, ipady=0)
# l1 = Label(frame, text="Enter your name:", font='Times 25', fg="Brown", bg="light blue")
# l1.place(x=30, y=30)
#
# l2 = Label(frame, text="Enter your personal mail ID:", font='Times 25', fg="Brown", bg="light blue")
# l2.place(x=30, y=100)
#
# # name=win2.StringVar()
# # mail=win2.StringVar()
#
# nentry=Entry(frame,width=40,bg="light grey")
# mentry=Entry(frame,width=40,bg="light grey")
# nentry.place(x=350,y=50)
# mentry.place(x=450,y=120)
#
# name=nentry.get()
# mail=mentry.get()
# print(name)
# print(mail)
#
# enter = Button(frame, text="Enter", fg="Dark Green", bg="Light green", font='Times 20 bold', command=nextpage)
# enter.place(x=300, y=270)
#
# win2.mainloop()
from tkinter import *
from tkinter import font
from tkinter.font import BOLD
from tkinter.ttk import Style
global name
def nextpage():

    name=e1.get()
    mail=e2.get()
    # print(name)
    # print(mail)
    win2.destroy()
    import win3


win2 = Tk()
win2.title('Audiobook')
win2.configure(bg="light blue")
win2.geometry('850x500')
# frame=Frame(win2,width=750,height=400,highlightbackground='Black',highlightthickness=10,bg="light blue")
# win2.grid(row=0,column=0,padx=40,pady=40,ipadx=0,ipady=0)
l1 = Label(win2, text="Enter your name:", font='Times 25', fg="Brown", bg="light blue")
l1.place(x=30, y=30)

l2 = Label(win2, text="Enter your personal mail ID:", font='Times 25', fg="Brown", bg="light blue")
l2.place(x=30, y=100)

e1 = Entry(win2, bg="light grey", font="Algerian 18 italic")
e2 = Entry(win2, bg="light grey", font="Algerian 18 italic")
e1.place(x=410, y=40)
e2.place(x=410, y=110)
# name=e1.get()
# mail=e2.get()
enter = Button(win2, text="Enter", fg="Dark Green", bg="Light green", font='Times 20 bold', command=nextpage)
enter.place(x=300, y=270)
win2.mainloop()