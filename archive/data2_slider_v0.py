import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider, Button

output = open('data2.txt', 'w')
adatok = pd.read_csv('SMALL.csv', sep = ';')

#print(adatok)
fig = plt.subplot()
plt.scatter(adatok.loc[0:20, 'Relativzeit'], adatok.loc[0:20, 'CW_NO_READ'])

xRange = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='red')

f0 = 3
scale = 0.5


#region slider
sxRange = Slider(xRange, 'Scale', 0.1, 300.0, valinit=0.5)

def update(val):
    scale = sxRange.val
    plt.xlim(scale, 400)
    plt.draw()
    #fig.canvas.draw_idle()
sxRange.on_changed(update)
#endregion

plt.show()

#output.write(str(adatok))
#output.close()
