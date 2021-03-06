#P6_1 writing a cSV file
#uses the built-in CSV module
import csv
from random import randint

CH = [chr(randint(65,127)) for each in range(10)]       #random characters to write

#set up file access for writing a csv file
FILENAME ="data.csv"                                    #file to write in current directory
FILE_MODE ="w"                                          #READ, WRITE, APPEND R, W, +, BINARY

#creates a file pointer
#creates or overwrites a new file
with open(FILENAME, FILE_MODE,newline='') as csv_file:
    csv_write=csv.writer(csv_file)                      #open file
    csv_write.writerow(CH)                              #write list

print('Finished writing:', FILENAME)