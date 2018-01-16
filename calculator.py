# headrer imports
import sys
from tkinter import *

# creating mainwindow and setting its properties
mainwindow = Tk()
mainwindow.title("Calculator")
# creating frame 1
myframe = Frame(mainwindow)
myframe.pack()
operator = ""
var1 = StringVar()

# creating frame 2
topframe = Frame(mainwindow)
topframe.pack(side=TOP)

# creating frame 3
myframe3 = Frame(mainwindow)
myframe3.pack(side=TOP)

# creating frame 4
myframe4 = Frame(mainwindow)
myframe4.pack(side=TOP)


# defining function for new input on button click
def button_click(number):
    global operator
    operator = operator + str(number)
    var1.set(operator)


# defining function for Clear(C) button press
def allclear():
    global operator
    operator = ""
    input_text.delete(0, END)
    return


# defining function for Equal(=) button press
def equal_clicked():
    global operator
    sum = str(eval(operator))
    var1.set(sum)
    operator = ""


# defining entry box and necessary buttons
input_text = Entry(myframe, textvariable=var1, bd=20, bg='powder blue', font=10, insertwidth=1)
input_text.pack(side=TOP)
button1 = Button(myframe, padx=16, pady=16, bd=8, text="1", bg='powder blue', fg="black",
                 command=lambda: button_click(1))
button1.pack(side=LEFT)
button2 = Button(myframe, padx=16, pady=16, bd=8, text="2", bg='powder blue', fg="black",
                 command=lambda: button_click(2))
button2.pack(side=LEFT)
button3 = Button(myframe, padx=16, pady=16, bd=8, text="3", bg='powder blue', fg="black",
                 command=lambda: button_click(3))
button3.pack(side=LEFT)
button4 = Button(myframe, padx=16, pady=16, bd=8, text="C", bg='powder blue', fg="black", command=allclear)
button4.pack(side=LEFT)

button5 = Button(topframe, padx=16, pady=16, bd=8, text="4", bg='powder blue', fg="black",
                 command=lambda: button_click(4))
button5.pack(side=LEFT)
button6 = Button(topframe, padx=16, pady=16, bd=8, text="5", bg='powder blue', fg="black",
                 command=lambda: button_click(5))
button6.pack(side=LEFT)
button7 = Button(topframe, padx=16, pady=16, bd=8, text="6", bg='powder blue', fg="black",
                 command=lambda: button_click(6))
button7.pack(side=LEFT)
button8 = Button(topframe, padx=16, pady=16, bd=8, text="+", bg='powder blue', fg="black",
                 command=lambda: button_click('+'))
button8.pack(side=LEFT)

button9 = Button(myframe3, padx=16, pady=16, bd=8, text="7", bg='powder blue', fg="black",
                 command=lambda: button_click(7))
button9.pack(side=LEFT)
button10 = Button(myframe3, padx=16, pady=16, bd=8, text="8", bg='powder blue', fg="black",
                  command=lambda: button_click(8))
button10.pack(side=LEFT)
button11 = Button(myframe3, padx=16, pady=16, bd=8, text="9", bg='powder blue', fg="black",
                  command=lambda: button_click(9))
button11.pack(side=LEFT)
button12 = Button(myframe3, padx=16, pady=16, bd=8, text="-", bg='powder blue', fg="black",
                  command=lambda: button_click('-'))
button12.pack(side=LEFT)

button13 = Button(myframe4, padx=16, pady=16, bd=8, text="X", bg='powder blue', fg="black",
                  command=lambda: button_click('*'))
button13.pack(side=LEFT)
button14 = Button(myframe4, padx=16, pady=16, bd=8, text="0", bg='powder blue', fg="black",
                  command=lambda: button_click(0))
button14.pack(side=LEFT)
button15 = Button(myframe4, padx=16, pady=16, bd=8, text="/", bg='powder blue', fg="black",
                  command=lambda: button_click('/'))
button15.pack(side=LEFT)
button16 = Button(myframe4, padx=16, pady=16, bd=8, text="=", bg='powder blue', fg="black", command=equal_clicked)
button16.pack(side=LEFT)

mainwindow.mainloop()
