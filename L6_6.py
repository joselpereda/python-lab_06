#6_6 - Read JSON file
import json                         #std libray for JSON support

FILENAME = 'data.json'
FILE_MODE = 'r'

with open(FILENAME, FILE_MODE) as json_file:
    data = json.load(json_file)
    for each in data:
        print('JSON DATA: ', data[each])



