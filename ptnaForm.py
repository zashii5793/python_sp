import tkinter as tk
from ptna import *

entry = None
response_area = None
lb = None
action = None
ptna = Ptna('ptna')

def putlog(str):
    lb.insert(tk.END, str)

def prompt():
    p = ptna.get_name
    if (action.get()) == 0:
        p += ':' + ptna.get_responder_name

def taik():

    value = entry.get()

    if not value:

    response_area.configure(text='なに？')
    else:
        response = ptna.dialogue(value)
        response_area.configure(text=response)
        putlog('>' + value)
        putlog(prompt() + response)
        entry.delete(0, tk.END)

 def run():
     global entry, response_area, lb, action

     root = tk.TK() 
     root.geometry('880x560') 
     root.title('Intelligent Agent : ') 
     font=('Helevtetica', 14) 
     font_log=('Helevtetica', 11)

     menubar = tk.Menu(root)
     root.config(menu=menubar)
     filemenu = tk.Menu(menubar)
     menubar.add_cascade(label='ファイル', menu=filemenu)
     filemenu.add_command(label='閉じる', command=root.destroy)   
     action = tk.IntVar()
     optionmenu = tk.Menu(menubar)
     menubar.add_cascade(label='オプション', menu=optionmenu)
     optionmenu.add_radiobutton(
         label='Responderを表示',
         variable = action
         value = 0
     )
     optionmenu.add_radiobutton(
         label='Responderを表示しない',
         variable = action
         value = 1

     )
     canvas = tk.Canvas(
         root,
         width = 500,
         height = 300,
         relief = tk.RIDGE,
         bd = 2
     )
     canvas.place(x=370, y=0)

     img = tk.PhotoImage(file = 'img1.gif')
     canvas.create_image(
         0,
         0,
         image = img,
         anchor = tk.NW
     )

     response_area = tk.Label(
         root,
         width = 50,
         height = 10,
         bg = 'yellow',
         font = font,
         relief = tk.RIDGE,
         bd = 2
     )
     response_area.place(x = 370, y = 305)

     



