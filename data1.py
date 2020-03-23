# DB413.DBB96 is the first ATR IN INFO
startingAddress = 96
output = open('DB413_ATR.txt', 'w')


for i in range(32):
    if i == 0:
        output.write('Symbol\tInOut\tDatablock\tAddress\tType\tComment\tDefault\tImplicitSource\tImplicitSignal\n')
    else:
        output.write('Ujabb Sor: ' + str(i) + '\n')
output.close()