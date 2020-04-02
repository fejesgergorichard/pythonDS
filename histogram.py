import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('exports\\XR_DATA1.csv', header = 0, sep=';')

print(data.columns)
selectedColumn = 'IB 512'

beans = pd.unique(data[selectedColumn])
definedBins = []

print(beans.tolist())
for index, entry in enumerate(beans.tolist()):
    definedBins.append(int(str(entry).strip()))

definedBins.sort()
print(definedBins)

plt.hist(data[selectedColumn], bins = definedBins)

plt.show()

input()