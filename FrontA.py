from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import os

root = Tk()
root.geometry('1100x600')
root.title('EXPENSE TRACKER')
root.iconphoto(False, PhotoImage(file='icon1.1.png'))
root.resizable(0, 0)         # Disable resizing the GUI
frame1 = Frame(root ,height = 270 , width = 1100)
frame1.pack()
frame2 = Frame(root ,height = 330 , width = 1100,bg = 'white')
frame2.pack()
image = PhotoImage(file = "image.png")
img_label = Label(frame1 , image = image)
img_label.place(x=0 , y=0)

#using notebook for creating tabs
tabControl=ttk.Notebook(frame2)  
#Tab1  
tab1=ttk.Frame(tabControl)  
tabControl.add(tab1, text='                                                       HOME                                           ',padding = 20)
#Tab2
tab2=ttk.Frame(tabControl)  
tabControl.add(tab2, text = '                                                      LOGIN                                       ', padding = 20 )    
#Tab 3
tab3=ttk.Frame(tabControl)  
tabControl.add(tab3, text='                                                        REGISTRATION                                          ',padding = 20,)
tabControl.pack(expand=1, fill="both")

#content in tab1
l3=Label(tab1,text = "WELCOME!!!!",font=("Verdana",72),fg='DarkGoldenRod2',bg='LightSkyBlue1').place(x=200,y=40)
tabControl.select(tab2)

#content in tab2
def login():
    conn=sqlite3.connect("register1.db")
    c=conn.cursor()
    c.execute('SELECT * FROM entry WHERE email = ? AND password = ?', (mail1.get(),pass2.get()))
    a=c.fetchall()
    conn.commit()
    conn.close()
    if len(a)==0:
        messagebox.showwarning("warning","PLEASE DO REGISTRATION!!!")
    else:
        root.destroy()
        os.system('FrontB.py')

l1=Label(tab2,text = "Login" , font=("verdana 20"),fg='blue')
l1.grid(row=1 , column=2,columnspan=2,padx=420)
mail=Label(tab2,text = "Email:" , font=("calibri"))
mail.grid(row=3 , column=2,padx=100)
pass1=Label(tab2,text = "Password:",font="calibri")
pass1.grid(row=4,column=2,padx=100)

mail1=ttk.Entry(tab2)
mail1.place(x=400,y=45,width=250)
pass2=ttk.Entry(tab2,show="*")
pass2.place(x=400,y=70,width=250)
btn2=ttk.Button(tab2,text="Login",width=20,command = login)
btn2.place(x=400,y=100)

#content in tab3
def submit():
    conn=sqlite3.connect("register1.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS entry(f_name text , l_name text , m_name text , email text , password text , city text)")
    cur.execute("INSERT INTO entry Values(?,?,?,?,?,?)",(e1.get(),e2.get(),e3.get(),e4.get() , e5.get() , e6.get()))
    l4=Label(tab3,text="account created",font="times 15")
    l4.place(x=550 , y=200)
    conn.commit()
    conn.close()
    
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)

e1=Entry(tab3)
e1.place(x=400,y=45,width=250)
e2=Entry(tab3)
e2.place(x=400,y=70,width=250)
e3=Entry(tab3)
e3.place(x=400,y=100,width=250)
e4=Entry(tab3)
e4.place(x=400,y=130,width=250)
e5=Entry(tab3,show="*")
e5.place(x=400,y=160,width=250)
e6=Entry(tab3)
e6.place(x=400,y=190,width=250)

l1=Label(tab3,text = "Register" , font=("verdana 20"),fg='blue')
l1.grid(row=1 , column=2,columnspan=2,padx=420)
f_name=Label(tab3,text = "First Name:" , font=("calibri"))
f_name.grid(row=3 , column=2,padx=100)
l_name=Label(tab3,text = "Last Name:" , font=("calibri"))
l_name.grid(row=4 , column=2,padx=100)
m_name=Label(tab3,text = "Middle Name:" , font=("calibri"))
m_name.grid(row=5 , column=2,padx=100)
email=Label(tab3,text = "Email:",font='calibri')
email.grid(row=6,column=2,padx=100)
password=Label(tab3,text = "Password:",font="calibri")
password.grid(row=7,column=2,padx=100)
city=Label(tab3,text="City:",font="calibri")
city.grid(row=8,column=2,padx=100)
btn1=ttk.Button(tab3,text="Sign Up",width=20,command=submit)
btn1.grid(row=9,column=2)

root.mainloop()
