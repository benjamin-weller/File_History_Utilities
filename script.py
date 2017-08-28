import os
import subprocess
from datetime import datetime


def compareDateStrings(strOne, strTwo):
    """This function returns true if string one's date is greater than string two's date."""

    #I am asuming that the format of both of these strings will be
    #YYYY_MM_DD HH_MM_SS "UTC"
    #I'll make a substring of both strings that only has the first 10 digits

    strOneSplit=strOne[1:10].split(sep="_")
    strTwoSplit = strTwo[1:10].split(sep="_")


    first_date=datetime(int(strOneSplit[0]), int(strOneSplit[1]), int(strOneSplit[2]))
    second_date = datetime(int(strTwoSplit[0]), int(strTwoSplit[1]), int(strTwoSplit[2]))

    if first_date>second_date:
        return True
    else:
        return False

def makeFileWritable(file):
    subprocess.run("attrib", "-r", file)

def renameFiles():
    for file in os.listdir("."):
        os.rename(file, file[:indexOfParentheses].strip() + file[indexOfExtension:].strip())

dictionary={}

for file in os.listdir("."):
    if ("(201" in file):
        #Now get the index of the first parenthesis
        indexOfParentheses=file.find("(")
        indexOfExtension=file.find(".")

        #Remove the parenthesis
        file_name= file[:indexOfParentheses].strip() + file[indexOfExtension:].strip()

        #Check to see if the associative array has a key
        if (file_name in dictionary):
            #Then we should get the old value out and compare the two
            oldValue=dictionary[file_name]

            #I'm going to capture only the date portion of the strings
            newFile=file[indexOfParentheses:indexOfExtension].strip()
            oldFile=oldValue[file.find("("):file.find(".")].strip()

            if not compareDateStrings(oldFile, newFile):
            #I can't rely upon basic python lexicographic evaluation simply because our days and month go beyond one digit
            #if oldValue<file:
                #Remove the chronologically older file
                os.remove(oldValue)
                #Update the dictionary so it stays current
                dictionary[file_name]=file

                #Going to make the neweset file writable
 #               makeFileWritable(file)
            else:
                #Remove the chronologically older file
                os.remove(file)

        else:
            #Add to the dictionary
            dictionary[file_name]=file
#            makeFileWritable(file)

renameFiles()


        #os.rename(file, fileName+extension) #For later use