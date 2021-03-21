#P6_7 Reading and writing a YAML file
import yaml

#generate date
dict1 = [{'clark':'Superman', 'bruce':'Batman', 'barry':'The Flash'}]

FILENAME = 'data.yaml'
FILE_MODE = 'w'

#open the file for wrting
with open(FILENAME,FILE_MODE) as yaml_file:
    data = yaml.dump(dict1,yaml_file)

