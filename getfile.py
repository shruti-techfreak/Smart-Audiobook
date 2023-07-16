import pyttsx3
import PyPDF2
import smtplib
# import win2 as w2
# import win3 as w3
# import win4 as w4

name=input("Enter your name:")
mail=input("Enter your personal mail id:")
# pname=w2.name
# pmail=w2.mail
# pdf_book = open(w3.book, 'rb')
pdf_book=open('smart.pdf', 'rb')
reading_pdf = PyPDF2.PdfFileReader(pdf_book)

#to find number of pages in particular pdf
pdf_pages = reading_pdf.numPages

# #initialising the lib [pyttsx3] for speaking
speaker = pyttsx3.init()

#select page no. from where user wants to start reading
# n=int(w3.pgno)
n=int(input("Enter page number where you want to start reading:"))
s=int(input("Enter page number where you want to stop reading:"))
m = int(input("Choose voice mode either male or female \nEnter 0 for male and 1 for female:"))

for i in range(n-1, s):
    choose_page = reading_pdf.getPage(i)
    # to extract text from pdf for reading
    pdf_text = choose_page.extractText()
    # rate
    rate = speaker.getProperty("rate")
    speaker.setProperty("rate", 150)


    # volume
    volume = speaker.getProperty("volume")
    speaker.setProperty("volume", 0.8)
    # highest volume will be [1]

    # if w4.m=='male':
    #     mode=0
    # else:
    #     mode=1
    # voice
    # set voice [0] for male
    # set voice [1] for female
    voice = speaker.getProperty("voices")
    speaker.setProperty("voice", voice[m].id)

    speaker.say(pdf_text)
    # to run and wait
    speaker.runAndWait()
server=smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('smartaudiobook2022@gmail.com', 'smart@12')
server.sendmail("smartaudiobook2022@gmail.com", mail, "Dear, "+name+"\nThank You so much!!! \nFor reading through our Smart Audiobooks\nI hope you Enjoyed")
server.quit()
