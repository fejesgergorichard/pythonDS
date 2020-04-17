import pandas as pd
import re

data = pd.read_csv('data/XR_DATA3.csv', sep = ';')
regexString = "^((I|Q)B\s5)(([2-3][0-9])|(1[5-9]))"

# Convert all the values for IB 515-531 and QB 515-531 to ASCII characters (checking is done via regex)
for cols in data :
    newList = []
    if (re.match(regexString, cols)) :
        for entry in data[cols] :
            newList.append(chr(entry))
        newData = pd.DataFrame({cols : newList})
        data.update(newData)

# Save the transposed dataFrame to an excel file
data_transposed = data.transpose()
data_transposed.to_excel("output.xlsx")