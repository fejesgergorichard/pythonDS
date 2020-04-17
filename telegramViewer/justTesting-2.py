import tkinter
from tkinter import *
import tkinter.messagebox as messagebox
import pandas as pd

# Create a window variable
gui = tkinter.Tk()
gui.title("Telegram viewer")

width_of_window = 400
height_of_window = 800

screen_width = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()

x_coordinate = screen_width/2 - width_of_window/2
y_coordinate = screen_height/2 - height_of_window/2

gui.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))

var = [
        [StringVar(), StringVar(), StringVar(), StringVar()],
        [StringVar(), StringVar(), StringVar(), StringVar()],
        [StringVar(), StringVar(), StringVar(), StringVar()]
    ]

var = []

for i in range(3):
    entryLine = []
    for j in range(4):
        entryLine.append(StringVar())
    var.append(entryLine)

print(var)

labels = [
            [Label(gui, relief=RAISED, textvariable = var[0][0]), Label(gui, relief=RAISED, textvariable = var[0][1]), Label(gui, relief=RAISED, textvariable = var[0][2]), Label(gui, relief=RAISED, textvariable = var[0][3])],
            [Label(gui, relief=RAISED, textvariable = var[1][0]), Label(gui, relief=RAISED, textvariable = var[1][1]), Label(gui, relief=RAISED, textvariable = var[1][2]), Label(gui, relief=RAISED, textvariable = var[1][3])],
            [Label(gui, relief=RAISED, textvariable = var[2][0]), Label(gui, relief=RAISED, textvariable = var[2][1]), Label(gui, relief=RAISED, textvariable = var[2][2]), Label(gui, relief=RAISED, textvariable = var[2][3])]    
        ]
print()
print(len(labels))

labelsValues = [[48,49,50,51],[52,53,54,55],[70,71,72,73,74]]


i = 0
for row in var:
    j = 0
    for item in row:
        item.set(chr(labelsValues[i][j]))
        j += 1
    i += 1


j = 1
for lists in labels:
    i = 0
    for label in lists:
        label.grid(row = i, column = j)
        label.textvariable = var[j-1][i]
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
    """Function for the Next button. Uses the incrementList function"""
    global var
    global labelsValues

    labelsValues = incrementList(labelsValues, 1)

    i = 0
    for row in var:
        j = 0
        for item in row:
            item.set(chr(labelsValues[i][j]))
            j += 1
        i += 1


nextButton = tkinter.Button(gui, text ="Next", command = buttonFunction)

nextButton.grid(row = i, column = 2)
gui.mainloop()