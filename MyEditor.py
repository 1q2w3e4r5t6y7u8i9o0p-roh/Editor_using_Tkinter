from Tkinter import *
import os
import  Tkinter, tkFileDialog
from tkMessageBox import *


def open_command_event(event):
    open_command()

def open_command():
    global current_file
    file = tkFileDialog.askopenfilename(initialdir='/', title='Select a file')
    current_file = file
    #print(file)
    #displaying content of the file in editor
    with open(file, 'r+') as file:
        contents = file.read()
        text.insert('1.0', contents)

def newfile_command_event(event):
    newfile_command()

def newfile_command():
    text.delete('1.0', END)


def save_command_event(event):
    save_command()

def save_command():
    global current_file
    print(current_file)
    contents=text.get('1.0','end-1c')
    if current_file is None:
        saveas_command()
    else:
        with open(current_file,'w') as fp:
            fp.write(contents)


def saveas_command():
    contents=text.get('1.0','end-1c')
    file = tkFileDialog.asksaveasfile(mode='w', filetypes=[('all files', '.*'), ('text files', '.txt')])
    file.write(contents)
    file.close()

def exit_command():
    if(askyesno('Are you sure','All the unsaved worked will be discarded. Are you sure to exit?')):
        window.destroy()

def copy_command():
    print('copy')

def statusbar_command():
    global current_file
    status_bar = Label(window,text=current_file, bd=1, relief = SUNKEN,anchor=W)
    if(var.get()):
        status_bar.pack(side=BOTTOM, fill=X)
    else:
        status_bar.pack_forget()


window = Tk()
window.geometry('500x500')
window.title('Editor')
text = Text(window)
text.pack()
window.protocol("WM_DELETE_WINDOW", exit_command)

#shortcuts
window.bind('<Control-s>',save_command_event)
window.bind('<Control-n>',newfile_command_event)
window.bind('<Control-o>',open_command_event)

menubar = Menu(window)
window.config(menu = menubar)

submenu1 = Menu(menubar)
menubar.add_cascade(label='File', menu=submenu1)

#file menu
submenu1.add_cascade(label='New File   Cntrl+N', command=newfile_command)
submenu1.add_cascade(label='Open...    Cntrl+O', command=open_command)
submenu1.add_cascade(label='Save       Cntrl+S', command=save_command)
submenu1.add_cascade(label='Save As', command=saveas_command)
submenu1.add_cascade(label='Exit', command=exit_command)


submenu2 = Menu(menubar)
menubar.add_cascade(label='Edit', menu=submenu2)
#Edit Menu
submenu2.add_cascade(label='Undo    Cntrl+Z')
submenu2.add_cascade(label='Cut    Cntrl+X')
submenu2.add_cascade(label='Paste  Cntrl+V')
submenu2.add_cascade(label='Copy   Cntrl+C')



submenu3 = Menu(menubar)
menubar.add_cascade(label='View', menu=submenu3)
#search menu
var = Tkinter.IntVar()
submenu3.add_checkbutton(label='Status Bar', variable = var, command=statusbar_command)



submenu4 = Menu(menubar)
menubar.add_cascade(label='Help', menu=submenu4)
#help Menu
submenu4.add_cascade(label='View Help')
submenu4.add_cascade(label='About us')





window.mainloop()
