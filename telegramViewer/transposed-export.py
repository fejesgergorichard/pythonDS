import pandas as pd
import re

data = pd.read_csv('data/XR_DATA3.csv', sep = ';')
regexString = "^((I|Q)B\s5)(([2-3][0-9])|(1[5-9]))"

for cols in data :
    newList = []
    if (re.match(regexString, cols)) :
        for entry in data[cols] :
            newList.append(chr(entry))
        newData = pd.DataFrame({cols : newList})
        data.update(newData)


data_transposed = data.transpose()
data_transposed.to_excel("output.xlsx")