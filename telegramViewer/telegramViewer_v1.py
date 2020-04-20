import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas as pd
import re

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=(canvas.bbox("all"))
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill = BOTH, expand=1)
        scrollbar.pack(side="right", fill="y")

index = 1

root = tk.Tk()
root.title("Telegram viewer")

width_of_window = 650
height_of_window = 850

# Get the width and height of the user's screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_coordinate = screen_width/2 - width_of_window/2
y_coordinate = screen_height/2 - height_of_window/2

# Set the width and height of the window, and place it in the middle of the user's screen
root.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))

# Create a scrollable frame (fitted and packed at the end of program)
frame = ScrollableFrame(root)

# Read data from .csv file
data = pd.read_csv('data/XR_DATA3_Modified.csv', sep = ';')
print(data.shape)
print(data.columns)

#data_transposed = data.transpose()
#data_transposed.to_excel("output.xlsx")

# Create labels for info column:
infoLabels = []
i = 0
for entry in data.columns:
  newLabel = ttk.Label(frame.scrollable_frame, relief = SUNKEN, text = entry, anchor = E, width = 20, font = ("Helvetica", 8))
  newLabel.grid(row = i, column = 0)
  infoLabels.append(newLabel)
  i += 1



# Create labels for variables
labels = []
for i in range(len(infoLabels)):
    entryList = []
    for j in range(16):
        if (j % 2 == 0) :
            newLabel = ttk.Label(frame.scrollable_frame, relief = GROOVE, text = 's', width = 4, background = '#FFFFFF')
        else :
            newLabel = ttk.Label(frame.scrollable_frame, relief = GROOVE, text = 's', width = 4, background = '#DDDDDD')
        # The tkinter .grid() and .pack() function always need to be in a separate row, because they return a 'None' value
        newLabel.grid(row = i, column = j+1)
        entryList.append(newLabel)
    labels.append(entryList)

def refreshLabels():
  """Refreshes the content of the labels based on the imported data's contents"""
  global labels, index, infoLabels
  regexString = "^((I|Q)B\s5)(([2-3][0-9])|(1[5-9]))"
  i = 0
  for row in labels:
    j = 0
    for label in row:
        # If the regular expression finds a match for a row, those values must be shown as characters (IB 515-539 and QB 515-539)
        if (re.match(regexString, infoLabels[i]['text'])) :
            labels[i][j]['text'] = "'" + chr(data[infoLabels[i]['text']][index + j]) + "'"
        else :
            labels[i][j]['text'] = data[infoLabels[i]['text']][index + j]
        j += 1
    i += 1

refreshLabels()

# Modify the first two rows for the Time to be readable
i = 0
for entry in labels[0]:
    if (i % 2 != 0) :
        entry.grid_forget()
        #entry['text'] = ''
    else :
        entry['font'] = ("Helvetica", 6)
        entry['width'] = 12
        entry['anchor'] = W
        entry.grid(columnspan = 2, sticky = W)
    i += 1
i = 0
for entry in labels[1]:
    if (i % 2 == 0) :
        entry.grid_forget()
        #entry['text'] = ''
    else :
        entry['font'] = ("Helvetica", 6)
        entry['width'] = 12
        entry['anchor'] = W
        entry.grid(columnspan = 2, sticky = W)
    i += 1



#print('Your labels are: \n' + str(labels))
print('Number of labels: ' + str(len(labels)) + ' x ' + str(len(labels[0])) + ' = ' + str(len(labels) * len(labels[0])))
print('Length of data: ' + str(len(data)))

def nextButtonFunction():
    """Function for the next button. Uses the refreshLabels() function"""
    global index

    # Stop at the end of the data
    if (index < len(data)) :
        index += 1
        refreshLabels()
    else :
        pass

def backButtonFunction():
    """Function for the back button. Uses the refreshLabels() function"""
    global index

    # Stop at the beginning of the data
    if (index > 1) :
      index -= 1
      refreshLabels()
    else :
      pass


nextButton = tk.Button(frame.scrollable_frame, text ="Next", command = nextButtonFunction)
nextButton.grid(row = 20, column = len(labels[0])+1, rowspan = 2)
backButton = tk.Button(frame.scrollable_frame, text = "Back", command = backButtonFunction)
backButton.grid(row = 22, column = len(labels[0])+1, rowspan = 2)

frame.pack(fill = BOTH, expand=1)
root.mainloop()