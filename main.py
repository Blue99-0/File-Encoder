from tkinter import *
from tkinter import filedialog
import os

def encodeFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users",
                                          title="Select A File...",
                                          filetypes= (("text files","*.txt"),
                                          ("all files","*.*")))
    file = open(filepath,'r+')
    file.close()
    os.rename(filepath, str(filepath+".crypt"))

def decodeFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users",
                                          title="Select A File...",
                                          filetypes= (("encrypted files","*.crypt"),
                                          ("all files","*.*")))
    file = open(filepath,'r+')
    file.close()
    os.rename(filepath, str(filepath.replace(".crypt", "")))

window = Tk()

window.resizable(False, False)
window.geometry("150x50")
window.title("File Encoder")

button = Button(text="Encode",command=encodeFile)
button2 = Button(text="Decode",command=decodeFile)
button.pack()
button2.pack()
window.mainloop()
