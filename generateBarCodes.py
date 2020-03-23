# Syntax:
# GOOD-READ:
# "??????????  ;1111111111  00"
# NO-READ:
# "??????????  200000000000000"
# MULTIPLE CODE:
# "!!!!!!!!!!  A00000000000000"


telegramArray = ""
startingCode = 1111111111

for i in range(255) :
    currentCodeTelegram = '"??????????  ;' + str(startingCode + i) + '  00"'
    if i != 254 :
        telegramArray += currentCodeTelegram + ', \n'
    else :
        telegramArray += currentCodeTelegram

print(telegramArray)
with open('generatedBarCodes.txt', 'w') as output :  
    output.write(telegramArray)