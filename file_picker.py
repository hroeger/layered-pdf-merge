import pathlib

from tkinter import filedialog as fd

def open_file_selection():
    filenames = fd.askopenfilenames()

    print(filenames)
    return filenames


open_file_selection()
