import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

read = pd.read_csv('exports\\NOAA.csv', chunksize = 100, sep = ';')

dataSet1 = pd.DataFrame()
dataSet2 = pd.DataFrame()

dataSet1 = dataSet1.append(next(read))
dataSet2 = dataSet2.append(next(read))

# Plot the two datasets
plt.plot(dataSet1['Temperature'], dataSet1['Pressure Levels'], label = 'Rádiószonda')
plt.plot(dataSet2['Temperature'], dataSet2['Pressure Levels'], label = 'ATOVS')

# Show legend
plt.legend(loc='best')
# Invert the Y-axis
plt.gca().invert_yaxis()
plt.show()