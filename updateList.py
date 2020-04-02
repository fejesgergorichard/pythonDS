import tkinter
from tkinter import *
import tkinter.messagebox as messagebox

top = tkinter.Tk()


var = [
        [StringVar(), StringVar(), StringVar(), StringVar()],
        [StringVar(), StringVar(), StringVar(), StringVar()]
    ]

labels = [
            [Label(top, relief=RAISED), Label(top, relief=RAISED), Label(top, relief=RAISED), Label(top, relief=RAISED)],
            [Label(top, relief=RAISED), Label(top, relief=RAISED), Label(top, relief=RAISED), Label(top, relief=RAISED)]  
        ]

labelsValues = [[48,49,50,51],[52,53,54,55]]

j = 0
for lists in labels:
    i = 0
    for label in lists:
        label.grid(row = i, column = j)
        label.textvariable = var[j][i]
        i += 1
    j += 1


def incrementList(oldValues):
    newValues = oldValues
    i = 0
    for row in oldValues:
        j = 0
        for entry in row:
            newValues[i][j] = entry + 1
            j += 1
        i += 1

    return newValues

def buttonFunction():
    #messagebox.showinfo( "Updated.")
    global var
    global labelsValues

    labelsValues = incrementList(labelsValues)
    print(labelsValues)

    i = 0
    j = 0
    for row in var:
        for item in row:
            item.set(chr(labelsValues[i][j]))
            j += 1
        i += 1
        j = 0



B = tkinter.Button(top, text ="Next", command = buttonFunction)

B.grid(row = i)
top.mainloop()