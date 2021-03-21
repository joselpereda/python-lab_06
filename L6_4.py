#P6_6 Write a binary pickle file for serialization

import pickle                                           #std library for pickle file support
from random import randrange                            #support from randam data

#generate random data from a dictionary
d = {}
for each in range(65,95):
    d[chr(each)] = randrange(1000,2000)
print('Pickle Data: ', d,end='\n\n')

FILENAME ="mypickle.pickle"                             #file to write in current directory
FILE_MODE ="wb"                                         #open for write of binary data

#pickle the generated data
with open(FILENAME, FILE_MODE) as pickle_file:
    pickle.dump(d,pickle_file)
 
#delete the dictionary
del d

#read the pickled data
FILE_MODE = 'rb'
with open(FILENAME, FILE_MODE) as pickle_file:
    pickled_data = pickle.load(pickle_file)

#print pickled data
print('Pickled data: ', pickled_data)



print('Finished Reading:', FILENAME)