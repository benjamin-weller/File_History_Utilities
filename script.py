import re
import stat
import os
from datetime import datetime


"""This program was written to solve an issue I had when moving between operating systems and copying over my
files from the File Histroy backup (Windows backup utility).  Please consult my readme on github for details."""


def compare_date_strings(str_one: str, str_two: str) -> bool:
    """This method takes in two "date strings" from a file name.
    It returns true if string one's date is greater than string two's date.
    I am asuming that the format of both of these parameters will be: YYYY_MM_DD_HH_MM_SS."""

    str_one_split = str_one.split(sep="_")
    str_two_split = str_two.split(sep="_")

    first_date = datetime(int(str_one_split[0]), int(str_one_split[1]), int(str_one_split[2]),
                          hour=int(str_one_split[3]), minute=int(str_one_split[4]),
                          second=int(str_one_split[5]))
    second_date = datetime(int(str_two_split[0]), int(str_two_split[1]), int(str_two_split[2]),
                           hour=int(str_two_split[3]), minute=int(str_two_split[4]),
                           second=int(str_two_split[5]))

    return bool(first_date > second_date)


def rename_files():
    """This method does all the logic for renaming the remaining files."""
    for file in os.listdir("."):
        try:
            if re.search(r"\d{4}_\d{2}_\d{2} \d{2}_\d{2}_\d{2} UTC", file):
                os.chmod(file, stat.S_IWRITE)
                os.rename(file, only_file_name(file))
        except WindowsError:
            print("It appears we can't rename " + file +
                  " to " + only_file_name(file) + " because a file by that name already exists.")
            print("Please navigate to " + os.getcwd() + " and resolve this problem.")


def only_file_name(file: str) -> str:
    """This method takes in a file name and returns only the name and extension of that file."""

    # The below line is safe becuase I checked for it before
    result = re.search(r"\d{4}_\d{2}_\d{2} \d{2}_\d{2}_\d{2} UTC", file)

    return file[:result.start() - 1].strip() + file[file.rfind("."):]


def only_date_portion(file: str) -> str:
    """This method takes in a file name and returns only the date and time portion of the String."""

    # The below line is safe becuase I checked for it before
    result = re.search(r"\d{4}_\d{2}_\d{2} \d{2}_\d{2}_\d{2}", file)

    # Returns the string in the format I need for easy comparisions
    return file[result.start():result.end()].replace(" ", "_")


def remove_old_files():
    """This method does all the logic for removing old files."""
    dictionary = {}

    for file in os.listdir("."):
        if re.search(r"\d{4}_\d{2}_\d{2} \d{2}_\d{2}_\d{2} UTC", file):
            # Remove the time stamp
            file_name = only_file_name(file)

            # Check to see if the associative array has a key
            if file_name in dictionary:
                # Then we should get the old value out and compare the two
                old_value = dictionary[file_name]

                if not compare_date_strings(only_date_portion(old_value), only_date_portion(file)):
                    # Remove the chronologically older file
                    os.chmod(old_value, stat.S_IWRITE)
                    os.remove(old_value)
                    # Update the dictionary so it stays current
                    dictionary[file_name] = file
                else:
                    # Remove the chronologically older file
                    os.chmod(file, stat.S_IWRITE)
                    os.remove(file)
            else:
                # Add to the dictionary
                dictionary[file_name] = file


def recursive_walk(path_to_rootdir):
    """This recursive method will start at a specified directory, walk from the top down, renaming and removing files as it goes."""

    for my_tuple in os.walk(path_to_rootdir):
        dirpath, dirdirectories, dirfiles = my_tuple
        os.chdir(dirpath)
        remove_old_files()
        rename_files()


if __name__ == "__main__":
    path = input("Please enter a root directory for the beginning of the recursive rename: ")
    assert os.path.exists(path), "I did not find the directory at, " + str(path)
    recursive_walk(path)
