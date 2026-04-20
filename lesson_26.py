#JSON files
#App to app communications

"""
{
    name: Ashwin
    age: 32
    pet: Cat
}
"""
#Imports
import json
filename = 'json.txt'

#To string
outD = dict(name='Ashwin', age='32', pet='Cat')
s = json.dumps(outD) #Dumps puts it to a string
print(f'String={s}')

#To file
with open(filename, 'w') as f:
    json.dump(outD,f) #Dump puts it to a file

#From string
inD = json.loads(s) #Load the dictionary from the string
print(f'Dictionary={inD}')

#From file
with open(filename,'r') as f:
    fD = json.load(f) #Load the dictionary from the file

print(f'Type: {type(fD)} = {fD}')