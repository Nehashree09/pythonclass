from tkinter import*
myw=Tk()
myw.geometry('200x200')
myw.configure(bg='purple')
myw.title("listbox example")
myl=Listbox(myw)
myl.grid(row=0)
myl.insert(0,'Hello')
myl.insert(1,'안녕')
myl.insert(2,'こんにちは')
myl.insert(3,'สวัสดี')
myl.insert(END,'你好')
Label(myw,text="enter index to be deleted").grid(row=0,column=1)
e1=Entry(myw,width=5)
e1.grid(row=0,column=2)
def mydel():
    myl.delete(int(e1.get()))
Button(myw,text="Delete",command=mydel).grid(row=1,column=1)
mainloop()


#radiobutton
from tkinter import*
myww=Tk()
myww.geometry('300x200')
myww.configure(bg='purple')
myww.title("radiobutton widget using thinter")
myvar=IntVar()
myll=Label(myww,width=18)
myll.grid(row=0)
def myf():
    myll.configure(text="you have selected "+str(myvar.get()))
rb1=Radiobutton(myww,text="male",variable=myvar,value=0,width=15,anchor='w',command=myf)
rb1.grid(row=1)
rb2=Radiobutton(myww,text="female",variable=myvar,value=1,width=15,anchor='w',command=myf)
rb2.grid(row=2)
rb2.select()
mainloop()