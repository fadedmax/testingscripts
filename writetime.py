import datetime

with open("scr.txt", mode='a') as file:
    file.write('Printed string %s recorded at %s.\n' % 
               (scr, datetime.datetime.now()))
