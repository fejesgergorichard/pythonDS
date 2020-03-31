import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('exports\\XR_DATA1.csv', header = 0, sep=';')

print(data.columns)


beans = pd.unique(data['IB 515'])

print(beans.tolist())
plt.hist(data['IB 515'])

plt.show()

input()