#P6_7 Reading a YAML file
import yaml

#generate date
#dict1 = [{'clark':'Superman', 'bruce':'Batman', 'barry':'The Flash'}]

FILENAME = 'data.yaml'
FILE_MODE = 'r'

#open the file for reading
with open(FILENAME,FILE_MODE) as yaml_file:
    data = yaml.load(yaml_file,Loader=yaml.FullLoader)

print('*'*20)
print('YAML File Read:', FILENAME)
print('YAML File:', data)


