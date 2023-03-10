import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *




def change_color():
    color = colorchooser.askcolor(title="Choose a color")
    text_area.config(fg=str(color[1]))


def change_font(*args):
    text_area.config(font=(font_name.get(), font_size.get()))


def open_newfile():
    window.title("NEW")
    text_area.delete(1.0, END)


def open_file():
    file = None
    filepath = filedialog.askopenfilename(defaultextension=".txt",
                                          filetypes=[("Text Files", "*.txt"),
                                                     ("All Files", "*.*")])
    global file_path
    file_path = filepath
    print(file_path)
    try:
        window.title(os.path.basename(filepath))
        file = open(filepath, "r")

        text_area.delete(1.0, END)
        text_area.insert(1.0, file.read())

    except BaseException:
        showerror(title="Error",
                  message="Couldn't open file")

    finally:
        if file is None:
            pass
        else:
            file.close()


def saveas_file():
    file = None
    filepath = filedialog.asksaveasfilename(defaultextension=".txt",
                                            initialfile="NEW",
                                            initialdir=r"C:\Users\mayan\OneDrive\Desktop",
                                            filetypes=[("Text Files", "*.txt"),
                                                       ("All Files", "*.*")])
    try:
        window.title(os.path.basename(filepath))
        file = open(filepath, "w")

        file.write(text_area.get(1.0, END))

    except BaseException:
        showerror(title="Error",
                  message="Couldn't save file")
    finally:
        if file is None:
            pass
        else:
            file.close()


def save_file():
    file = None
    filepath = file_path
    print(filepath)

    try:

        file = open(filepath, "w")

        file.write(text_area.get(1.0, END))

    except BaseException:
        showerror(title="Error",
                  message="Couldn't save file")

    finally:
        if file is None:
            pass
        else:
            file.close()


def cut():
    text_area.event_generate("<<Cut>>")


def copy():
    text_area.event_generate("<<Copy>>")


def paste():
    text_area.event_generate("<<Paste>>")


def about():
    showinfo("About", "This is the first mayank text editor")


window = Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = 500
window_height = 500
x_window = int((screen_width - window_width) / 2)
y_window = int((screen_height - window_height) / 2)

window.geometry(f"{window_width}x{window_height}+{x_window}+{y_window}")
window.title("Text Editor")

window.iconbitmap("texteditoricon.ico")

font_name = StringVar(window)
font_name.set("Candara")
font_size = StringVar(window)
font_size.set("14")

text_area = Text(window, font=(font_name.get(), font_size.get()))
scrollbar = ttk.Scrollbar(text_area)
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)

text_area.grid(sticky=N + S + E + W)

frame = ttk.Frame(window)
frame.grid()
change_color_btn = ttk.Button(frame, text="Color", command=change_color)
change_color_btn.grid()  # re

font_box = ttk.OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

font_size_spinner = ttk.Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
font_size_spinner.grid(row=0, column=2)

scrollbar.pack(side="right", fill="y")
text_area.config(yscrollcommand=scrollbar.set)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New File", command=open_newfile)
file_menu.add_command(label="Open File", command=open_file)
file_menu.add_command(label="Save ", command=save_file)
file_menu.add_command(label="Save As", command=saveas_file)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)

help_menu.add_command(label="About", command=about)

window.mainloop()
