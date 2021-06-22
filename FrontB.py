from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from matplotlib import pyplot as plt

top = Tk()
top.geometry('1100x600')
top.title('EXPENSE TRACKER')
top.iconphoto(False, PhotoImage(file='icon1.1.png'))
top.resizable(0, 0)  
f1=Frame(top,height=230,width=1100)
f1.pack()
image = PhotoImage(file = "image.png")
img_label = Label(f1,image = image)
img_label.place(x = 0,y=0)
f2 = Frame(top,height = 370 , width =1100 , bg ='white')
f2.pack()

#using notebook for creating tabs
tc = ttk.Notebook(f2)
#tab1
t1=ttk.Frame(tc)
tc.add(t1,text='                     ADD INCOME                     ',padding = 20)
#tab2
t2=ttk.Frame(tc)
tc.add(t2,text='                     ADD EXPENSE                     ',padding = 20)
#tab3
t3=ttk.Frame(tc)
tc.add(t3,text='                    INCOME-EXPENSE CURVE                    ',padding = 20)
#tab4
t4=ttk.Frame(tc)
tc.add(t4,text='                     VIEW INCOME                      ',padding = 20)
#tab5
t5=ttk.Frame(tc)
tc.add(t5,text='                      VIEW EXPENSE                    ',padding = 20)

tc.pack(expand = 1,fill='both')

#tab1 content
def submit1():
    conn=sqlite3.connect("income.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS inc(ammount double , source text)")
    cur.execute("INSERT INTO inc Values(?,?)",(e1.get(),e2.get()))
    l=Label(t1,text="***Added Sucessfully***",font="times 15",fg='green')
    l.grid(row=6,column=3)
    conn.commit()
    conn.close()

    e1.delete(0,END)
    e2.delete(0,END)
    #e3.delete(0,END)
    
l1=Label(t1,text='Add Income',font=('verdana 20'),fg='blue')
l1.grid(row=1,column=2,columnspan=2,padx=420)
amm=Label(t1,text = "Amount:" , font=("calibri"))
amm.grid(row=3 , column=2)
s=Label(t1,text = "Source:",font="calibri")
s.grid(row=4,column=2)
#dt = Label(t1,text = "Date :",font = ("calibri"))
#dt.grid(row = 5 , column = 2)
btn1=Button(t1,text="Submit",width=15,fg='yellow',bg='black',command=submit1)
btn1.grid(row=5,column=3)
e1=ttk.Entry(t1)
e1.place(x=350,y=45,width=250)
e2=ttk.Entry(t1)
e2.place(x=350,y=70,width=250)
#e3 = ttk.Entry(t1)
#e3.place(x = 350,y=98,width=250)

#tab2 content
def submit2():
    conn=sqlite3.connect("expense.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS exp(amount double , source text)")
    cur.execute("INSERT INTO exp Values(?,?)",(e3.get(),e4.get()))
    lx=Label(t2,text="***Added Sucessfully***",font="times 15",fg="red")
    lx.grid(row=6 , column=3)
    conn.commit()
    conn.close()

    e3.delete(0,END)
    e4.delete(0,END)

l2=Label(t2,text='Add Expense',font=('verdana 20'),fg='blue')
l2.grid(row=1,column=2,columnspan=2,padx=420)
amm2=Label(t2,text = "Amount:" , font=("calibri"))
amm2.grid(row=3 , column=2)
s1=Label(t2,text = "Source:",font="calibri")
s1.grid(row=4,column=2)
btn2=Button(t2,text="Submit",width=15,fg='yellow',bg='black',command=submit2)
btn2.grid(row=5,column=2)
e3=ttk.Entry(t2)
e3.place(x=350,y=45,width=250)
e4=ttk.Entry(t2)
e4.place(x=350,y=70,width=250)
#tab3 content
def graph():
    con = sqlite3.connect("income.db")
    c = con.cursor()
    c.execute("SELECT amm FROM inc")
    ammount = c.fetchall()
    con.commit()
    c.execute("SELECT source FROM inc")
    source = c.fetchall()
    con.commit()

    s = []
    a = []
    for row in source :
        s.append(row[0])
    for i in ammount :
        a.append(i[0])
    con.close()

    conn = sqlite3.connect("expense.db")
    cur = conn.cursor()
    cur.execute("SELECT amount FROM exp")
    ammount1 = cur.fetchall()
    conn.commit()
    cur.execute("SELECT source FROM exp")
    source1 = cur.fetchall()
    conn.commit()

    s1 = []
    a1= []
    for row in source1 :
        s1.append(row[0])
    for i in ammount1 :
        a1.append(i[0])
    conn.close()

    plt.plot(s1,a1,color= 'red',label = 'Expense')
    plt.plot(s,a,color= 'green',label = 'Income')
    plt.title('Income Expense Curve')
    plt.ylabel('Ammount ')
    plt.xlabel('Source ')
    plt.legend()
    
    plt.show()

btn3=Button(t3,text="Click here",width=30,fg='yellow',bg='black',height = 5,command=graph)
btn3.grid(row=5,column=2)

#tab4 content
def inc() :
    con = sqlite3.connect("income.db")
    c = con.cursor()
    c.execute("SELECT *  FROM inc")
    record = c.fetchall()
    print_record = ' '
    for row in record :
        print_record += str(row[0]) + " \t" +" \t"+ str(row[1]) + "\n"
    li1 = Label(t4,text = 'Ammount / Source',font=('verdana 10'),fg='green')
    li1.grid(row=1,column = 3)
    li = Label(t4,text = print_record,font=('verdana 10'),padx = 250)
    li.grid(row = 3, column = 3)
    
    con.commit()
    con.close()
btn4 = Button(t4,text = "Display Record",width = 30,height = 5,bg = "black",fg = 'yellow',command = inc)
btn4.grid(row=5,column=2)

#tab5 content

def exp() :
    con = sqlite3.connect("expense.db")
    c = con.cursor()
    c.execute("SELECT *  FROM exp")
    record = c.fetchall()
    print_record = ' '
    for row in record :
        print_record += str(row[0]) + " \t" +" \t"+ str(row[1]) + "\n"
    li1 = Label(t5,text = 'Ammount / Source',font=('verdana 10'),fg='green')
    li1.grid(row=1,column = 3)
    li = Label(t5,text = print_record,font=('verdana 10'),padx = 250)
    li.grid(row = 3, column = 3)
    
    con.commit()
    con.close()
btn5 = Button(t5,text = "Display Record",width = 30,height = 5,bg = "black",fg = 'yellow',command = exp)
btn5.grid(row=5,column=2)

top.mainloop()
