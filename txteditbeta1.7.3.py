from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
import os
import time
import re
def newfile():
                t.delete('1.0',END)
                windows.title('标题')
def openfile():
                global filename
                filename=askopenfilename()
                if filename=='':
                                return
                with open(filename,'r') as o:
                                c=o.read()
                t.delete('1.0',END)
                t.insert(END,c)
                windows.title(filename)
def saveas():
                global filename
                g=t.get('1.0',END)
                filename=asksaveasfilename()
                if filename=='':
                                return
                with open(filename,'w') as ou:
                                ou.write(g)
                                windows.title(filename)
def save():
                global filename
                g=t.get('1.0',END)
                if filename=='标题':
                                saveas()
                else:
                                with open(filename,'w') as o:
                                                o.write(g)
def cut():
    copy()
    t.delete(SEL_FIRST,SEL_LAST)
def copy():
    t.clipboard_clear()
    ct=t.get(SEL_FIRST,SEL_LAST)
    t.clipboard_append(ct)
def paste():
    ct=t.selection_get(selection='CLIPBOARO')
    t.insert(INSERT,ct)
def s(event):
    pop.post(event.x_root,event.y_root)
filename='标题'
windows=Tk()
windows.title(filename)
windows.geometry('1000x618')
m=Menu(windows)
f=Menu(m,tearoff=False)
m.add_cascade(label='文件',menu=f)
f.add_command(label='新文件',command=newfile)
f.add_command(label='打开文件',command=openfile)
f.add_command(label='保存',command=save)
f.add_command(label='另存为',command=saveas)
f.add_command(label='退出',command=windows.destroy)
windows.config(menu=m)
t=Text(windows)
t.pack(fill=BOTH,expand=True)
pop=Menu(windows,tearoff=False)
pop.add_command(label='剪贴',command=cut)
pop.add_command(label='复制',command=copy)
pop.add_command(label='粘贴',command=paste)
windows.bind('<Button-3>',s)
windows.mainloop()
