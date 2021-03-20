#6_5 - Write JSON file
import json                         #std libray for JSON support

#create data
data = {}
data['person'] = []
data['person'].append({'name': 'Jimmy Cricket', \
    'address':'1 Disney Way'})
data['person'].append({'name':'Balu', \
    'address':'10 Bare Necessites Place'})

#Write the JSON data
FILENAME = 'data.json'
FILE_MODE = 'w'
with open(FILENAME, FILE_MODE) as json_file:
    json.dump(data,json_file)
