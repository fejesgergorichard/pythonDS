import tkinter
from tkinter import *
import tkinter.messagebox as messagebox

top = tkinter.Tk()


var = [
        [StringVar(), StringVar(), StringVar(), StringVar()],
        [StringVar(), StringVar(), StringVar(), StringVar()],
        [StringVar(), StringVar(), StringVar(), StringVar()]
    ]

labels = [
            [Label(top, relief=RAISED, textvariable = var[0][0]), Label(top, relief=RAISED, textvariable = var[0][1]), Label(top, relief=RAISED, textvariable = var[0][2]), Label(top, relief=RAISED, textvariable = var[0][3])],
            [Label(top, relief=RAISED, textvariable = var[1][0]), Label(top, relief=RAISED, textvariable = var[1][1]), Label(top, relief=RAISED, textvariable = var[1][2]), Label(top, relief=RAISED, textvariable = var[1][3])],
            [Label(top, relief=RAISED, textvariable = var[2][0]), Label(top, relief=RAISED, textvariable = var[2][1]), Label(top, relief=RAISED, textvariable = var[2][2]), Label(top, relief=RAISED, textvariable = var[2][3])]    
        ]

labelsValues = [[48,49,50,51],[52,53,54,55],[70,71,72,73,74]]


i = 0
for row in var:
    j = 0
    for item in row:
        item.set(chr(labelsValues[i][j]))
        print(item.get())
        j += 1
    i += 1


j = 1
for lists in labels:
    i = 0
    for label in lists:
        label.grid(row = i, column = j)
        label.textvariable = var[j-1][i]
        print(label.textvariable)
        i += 1
    j += 1

def incrementList(oldValues, inc = 1):
    """Increments the integers stored in a given list by inc, which is 1 by default"""
    newValues = oldValues
    i = 0
    for row in oldValues:
        j = 0
        for entry in row:
            newValues[i][j] = entry + inc
            j += 1
        i += 1
    return newValues


def buttonFunction():
    #messagebox.showinfo( "Updated.")
    global var
    global labelsValues

    labelsValues = incrementList(labelsValues, 1)

    i = 0
    for row in var:
        j = 0
        for item in row:
            item.set(chr(labelsValues[i][j]))
            print(item.get())
            j += 1
        i += 1


B = tkinter.Button(top, text ="Next", command = buttonFunction)

B.grid(row = i, column = 2)
top.mainloop()