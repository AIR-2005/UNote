from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import font
from tkinter import ttk

#Font Change Window
class FontWindow(Toplevel):
    def __init__(self,main_window):
        super().__init__()
        #Initialize font window
        self.up_window = main_window
        self.title("Font Window")
        self.geometry("360x240")

        #Create font options
        self.font = StringVar()
        self.font.set("Font")
        self.font_box = ttk.Combobox(self, textvariable=self.font, width=120)
        self.font_box["values"] = [f for f in font.families()]
        self.font_box.pack()

        #Create size options
        self.size = StringVar()
        self.size.set("Size")
        self.size_box = ttk.Combobox(self, textvariable=self.size, width=120)
        self.size_box["values"] = [i for i in range(2, 62, 2)]
        self.size_box.pack()

        #Create change button
        self.change_btn = Button(self, text="Change", command=self.change_size)
        self.change_btn.pack()

    #Change font according to given font and size
    def change_size(self):
        self.up_window.note_box.config(font=(self.font.get(),int(self.size.get())))

#About Window
class AboutWindow(Toplevel):
    def __init__(self):
        super().__init__()
        #Initialize about window
        self.title("UNote About")
        self.geometry("240x60")
        self.aboutTxt = Label(self,text="UNote v2.0")
        self.aboutTxt.pack()


#Main Window
class UNote(Tk):
    def __init__(self):
        #Initialize main window
        super().__init__()
        self.title("UNote")
        self.geometry("720x720")
        #Removes tear off pattern from menus
        self.option_add('*tearOff', FALSE)

        #Menu bar
        self.menu_bar = Menu(self)
        self.config(menu=self.menu_bar)

        #Edit Menu
        self.edit_menu = Menu(self.menu_bar)
        self.menu_bar.add_cascade(label="Edit",menu=self.edit_menu)
        self.edit_menu.add_command(label="Clean",command=self.clean_txt)
        self.edit_menu.add_command(label="Save As",command=self.save_txt)
        self.edit_menu.add_command(label="Open Txt",command=self.open_txt)

        #Style Menu
        self.style_menu = Menu(self.menu_bar)
        self.menu_bar.add_cascade(label="Style", menu=self.style_menu)
        self.style_menu.add_command(label="Font",command=self.font_change)

        #About Menu
        self.about_menu = Menu(self.menu_bar)
        self.menu_bar.add_command(label="About", command=self.about_create)

        #Text Field for writing
        self.note_box = scrolledtext.ScrolledText(self,wrap=WORD,undo=True,autoseparators=True)
        self.note_box.pack(expand=True,fill="both")

        #Run save on exit function when clicked on exit button
        self.protocol("WM_DELETE_WINDOW", self.save_on_exit)

    #Clean text field function for new file
    def clean_txt(self):
        self.note_box.delete(1.0,END)

    #Save text file function for saving txt files
    def save_txt(self):
        file = filedialog.asksaveasfile(defaultextension=".txt",
                                        filetypes=[("Text Files", ".txt"), ("HTML Files", ".html"),
                                                   ("Other Files", ".*")])
        if file is None:
            return
        text = self.note_box.get(1.0, END)
        file.write(text)
        file.close()

    #Open text file function for opening txt files
    def open_txt(self):
        file = filedialog.askopenfile(defaultextension=".txt",
                                      filetypes=[("Text Files", ".txt"), ("HTML Files", ".html"),
                                                 ("Other Files", ".*")])
        if file is None:
            return
        text = file.read()
        #Clean note box
        self.note_box.delete(1.0, END)
        #Insert opened file's text
        self.note_box.insert(1.0, text)
        file.close()

    #Save on exit function for saving txt files after clicking exit button
    def save_on_exit(self):
        #Ask a messagebox for saving file
        save_msg = messagebox.askyesnocancel("Save File", "Do you want to save this file?")
        #If yes, run save text file function
        if save_msg:
            self.save_txt()
        #If canceled, stop messagebox
        elif save_msg is None:
            return
        #If no, close the main window
        elif not save_msg:
            self.destroy()

    #Creates a font change window
    def font_change(self):
        font_window = FontWindow(self)
        font_window.focus()
        font_window.grab_set()

    def about_create(self):
        about = AboutWindow()
        about.focus()
        about.grab_set()

#Main function
if __name__ == "__main__":
    window = UNote()
    window.mainloop()
