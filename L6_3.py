#P6_3 Read a CSV file
import csv
FILENAME ="data.csv"                                    #file to write in current directory
FILE_MODE ="r"                                          #set file mode to read

with open(FILENAME, FILE_MODE,newline='') as csv_file:
    csv_read=csv.reader(csv_file)                       #open file
    for each in csv_read:            
        print(each)

print('Finished Reading:', FILENAME)