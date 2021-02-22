#import  os library
import os

#define a function to check if directory is valid
def checkDir():
    dirWant = input('Enter the directory you would like to save your file in. : ')
    if os.path.isdir(dirWant) is True: 
        #get info from user for name of file and info to be written to file
        userFile = input('What would you like to name the file? : ')
        userName = input('Please enter your first and last name. : ') 
        userAddress = input('Please enter your address. : ')
        userNumber = input('Please enter your phone number. : ')
        userInfo = (userName + ", " + userAddress + ", " + userNumber)
        #write the info to the file
        with open(userFile, 'w') as fileHandle :
            fileHandle.write(userInfo)
        #read the info written to the file and print what was written back to the user
        with open(userFile, 'r') as fileHandle :
            data = fileHandle.read()
            print(data)
    if os.path.isdir(dirWant) is False:
        print('Sorry, that directory does not exist.')

#call the function
checkDir()