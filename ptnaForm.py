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
        response
