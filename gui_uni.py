#!/usr/bin/env python
import os
import tkinter
from tkinter import *
from tkinter.messagebox import *
import tkinter.messagebox
import string
import imp
import matplotlib
import matplotlib.pyplot
import matplotlib.image


 #This code (gui_uni.py) creates GUI for an executable module. 
 #It requires the configuration file named gui.conf structured as follows. 
 #The first line is the working directory      DIR. 
 #The second line is the executable file name  EXE. 
 #The third line is the argument file:          ARG. 
 #The ARG file contains control parameters and list of other input data files: F. 
 #All files (EXE, ARG, and F) are located in the same directory DIR. 
 #Starting the program. 
 #      open terminal window. 
 #      change directory to where files gui_uni.py and gui.conf are located. 
 #      run command line: python.exe gui_uni.py . 
 #Note. it could be necessary to use the full path to python.exe 

file_conf = 'gui.conf'
par_name = []
par_val  = []


#reading gui configuration file to get parameter names and parameter initial values (or list of values for drop-down menu items)
def read_conf(file_conf):
    try:
        f = open(file_conf, 'r')
    except:
        messagebox.showinfo("showinfo", "File "+file_conf+' is not available')
    line="_"
    k = 0
    while (line != ''):
        line = f.readline().strip()        #stripping end symbol/n
        line_split = line.split(',')
        n = len(line_split)
        if len(line_split[0]) !=0:
            par_name.append(line_split[0])    # parameter name
        pars = []                         # array of values (one or more)
        for j in range(1,n):
            pars.append(line_split[j])
        if len(pars) !=0:
            par_val.append(pars)              # adding value items to the name
    n_base = len(par_val)
    f.close()
    return n_base
    

def read_comm_file(file_comm):
    try:
        f = open(file_comm, 'r')
    except:
        tkinter.messagebox.showinfo("showinfo", "File "+file_comm+' is not available')
    line="_"
    k = 0
    while (line != ''):
        line = f.readline().strip()        #stripping end symbol/n
       
        line_split = line.split(',')
        
        n = len(line_split)
        if len(line_split[0]) != 0:
            par_name.append(line_split[0])    # parameter name
        val = []                         # array of values (one or more)
        for j in range(1,n):
            val.append(line_split[j])
        if len(val) != 0:
            par_val.append(val)              # adding value items to the name
    f.close()

parameters = ''
# is executed by the button RUN
def run(dir0,dir,command, comm_file, n_base):
    os.chdir(dir)

    save_contr(n_menu, f_contr)

    os.system(command) 

    os.chdir(dir_0)
    print('saving configuration to ', file_conf)
    f = open(file_conf, 'w')         # opening configuration file to update parameters
    for i in range(0,n_base):
        f.write(par_name[i])
        for j in range(0,len(par_val[i])):
            if(len(par_val[i]) > 1):
                f.write(','+par_val[i][j])
            if(len(par_val[i]) == 1):
                f.write(','+ par[i].get())
        f.write('\n')
    f.close()
    f = open(comm_file, 'w')         # opening ...
    for i in range(n_base,len(par_name)):
        f.write(par_name[i])
        for j in range(0,len(par_val[i])):
            if(len(par_val[i]) > 1):
                f.write(','+par_val[i][j])
            if(len(par_val[i]) == 1):
                f.write(','+ par[i].get())
        f.write('\n')
    f.close()

    result_file = dir + '/' +par_val[3][0]
    f = open(result_file, "r")
    res_txt = f.read()
    f.close()

    top = Toplevel()
    top.title("Result of calibration:")
    content = Text(top, font=("Times", 14), bg="light cyan", fg="black")
    content.insert(INSERT, res_txt)
    content.grid(row=0, column=0, sticky=W+E)
    yscroll = Scrollbar(top, command=content.yview, orient=VERTICAL)
    yscroll.grid(row=0, column=1, rowspan=1, sticky=N + S)
    content.configure(yscrollcommand=yscroll.set)
    button = Button(top, text="Close", command=top.destroy).grid(row=1,column=0)
    top.mainloop()

