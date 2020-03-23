# 2020.03.17. - FGR
# INSTALLED PACKAGES:
# matplotlib threw errors when it was installed with conda.
# I reinstalled these packages with 'pip' and it fixed the errors
# ----------------------------------------------------------------------
# pip list (or conda list)
# pandas                    1.0.2                    pypi_0    pypi
# numpy                     1.18.1           py37h93ca92e_0
# matplotlib                3.2.0                    pypi_0    pypi
# ----------------------------------------------------------------------

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Button

files = ['DATA1', 'DATA2', 'DATA3', 'DATA4', 'DATA5']

fileToOpen = files[1]

# Read the input data
adatok = pd.read_csv('exports\\' + fileToOpen + '.csv', sep = ';')

#print(adatok)

# Set the starting index of the data to be plotted
index = 5

# Convert function for numbers to characters
def convert(uniquesArray) :
    # Create uniqueChars array with the same size as the input
    uniqueCharsArray = uniquesArray
    
    # Enumerate the input array and convert each number to its ASCII character. Simply its chr(c), but we strip the input numbers to be sure
    for index, c in enumerate(uniquesArray) :
        try:
            uniqueCharsArray[index] = chr(int(str(c).strip()))
            index += 1
        except:
            print('error with: ' + str(c))
        
    return uniqueCharsArray

# Update function for the button
def update(event):
    # Increment 'index' by 1
    global index
    index += 1

    # Clear the figure
    plt.clf()

    # Recreate the figure with data from the next column
    plt.scatter(adatok.loc[:,'Relativzeit'], adatok.iloc[:, index])
    plt.xlabel(adatok.columns[index])

    # Recreate the nextButton
    global subax
    subax = plt.axes([0.8, 0.025, 0.1, 0.04])
    global nextButton 
    nextButton = Button(subax, 'Next', color='red', hovercolor='0.975')

    # Actually redraw the figure
    plt.draw()

    # Calculate min and max of the data
    plotMin = np.min(adatok.iloc[:, index])
    plotMax = np.max(adatok.iloc[:, index])

    # Print stats
    if plotMax == plotMin :
        print(str(index) + " - " + adatok.columns[index] + " | constant value: " + str(plotMin))
    else :
        uniques = pd.unique(adatok.iloc[:, index])
        print('Unique values: ' + str(uniques))
        for c in uniques :
            print(c)
            int(str(c).strip())
            print(chr(c))
        print(str(index) + " - " + adatok.columns[index] + " | min: " + str(plotMin) + " | max: " + str(plotMax))

    # Run the update again when clicked
    nextButton.on_clicked(update)

#region REPORT
# Open output file
output = open('exports\\' + fileToOpen + '_processed.csv', 'w')

# Create the header
output.write("Index\tName\tIsConst\tMin\tMax\tUnique values\tUnique values in characters\n")

for i in range(5, 98) :
    plotMin = np.min(adatok.iloc[:, i])
    plotMax = np.max(adatok.iloc[:, i])
    uniques = pd.unique(adatok.iloc[:, i])

    # Case of constant value
    if plotMax == plotMin :
        output.write(str(i) + "\t" + adatok.columns[i] + "\tTrue\t\t\t" + str(uniques.tolist()) + "\t" + str(convert(uniques.tolist())))
        output.write('\n')
    
    # Counter has too many values and is not relevant
    elif adatok.columns[i] == 'ATR.IN.HEADER.RECIEVE_COUNT_B' :
        output.write(str(i) + "\t" + adatok.columns[i] + "\t" + 'Increasing')
        output.write('\n')
    else :
        print(uniques.tolist())
        print(convert(uniques.tolist()))
        output.write(str(i) + "\t" + adatok.columns[i] + "\tFalse\t" + str(plotMin) + "\t" + str(plotMax) + "\t" + str(uniques.tolist()) + "\t" + str(convert(uniques.tolist())))
        output.write('\n')

# Close the output file
output.close()

#endregion

# Create the scatter plot and add labels
plt.scatter(adatok.loc[:,'Relativzeit'], adatok.iloc[:, index])
plt.xlabel(adatok.columns[index])
plt.ylabel('Relativzeit')

# Create the 'next' nextButton
subax = plt.axes([0.8, 0.025, 0.1, 0.04])
nextButton = Button(subax, 'Next', color='red', hovercolor='0.975')

# Enter the update method when clicked
nextButton.on_clicked(update)

# Show plot
#plt.show()