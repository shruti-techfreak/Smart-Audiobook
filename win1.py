from msilib.schema import TextStyle
from tkinter import *
from tkinter import font
from tkinter.font import BOLD
from tkinter.ttk import Style


def nextpage():
    win1.destroy()
    import win2

win1=Tk()
win1.title('Audiobook')
win1.geometry('850x500')
frame=Frame(win1,width=1000,height=500,highlightbackground='Black',highlightthickness=10,bg="light blue")
frame.grid(row=0,column=0,padx=40,pady=40,ipadx=50,ipady=50)
l1=Label(frame,text="      Welcome \n     To \n      Smart AudioBooks",font='Times 50',fg='purple',bg="light blue")
l1.grid(row=0,column=0,padx=20,pady=20)
but=Button(frame,text="Proceed",fg="Dark Green",bg="Light green",font='Times 20 bold',command=nextpage)
but.place(x=300,y=270)

win1.mainloop()