def show_edit_txt_file(file_name,width,height): 
    f = open(file_name, "r")
    txt = f.read()
    f.close()
    loc_root = Tk()
    loc_root.title(file_name)
    content = Text(loc_root, width=width, height=height, wrap='none', font=("Times", 14), bg="light cyan", fg="black")
    content.insert(INSERT, txt)
    content.grid(row=0, column=0, sticky=N + S)
    yscroll = Scrollbar(loc_root, command=content.yview, orient=VERTICAL)
    yscroll.grid(row=0, column=1, rowspan=1, sticky=N + S)
    content.configure(yscrollcommand=yscroll.set)
    xscroll = Scrollbar(loc_root, command=content.xview, orient=HORIZONTAL)
    xscroll.grid(row=1, column=0, columnspan=1, sticky=W + E)
    content.configure(xscrollcommand=xscroll.set)
    Button(loc_root, bg='black', fg='pale green', text='Save', font=("Arial", 12, "bold"), command=lambda: save_widget_text(content, file_name)).grid(row=3, column=0, columnspan=2, sticky=W+E)
    Button(loc_root, bg='black', fg='aquamarine', text='Close window',font=("Arial", 12, "bold"), command=lambda: loc_root.destroy()).grid(row=4, column=0, columnspan=2, sticky=W + E)
    Label(loc_root, bg='black', fg='yellow', text='Restart if saved',font=("Arial", 12, "bold")).grid(row=5, column=0, columnspan=2, sticky=W + E)
    loc_root.mainloop()	

def save_widget_text(content,fname):
    text = content.get("1.0", END)
    f = open(fname, "w")
    f.write(text)
    f.close()

def save_contr(m,fname):
    f = open(fname, "w")
    for i in range(n_base,m):
        text = par[i].get()
        print(text+'\n')
        f.write(text+'\n')
    f.close()



n_base = read_conf(file_conf)         # reading configuration file 
dir = par_val[0][0]

files2open = []
for i in range(3,n_base):
    files2open.append(dir + '/' + str(par_val[i][0]))



comm_file = dir + '/' +par_val[2][0]
read_comm_file(comm_file)

n_menu = len(par_name) 

width= 40
height = 25

# creating menu
root = Tk()
root.title("uni")
    

km1 = n_menu
n_col = 0
par = []
k = 0
for i in range(0,n_menu):
    if(len(par_val[i]) == 1):       # menu items with value which can be manually entered
        Label(root, text= par_name[i],borderwidth=2 ).grid(row=k,column=n_col,sticky= W)
        par.append(StringVar())
        par[i].set(par_val[i][0])
        w = Entry(root,textvariable= par[i], bd =5,bg='PeachPuff',fg='DarkBlue')
        w.config(width = width)
        w.grid(row=k,column=n_col+1)

    if(len(par_val[i]) > 1):        # menu items with a set of values in the drop-down list
        Label(root, text= par_name[i],borderwidth=1 ).grid(row=k,column=n_col,sticky= W+E)
        par.append(StringVar())
        par[i].set(par_val[i][0])
        w = OptionMenu(root, par[i], *par_val[i])
        w.config(bg='yellow')
        w.grid(row=k,column=n_col+1,sticky= W+E)
    k = k + 1
    if(k - 1 >= km1):
        k = 0
        n_col = 2

dir_0 = os.getcwd()
dir =  par[0].get() 

f_contr = dir + '/' + 'control'



command =  par[1].get() + ' ' +  f_contr

Button(root,fg='navy', bg='coral',text='Run',command = lambda: run(dir_0,dir,command,comm_file,n_base)).grid(row=km1 + 2, columnspan=4,sticky= E+W)
#Button(root, fg='snow',bg='black', text='Show results',command = lambda: open_results()).grid(row=km1 + 3,columnspan=4,sticky= E+W)
Button(root, fg='navy',bg='lemon chiffon', text='Edit Command File',command = lambda: show_edit_txt_file(comm_file,width,height)).grid(row=km1 + 4,columnspan=4,sticky= E+W)
Button(root, fg='red',bg='snow3', text='Quit',command = root.destroy).grid(row=km1 + 5,columnspan=4,sticky= E+W)
Button(root, fg='white',bg='light blue', text='Help',command = lambda: show_edit_txt_file("help",100,30)).grid(row=km1 + 6,columnspan=4,sticky= E+W)
root.mainloop()

