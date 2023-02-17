import os
import hashlib
import tkinter as tk
from tkinter import filedialog

def hash_file(filename):
    """"This function returns the SHA-1 hash
    of the file passed into it"""

    # make a hash object
    h = hashlib.sha1()

    # open file for reading in binary mode
    with open(filename, 'rb') as file:

        # loop till the end of the file
        chunk = 0
        while chunk != b'':
            # read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)

    # return the hex representation of digest
    return h.hexdigest()

def check_for_duplicates(path):
    """This function checks for duplicates in the given directory"""
    files_list = {}
    duplicates = []

    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            file_path = os.path.join(r, file)
            file_hash = hash_file(file_path)

            if file_hash in files_list:
                duplicates.append((file_path, files_list[file_hash]))
            else:
                files_list[file_hash] = file_path

    return duplicates

def write_to_file(duplicates):
    """This function writes the duplicates to a file named 'matches.txt'"""
    with open("matches.txt", "w") as file:
        for duplicate in duplicates:
            file.write(f"{duplicate[0]} - {duplicate[1]}\n")

def gui():
    """This function implements the GUI"""
    root = tk.Tk()
    root.withdraw()

    path = filedialog.askdirectory()

    if not path:
        print("No directory selected. Exiting program.")
        return

    duplicates = check_for_duplicates(path)

    if duplicates:
        print("Duplicates found:")
        for duplicate in duplicates:
            print(f"{duplicate[0]} - {duplicate[1]}")
        write_to_file(duplicates)
        print(f"Duplicates written to file 'matches.txt'")
    else:
        print("No duplicates found.")

if __name__ == '__main__':
    gui()
