import tkinter
mybox=tkinter.Tk()
mybox.geometry('400x200')
mybox.title("This is window")
myb1=tkinter.Button(mybox,text="Button 1",bg='purple',fg='yellow').pack(side="left")
myb2=tkinter.Button(mybox,text="Button 2",bg='pink',fg='black').pack(side="top")
myb3=tkinter.Button(mybox,text="Button 3",bg='cyan',fg='black').pack(side="right")
myb4=tkinter.Button(mybox,text="Button 4",bg='red',fg='black').pack(side="bottom")
tkinter.mainloop()

from tkinter import*
myw=Tk()
myw.geometry('300x200')
Label(myw,text="User id").grid(row=0)
Label(myw,text="Password").grid(row=1)
t1=Entry(myw)
t2=Entry(myw)
t1.grid(row=0,column=1)
t2.grid(row=1,column=1)
mainloop()


import tkinter
from tkinter import messagebox
root=tkinter.Tk()
root.withdraw()
messagebox.showerror("error", "Error message")
messagebox.showwarning("warning", "Warning message")
messagebox.showinfo("information", "Information message")
