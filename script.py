import stat
import os
from datetime import datetime

"""This program was written to solve an issue I had when moving between operating systems and copying over my
files from the File Histroy backup (Windows backup utility).  Please consult my readme on github for details."""

def compare_date_strings(str_one: str, str_two: str) -> bool:
    """This method takes in two "date strings" from a file name,
    it returns true if string one's date is greater than string two's date.
    I am asuming that the format of both of these parameters will be: YYYY_MM_DD HH_MM_SS "UTC"."""

    #I'll make a substring of both strings that only has the first 10 digits
    str_one_split = str_one.split(sep="_")
    str_two_split = str_two.split(sep="_")


    first_date = datetime(int(str_one_split[0]), int(str_one_split[1]), int(str_one_split[2]))
    second_date = datetime(int(str_two_split[0]), int(str_two_split[1]), int(str_two_split[2]))

    return bool(first_date > second_date)


def rename_files():
    """This method does all the logic for renaming the remaining files."""
    for file in os.listdir("."):
        if "(201" in file:
            os.chmod(file, stat.S_IWRITE)
            os.rename(file, file[:file.find("(")].strip() + file[file.find("."):].strip())


def only_file_name(file: str):
    """This method takes in a file name and returns only the name and extension of that file."""
    return file[:file.find("(")].strip() + file[file.find("."):].strip()


def only_date_portion(file: str):
    """This method takes in a file name and returns only the date portion of the String."""
    start_of_date = file.find("(")+1
    date_string_length = 10 + start_of_date
    return file[start_of_date:date_string_length].strip()


def remove_old_files():
    """This method does all the logic for removing old files."""
    dictionary = {}

    for file in os.listdir("."):
        if "(201" in file:
            # Remove the time stamp parenthesis
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
                    os.remove(file)
            else:
                # Add to the dictionary
                dictionary[file_name] = file


if __name__ == "__main__":
    remove_old_files()
    rename_files()
