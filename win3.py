# from tkinter import *
# from tkinter import font
# from tkinter.font import BOLD
# from tkinter.ttk import Style
#
#
# def nextpage():
#     win3.destroy()
#     import win4
#
# win3 = Tk()
# win3.title('Audiobook')
# win3.geometry('850x500')
# frame = Frame(win3, width=750, height=400, highlightbackground='Black', highlightthickness=10, bg="light blue")
# frame.grid(row=0, column=0, padx=40, pady=40, ipadx=0, ipady=0)
#
# heading = Label(frame, text="Book  Info", font='Imapct 30 bold', fg="Dark Blue", bg="light blue")
# heading.place(x=300, y=20)
#
# l1 = Label(frame, text="Enter name of book \nwhich you want to read:", font='Times 25', fg="Brown", bg="light blue")
# l1.place(x=40, y=70)
#
# l2 = Label(frame, text="Enter page number \nfrom which you want to start reading:", font='Times 25', fg="Brown",
#            bg="light blue")
# l2.place(x=40, y=180)
# enter = Button(frame, text="Enter", fg="Dark Green", bg="Light green", font='Times 20 bold', command=nextpage)
# enter.place(x=300, y=270)
#
# e1 = Entry(frame, bg="light grey", font="Algerian 18 italic")
# e2 = Entry(frame, bg="light grey", font="Algerian 18 italic", width=5)
# e1.place(x=410, y=110)
# e2.place(x=550, y=220)
# book = e1.get()
# pgno = e2.get()

# win3.mainloop()
from tkinter import *
from tkinter import font
from tkinter.font import BOLD
from tkinter.ttk import Style

def nextpage():
    # print(e1.get())
    # print(e2.get())
    win3.destroy()
    import win4

win3 = Tk()
win3.title('Audiobook')
win3.configure(bg="Light blue")
win3.geometry('850x500')
# frame=Frame(win3,width=750,height=400,highlightbackground='Black',highlightthickness=10,bg="light blue")
# frame.grid(row=0,column=0,padx=40,pady=40,ipadx=0,ipady=0)

heading = Label(win3, text="Book  Info", font='Imapct 30 bold', fg="Dark Blue", bg="light blue")
heading.place(x=300, y=20)

l1 = Label(win3, text="Enter name of book \nwhich you want to read:", font='Times 25', fg="Brown", bg="light blue")
l1.place(x=40, y=70)

l2 = Label(win3, text="Enter page number \nfrom which you want to start reading:", font='Times 25', fg="Brown",
           bg="light blue")
l2.place(x=40, y=180)

l2 = Label(win3, text="Enter page number \nfrom where you want to stop reading:", font='Times 25', fg="Brown",
           bg="light blue")
l2.place(x=40, y=300)

enter = Button(win3, text="Enter", fg="Dark Green", bg="Light green", font='Times 20 bold', command=nextpage)
enter.place(x=300, y=400)

e1 = Entry(win3, bg="light grey", font="Algerian 18 italic")
e2 = Entry(win3, bg="light grey", font="Algerian 18 italic", width=5)
e3 = Entry(win3, bg="light grey", font="Algerian 18 italic", width=5)
e1.place(x=410, y=110)
e2.place(x=550, y=220)
e3.place(x=550, y=330)
book = e1.get()
pgno = e2.get()

win3.mainloop()