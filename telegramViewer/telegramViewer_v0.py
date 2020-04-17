import tkinter
from tkinter import *
import tkinter.messagebox as messagebox
from tkinter import ttk
import pandas as pd

data = pd.read_csv('data/XR_DATA3.csv', sep = ';')
print(data.shape)
print(data.columns)

# Create a window variable
gui = tkinter.Tk()
gui.title("Telegram viewer")

width_of_window = 800
height_of_window = 600

# Get the width and height of the user's screen
screen_width = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()

x_coordinate = screen_width/2 - width_of_window/2
y_coordinate = screen_height/2 - height_of_window/2

# Set the width and height of the window, and place it in the middle of the user's screen
gui.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))

# Create labels for variables
labels = []
for i in range(27):
    entryList = []
    for j in range(16):
        if (j % 2 == 0) :
            newLabel = ttk.Label(gui, relief = GROOVE, text = 's', width = 4, background = '#FFFFFF')
        else :
            newLabel = ttk.Label(gui, relief = GROOVE, text = 's', width = 4, background = '#DDDDDD')
        newLabel.grid(row = i, column = j+1)
        entryList.append(newLabel)
    labels.append(entryList)

i = 0
for entry in labels[len(labels)-2]:
    if (i % 2 != 0) :
        entry.grid_forget()
        #entry['text'] = ''
    else :
        entry['text'] = '17:10:26.432'
        entry['font'] = ("Helvetica", 7)
        entry['width'] = 9
        entry['anchor'] = W
        entry.grid(columnspan = 2, sticky = W)
    i += 1

i = 0
for entry in labels[len(labels)-1]:
    if (i % 2 == 0) :
        entry.grid_forget()
        #entry['text'] = ''
    else :
        entry['text'] = '17:10:26.432'
        entry['font'] = ("Helvetica", 7)
        entry['width'] = 9
        entry['anchor'] = W
        entry.grid(columnspan = 2, sticky = W)
    i += 1

#print('Your labels are: \n' + str(labels))
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