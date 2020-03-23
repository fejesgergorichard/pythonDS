# Syntax:
# GOOD-READ:
# "??????????  ;1111111111  00"
# NO-READ:
# "??????????  200000000000000"
# MULTIPLE CODE:
# "!!!!!!!!!!  A00000000000000"

allBarCodes = []
startingCode = 1111111111

currentCode = startingCode
for i in range(1,255) :
    currentCodeTelegram = '"??????????  ;' + str(currentCode) + '  00"'
    allBarCodes.append(currentCodeTelegram)
    currentCode += 1

print(allBarCodes)