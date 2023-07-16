from tkinter import *
import pyttsx3
import PyPDF2
import smtplib
# from win2 import name
# def print():
#     print(name)
# from win2 import *
# # import win3
# import win4
# import main
# main.print_hi(win2.name)
# count=89
def readbook():
    import read
# def fun():
#     count=0
win5=Tk()
win5.title('Audiobook')
win5.geometry('850x500')
frame=Frame(win5,width=750,height=400,highlightbackground='Black',highlightthickness=10,bg="light blue")
frame.grid(row=0,column=0,padx=40,pady=40,ipadx=0,ipady=0)


start=Button(frame,text="Start",fg="Purple",bg="pink",font='algerian 20 bold',width=20,height=3,command=readbook)
start.place(x=200,y=20)

finish = Button(frame, text="Finish", fg="Purple", bg="pink", font='algerian 20 bold', width=20, height=3)
finish.place(x=200, y=200)

win5.mainloop()
