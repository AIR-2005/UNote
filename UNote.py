from tkinter import *
from tkinter import filedialog

def save_txt():
    file = filedialog.asksaveasfile(defaultextension='.txt',filetypes=[("Text File",".txt"),("HTML File",".html"),("Other Files",".*")])
    if file is None:
        return
    text = noteBox.get(1.0,END)
    file.write(text)
    file.close()


root = Tk()
root.title("UNote")
root.geometry("720x720")

noteBox = Text(root, width=720)
noteBox.pack()

saveBtn = Button(root, text="Save", command=save_txt)
saveBtn.pack()

root.mainloop()