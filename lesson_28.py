#Main Function

#How do we get our code to run automatically

#Determine how the script was runn using "__name__"
print(f'Name: {__name__}')
print(f'File: {__file__}')

#Create some code
def test():
    print('This is a test function')

def main():
    print('This is the main function')
    test()

#Run automatically
if __name__ == '__main__':
    main()

