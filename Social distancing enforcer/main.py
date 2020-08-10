from tkinter import *
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog
from PIL import ImageTk, Image

top = Tk()
top.minsize(400, 260)
top.maxsize(400, 260)
top.iconbitmap('icon.ico')
top.title('Social Distancing Enforcer')

evaluate = None
image = ImageTk.PhotoImage(Image.open('icon.png'))
label = Label(top, image=image)
label.pack(side='top', fill='both', expand='yes')

def onOpen(event=None):
    global evaluate
    dialog = filedialog.Open(top, filetypes=[('MP4 Files', '*.mp4')])
    name = dialog.show()

    if evaluate == None:
        from people_counter import evaluate as e
        evaluate = e
    if name != '':
        top.withdraw()
        evaluate(name)
        top.deiconify()

def onStream(event=None):
    global evaluate
    if evaluate == None:
        from people_counter import evaluate as e
        evaluate = e
    top.withdraw()
    evaluate(None)
    top.deiconify()

def onAbout(event=None):
    messagebox.showinfo('About Software', 'Developed by Isolated Boys')

def onExit(event=None):
    top.quit()

menu = Menu(top)
filemenu = Menu(menu, tearoff=0)
filemenu.add_command(label='Open File', accelerator='Ctrl+O', command=onOpen)
filemenu.add_command(label='Live Stream', accelerator='Ctrl+L', command=onStream)
filemenu.add_separator()
filemenu.add_command(label='Exit Application', accelerator='Ctrl+Q', command=onExit)
menu.add_cascade(label='File', menu=filemenu)
menu.add_cascade(label='About', command=onAbout)
top.bind_all('<Control-o>', onOpen)
top.bind_all('<Control-l>', onStream)
top.bind_all('<Control-q>', onExit)

top.config(menu=menu)
top.mainloop()
