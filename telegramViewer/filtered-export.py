import pandas as pd
import re

dataIn = pd.read_csv('data/20200420.csv', sep = ';')
regexString = "^((I|Q)B\s5)(([2-3][0-9])|(1[5-9]))"

filterConditions = (dataIn['IB 512']!= 0) | (dataIn['IB 514'] != 0)

for i in range(len(filterConditions)) :
    if filterConditions.iloc[i] == True :
        filterConditions.iloc[i-1] = True
        filterConditions.iloc[i-2] = True
        filterConditions.iloc[i-3] = True


data = dataIn[filterConditions]
print(data.shape)

# Convert all the values for IB 515-531 and QB 515-531 to ASCII characters (checking is done via regex)
for cols in data :
    newList = []
    if (re.match(regexString, cols)) :
        for entry in data[cols] :
            newList.append(chr(entry))
        newData = pd.DataFrame({cols : newList})
        data.update(newData)
        
# Save the transposed dataFrame to an excel file
#data_transposed = data.transpose()
data.to_excel("output_2.xlsx")