import tkinter
from tkinter import *
import tkinter.messagebox as messagebox

top = tkinter.Tk()


var = [
        [StringVar(), StringVar(), StringVar()],
        [StringVar(), StringVar(), StringVar()]
    ]

a = 48
b = 49
c = 50
for row in var:
    for entry in row:
        entry.set(chr(a))

label_0 = Label(top, textvariable=var[1][1], relief=RAISED).grid(row=0, sticky=W, )
label_01 = Label(top, textvariable=var[0][1], relief=RAISED).grid(row = 0, column = 1, sticky = W)
label_1 = Label(top, textvariable=var[1][2], relief=RAISED ).grid(row = 1, sticky = W)
label_2 = Label(top, textvariable=var[1][0], relief=RAISED ).grid(row = 1, column = 1, sticky = E)

labels = [
            [Label(top, textvariable=var[0], relief=RAISED), Label(top, textvariable=var[0], relief=RAISED), Label(top, textvariable=var[0], relief=RAISED), Label(top, textvariable=var[0], relief=RAISED)],
            [Label(top, textvariable=var[0], relief=RAISED), Label(top, textvariable=var[0], relief=RAISED), Label(top, textvariable=var[0], relief=RAISED), Label(top, textvariable=var[0], relief=RAISED)]
        ]

var[1][1].set("fasz")

def helloCallBack():
    #messagebox.showinfo( "Updated.")
    global a,b,c
    a += 1
    b += 1
    c += 1
    var[0][1].set(chr(a))
    var[0][1].set(chr(b))
    var[0][2].set(chr(c))


B = tkinter.Button(top, text ="Next", command = helloCallBack)



B.grid(row = 4)
top.mainloop()