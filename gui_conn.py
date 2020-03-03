from tkinter import *
from tkinter import ttk
import pymysql.cursors
import datetime as dt

root=Tk()
root.geometry('500x500')
root.title("Registration form")

Fullname=StringVar()
Email=StringVar()
g=IntVar()
c=StringVar()
#var1= IntVar()

def database():
    db=pymysql.connect("localhost","root","root","test")
    cursor=db.cursor()
    name1=Fullname.get()
    email=Email.get()
    gender1=g.get()
    course1=c.get()
    with db:
        cursor=db.cursor()
        sql=('CREATE TABLE IF NOT EXISTS Student6(Fullname char(10),Email char(10),gender char(2),course char(100))')
        cursor.execute(sql)
        print("Table created")
        sql1=("INSERT INTO Student6 VALUES(\"%s\",\"%s\",\"%s\",\"%s\")" %(str(name1),str(email),str(gender1), str(course1)))
        cursor.execute(sql1)
        print("inserted")
        db.commit()
    
Label_0 = Label(root,text="Registration form for Course",width=30,font=("bold",20))
Label_0.place(x=90,y=53)

Label_1=Label(root,text="Full Name",width=20,font=("bold",10))
Label_1.place(x=80,y=130)

entry_1=Entry(root,textvar=Fullname)
entry_1.place(x=240,y=130)

Label_2=Label(root,text="Email",width=20,font=("bold",10))
Label_2.place(x=68,y=180)

entry_2=Entry(root,textvar=Email)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

Radiobutton(root, text="Male",padx = 5, variable=g, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=g, value=2).place(x=290,y=230)

label_4 = Label(root, text="Course",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

list1 = ['Data Science','DataLakes','Software Testing','Augmented Reality','Python Programming','BigData-Hadoop'];

#following is working fine!

droplist=OptionMenu(root,c,*list1)
droplist.config(width=15)
c.set('select your course') 
droplist.place(x=240,y=280)

date = dt.datetime.now()

w = Label(root, text=f"{dt.datetime.now():%a, %b %d %Y}", fg="white", bg="black", font=("helvetica", 13)).place(x=400,y=230)

#label4 = Label(root,text = "Choose your favourite course")
#label4.place(x=70,y=280)

#comboExample = ttk.Combobox(root,
#                            values=[
#                                    "Data Science", 
#                                    "DataLakes",
#                                    "Python programming",
#                                    "Augmented Reality"])
#print(dict(comboExample))
#c.set('select your course') 
#comboExample.place(x=240,y=280)
#comboExample.current(1)
#print(comboExample.current(), comboExample.get())


Button(root, text="Submit",width=20,bg='brown',fg='white',command=database).place(x=180,y=380)
root.mainloop()

