import tkinter
from tkinter import *
import tkinter.messagebox as messagebox
import pandas as pd

# Create a window variable
gui = tkinter.Tk()
gui.title("Telegram viewer")

width_of_window = 400
height_of_window = 800

# Get the width and height of the user's screen
screen_width = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()

x_coordinate = screen_width/2 - width_of_window/2
y_coordinate = screen_height/2 - height_of_window/2

# Set the width and height of the window, and place it in the middle of the user's screen
gui.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))

labels = []
for i in range(15):
    entryList = []
    for j in range(30):
        newLabel = Label(gui, relief = GROOVE, text = 's')
        newLabel.grid(row = i, column = j)
        entryList.append(newLabel)
    labels.append(entryList)

print('Your labels are: \n' + str(labels))
print('Number of labels: ' + str(len(labels)) + ' x ' + str(len(labels[0])) + ' = ' + str(len(labels) * len(labels[0])))

def nextStep(inc = 'ejj '):
    global labels

    i = 0
    for row in labels:
        j = 0
        for label in row:
            labels[i][j]['text'] += inc
            j += 1
        i += 1


def buttonFunction():
    """Function for the Next button. Uses the incrementList function"""
    global labels
    nextStep()


nextButton = tkinter.Button(gui, text ="Next", command = buttonFunction)
nextButton.grid(row = len(labels), column = 0)
gui.mainloop()