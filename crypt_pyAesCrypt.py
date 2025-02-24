#! /usr/bin/python3
#:::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::www.aiutocomputerhelp.it::::::::::::::::::::::::::
#:::Cripto/Decripto un file di testo:::::::::::2019:::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::

#import tkinter as tk #per finestra 
from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import LabelFrame
from tkinter import Label
from tkinter import Button

import pyAesCrypt

def scelgofile():
    
    filescelto = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
    file.delete(0, END)
    file.insert(0, filescelto)
    valore_password.focus_set()
   
# Cifro

def cifra():
    bufferSize = 64 * 1024
    key = valore_password.get()
    filename = file.get()
    pyAesCrypt.encryptFile(filename, filename +".aes", key, bufferSize)


def decifra():
    bufferSize = 64 * 1024
    key = valore_password.get()
    filename = file.get()
    pyAesCrypt.decryptFile(filename, filename +".inchiaro", key, bufferSize)

    
finestra = Tk()
finestra.resizable(True,True)
finestra.title("www.aiutocomputerhelp.it Cifriamo/Decifriamo con pyAesCrypt")
finestra.geometry('700x300')

 
rows = 0
while rows < 40:
    finestra.rowconfigure(rows, weight=1)
    finestra.columnconfigure(rows,weight=1)
    rows += 1



Input_step = LabelFrame(finestra,text="Cripto / Decripto", font="Arial 12 bold italic")

Input_step.grid(row=1,column=1, columnspan=57 ,rowspan = 10, sticky='W', padx=1, pady=1, ipadx=10, ipady=15)


Label(Input_step, text="File ").grid(row=2, column=1)
Label(Input_step, text="Password").grid(row=7, column=1)

Label(Input_step, text="                           Scegli l'operazione da compiere").grid(row=8, column=20)
 
#input File Criptare
file = Entry(Input_step, width=40)
file.grid(row=2, column=20)

#input Password
valore_password = Entry(Input_step,width=40)
valore_password.grid(row=7, column=20)
file.focus_set()

#Tasto scelta file
scelgo_button = Button(Input_step)
scelgo_button.configure(text='Scegli File', command=scelgofile)
scelgo_button.grid(row=2, column=46)

#Tasto Cripta
cifra_button = Button(Input_step)
cifra_button.configure(text='  Cripta  ', command=cifra)
cifra_button.grid(row=10, column=20)

#Tasto DeCripta
decifra_button = Button(Input_step)
decifra_button.configure(text='  De-Cripta  ', command=decifra)
decifra_button.grid(row=10, column=21)




#Label(Input, text="Ed ora potete eseguirlo su Microsoft, Mac , Linux , Smartphone Android .... ").grid(row=2, column=1)

 
finestra.mainloop()
