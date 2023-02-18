# duplicate-file-scan-using-hash
a Python script to find duplicate files in a given directory using the SHA-1 hash function to compare file contents. It uses the Tkinter library to create a simple GUI for selecting the directory to search for duplicates.

The code first imports necessary libraries:

os: for accessing files and directories
hashlib: for computing the SHA-1 hash of files
tkinter: for creating a GUI
filedialog: for opening a file selection dialog in the GUI
The hash_file function takes a file path and returns the SHA-1 hash of its contents in hexadecimal format. It first creates a new sha1 hash object, then reads the file in binary mode in chunks of 1024 bytes and updates the hash object with each chunk. Finally, it returns the hex digest of the hash.

The check_for_duplicates function takes a path to a directory and returns a list of tuples containing paths to duplicate files and their duplicates. It uses the os.walk method to traverse the directory and its subdirectories and iterates through the files it finds. For each file, it computes its SHA-1 hash using the hash_file function and checks if the hash has been seen before. If it has, it adds the file path and its duplicate to a list of duplicates. If not, it adds the hash and the file path to a dictionary. Finally, it returns the list of duplicates.

The write_to_file function takes a list of duplicates and writes them to a file named 'matches.txt'. It opens the file in write mode and iterates through the list of duplicates, writing each pair of file paths to a new line in the file.

The gui function implements the graphical user interface using the Tkinter library. It creates a new Tkinter object, hides the main window, and opens a file selection dialog. If no directory is selected, it prints an error message and exits. Otherwise, it calls the check_for_duplicates function on the selected directory and prints the list of duplicates to the console. If duplicates are found, it also writes them to a file named 'matches.txt' using the write_to_file function.

Finally, the if __name__ == '__main__': block checks if the script is being run directly (as opposed to being imported as a module) and calls the gui function to start the program.
