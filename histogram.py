import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('exports\\XR_DATA3.csv', header = 0, sep=';')

print(data.columns)
selectedColumn = 'IB 512'

beans = pd.unique(data[selectedColumn])
definedBins = []

print(beans.tolist())
for index, entry in enumerate(beans.tolist()):
    definedBins.append(int(str(entry).strip()))

definedBins.sort()
print(len(definedBins))
length = len(definedBins)

plt.hist(data[selectedColumn], bins = length, histtype='bar')
plt.xticks(definedBins)
plt.show()