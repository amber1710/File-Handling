from tkinter import *

window = Tk()
window.title('Text Files')
window.geometry("500x400")
window.configure(background="pink")
heading=Label(text="My weekend activities" , bg = "light grey" , fg="black")
heading.pack()
def create():
    file=open('/home/user/Desktop/my_weekend_activities.txt','w+')
    file.write("My weekend was tiring , had to move out of a home that I've grown fond of .")
    file.write("It was a bit sad , new begginings but my body is so sore other than that I had a good weekend")
    file.close()

def display():
    file=open('/home/user/Desktop/my_weekend_activities.txt','r')
    text_display= file.read()
    my_text.insert(END,text_display)
    file.close()


my_text = Text(window,width=40, height=10)
my_text.pack(pady=20)

open_button1= Button(window,text="Create textfile",command=create)
open_button1.place(x=50,y=220)

open_button2=Button(window,text="Display", command=display)
open_button2.place(x=180,y=220)


open_button3 = Button(window,text="Append Data")
open_button3.place(x=260,y=220)


def clear():
    my_text.delete('1.0',END)

open_buttonclear = Button(window,text="Clear", command=clear)
open_buttonclear.place(x=375,y=220)

open_button_exit = Button(window,text="Exit",command=exit)
open_button_exit.place(x=440,y=220)


window.mainloop()
