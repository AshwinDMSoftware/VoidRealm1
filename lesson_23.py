#Reading a text file

#Get a filename
import os, sys

print(f'File: {__file__}') #Built in file name
print(f'Args: {sys.argv}')
sfile = os.path.abspath(sys.argv[0])
print(f'Reading: {sfile}')

#Exists
if not os.path.exists(sfile):
    print('File not found')
    exit(1)

#Open the file
#FileNotFoundError: wrong file path
f = open(sfile,'r')

#Read a line
line = f.readline()
print(line)

#Read number of letters
chars = f.read