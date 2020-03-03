from datetime import datetime
import pymysql.cursors
from tkinter import *

root=Tk()
root.geometry('500x500')
root.title("Date entry")


id=IntVar()
dd=StringVar()
mm=StringVar()
yy=StringVar()

def database():
    db=pymysql.connect("localhost","root","root","test")
    cursor=db.cursor()
    id1 = id.get()
    dd1=dd.get()
    mm1=mm.get()
    yy1=yy.get()
    now=datetime(int(yy1),int(mm1),int(dd1))
    print(now)

    cursor.execute('insert into table3(id, dt) values(%s,%s)', (id1, now))
    print("inserted")
    db.commit()



Label_0 = Label(root,text="Date details",width=30,font=("bold",20))
Label_0.place(x=90,y=53)

Label_5=Label(root,text="id", width=20,font=("bold",10))
Label_5.place(x=60,y=100)

entry_5=Entry(root,textvar=id)
entry_5.place(x=200,y=100)

Label_1=Label(root,text="dd",width=20,font=("bold",10))
Label_1.place(x=60,y=130)

entry_1=Entry(root,textvar=dd)
entry_1.place(x=200,y=130)

Label_2=Label(root,text="mm",width=20,font=("bold",10))
Label_2.place(x=60,y=180)

entry_2=Entry(root,textvar=mm)
entry_2.place(x=200,y=180)

Label_3=Label(root,text="yy",width=20,font=("bold",10))
Label_3.place(x=60,y=210)

entry_3=Entry(root,textvar=yy)
entry_3.place(x=200,y=210)

find_dt=Button(root,text="Find Date",width=20,bg='brown',fg='white')
find_dt.configure(command=database)
find_dt.place(x=140,y=280)
