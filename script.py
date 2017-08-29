import stat
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

def renameFiles():
    for file in os.listdir("."):
        if ("(201" in file):
            os.chmod(file, stat.S_IWRITE)
            os.rename(file, file[:file.find("(")].strip() + file[file.find("."):].strip())

def onlyFileName(file):
    return file[:file.find("(")].strip() + file[file.find("."):].strip()

def onlyDatePortion(file):
    return file[file.find("("):file.find(".")].strip()

dictionary = {}

for file in os.listdir("."):
    if ("(201" in file):
        # Remove the time stamp parenthesis
        file_name = onlyFileName(file)

        # Check to see if the associative array has a key
        if (file_name in dictionary):
            # Then we should get the old value out and compare the two
            oldValue = dictionary[file_name]

            if not compareDateStrings(onlyDatePortion(oldValue), onlyDatePortion(file)):
                # Remove the chronologically older file
                os.chmod(oldValue, stat.S_IWRITE)
                os.remove(oldValue)
                # Update the dictionary so it stays current
                dictionary[file_name] = file
            else:
                # Remove the chronologically older file
                os.remove(file)
        else:
            # Add to the dictionary
            dictionary[file_name] = file
renameFiles()
#
# if __name__=="_main_":
#     removeOldFiles()
#     renameFiles()