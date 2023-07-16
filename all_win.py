from tkinter import *
from tkinter import ttk
import pyttsx3
import PyPDF2
import smtplib
name=''
mail=''
book=''
pgno=0
stno=0
def win1():
    def nextpage():
        win1.destroy()
        win2()

    win1 = Tk()
    win1.title('Audiobook')
    win1.geometry('850x500')
    frame = Frame(win1, width=1000, height=500, highlightbackground='Black', highlightthickness=10, bg="light blue")
    frame.grid(row=0, column=0, padx=40, pady=40, ipadx=50, ipady=50)
    l1 = Label(frame, text="      Welcome \n     To \n      Smart AudioBooks", font='Times 50', fg='purple',
               bg="light blue")
    l1.grid(row=0, column=0, padx=20, pady=20)
    but = Button(frame, text="Proceed", fg="Dark Green", bg="Light green", font='Times 20 bold', command=nextpage)
    but.place(x=300, y=270)
    win1.mainloop()

def win2():
    def nextpage():
        global name,mail
        name = e1.get()
        mail = e2.get()
        win2.destroy()
        win3()

    win2 = Tk()
    win2.title('Audiobook')
    win2.configure(bg="light blue")
    win2.geometry('850x500')
    l1 = Label(win2, text="Enter your name:", font='Times 25', fg="Brown", bg="light blue")
    l1.place(x=30, y=30)

    l2 = Label(win2, text="Enter your personal mail ID:", font='Times 25', fg="Brown", bg="light blue")
    l2.place(x=30, y=100)

    e1 = Entry(win2, bg="light grey", font="Algerian 18 italic")
    e2 = Entry(win2, bg="light grey", font="Algerian 18 italic")
    e1.place(x=410, y=40)
    e2.place(x=410, y=110)

    enter = Button(win2, text="Enter", fg="Dark Green", bg="Light green", font='Times 20 bold', command=nextpage)
    enter.place(x=300, y=270)
    win2.mainloop()

def win3():
    def nextpage():
        global book,pgno,stno
        book = e1.get()
        pgno = e2.get()
        stno = e3.get()
        win3.destroy()
        win4()

    win3 = Tk()
    win3.title('Audiobook')
    win3.configure(bg="Light blue")
    win3.geometry('850x500')

    heading = Label(win3, text="Book  Info", font='Imapct 30 bold', fg="Dark Blue", bg="light blue")
    heading.place(x=300, y=20)

    l1 = Label(win3, text="     Enter book name:", font='Times 25', fg="Brown", bg="light blue")
    l1.place(x=40, y=100)

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

    win3.mainloop()

def win4():
    def nextpage():
        global m,v,s
        def get(cmb):
            c = cmb.get()
            return c

        m = get(Combo0)  # mode
        v = get(Combo1)  # rate
        s = get(Combo2)  # speed
        win4.destroy()
        win5()
    # global m,v,s
    win4 = Tk()
    win4.title('Audiobook')
    win4.configure(bg="light blue")
    win4.geometry('850x500')
    l = Label(win4, text="Select voice mode,set volume range and also set speed of voice", font="calibri 15 italic",
              fg="red", bg="light blue")
    l.place(x=30, y=20)

    L1 = Label(win4, text="Voice:", font='times 25 bold', fg="Navy Blue", bg="Light Blue")
    L1.place(x=30, y=70)

    rlist = ["male", "female"]
    Combo0 = ttk.Combobox(win4, values=rlist, font="calibri 20 italic")
    Combo0.set("Select voice mode")
    Combo0.place(x=250, y=70)

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
    enter = Button(win4, text="Enter", fg="Dark Green", bg="Light green", font='Times 20 bold', command=nextpage)
    enter.place(x=300, y=290)
    win4.mainloop()

def win5():
    def readbook():
        read()

    win5 = Tk()
    win5.title('Audiobook')
    win5.geometry('850x500')
    frame = Frame(win5, width=750, height=400, highlightbackground='Black', highlightthickness=10, bg="light blue")
    frame.grid(row=0, column=0, padx=40, pady=40, ipadx=0, ipady=0)

    start = Button(frame, text="Start", fg="Purple", bg="pink", font='algerian 20 bold', width=20, height=3,command=readbook)
    start.place(x=200, y=20)

    finish = Button(frame, text="Finish", fg="Purple", bg="pink", font='algerian 20 bold', width=20, height=3,command=mailauto)
    finish.place(x=200, y=200)

    win5.mainloop()

def read():
    # pdf_book = open('smart.pdf', 'rb')
    pdf_book = open(book, 'rb')
    reading_pdf = PyPDF2.PdfFileReader(pdf_book)

    #to find number of pages in particular pdf
    pdf_pages = reading_pdf.numPages

     #initialising the lib [pyttsx3] for speaking
    speaker = pyttsx3.init()

    #select page no. from where user wants to start reading
    n=int(pgno)
    sn=int(stno)

    def readn(v,s,m,n,sn):
        for i in range(n - 1, sn):
                choose_page = reading_pdf.getPage(i)
                # to extract text from pdf for reading
                pdf_text = choose_page.extractText()
                # rate
                rate = speaker.getProperty("rate")
                speaker.setProperty("rate", s)

                # volume
                volume = speaker.getProperty("volume")
                speaker.setProperty("volume", v)
                # highest volume will be [1]

                if m == 'male':
                    mode = 0
                else:
                    mode = 1
                # voice mode
                # set voice [0] for male
                # set voice [1] for female
                voice = speaker.getProperty("voices")
                speaker.setProperty("voice", voice[mode].id)

                speaker.say(pdf_text)
                # to run and wait
                speaker.runAndWait()

    readn(v, s, m, n, sn)

def mailauto():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('smartaudiobook2022@gmail.com', 'smart@12')
    server.sendmail("smartaudiobook2022@gmail.com", mail,
                        "Dear, " + name + "\nThank You so much!!! \nFor reading through our Smart Audiobooks\nI hope you Enjoyed")
    server.quit()

win1()


