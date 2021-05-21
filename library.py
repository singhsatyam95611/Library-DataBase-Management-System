from tkinter import*
from tkinter import ttk, messagebox
import mysql.connector as connector
from PIL import ImageTk

con= connector.connect(host="localhost",port="3306",user="root",password="satyam@1234",database="library")
cur=con.cursor()

root = Tk()

root.title("Library DataBase Management System")
root.geometry("730x530")
root.configure(bg="black")
""" title = Label(text="LIBRARY MANAGEMENT SYSTEM",fg="white",bg="green",
font=("Bahnschrift SemiBold","19"),padx="5",pady="5",relief=SUNKEN,bd=4)
title.pack() """

can = Canvas(root,width=730,height=530,bg="white")
can.pack(expand=YES,fill=BOTH) 
path = PhotoImage(file='C:\\Users\\Satyam Singh\\OneDrive\\Desktop\\Python\\lib.png')
can.create_image(0,0,anchor=NW,image=path)




def showbooks():
    new=Toplevel(root)
    new.title("Library DataBase Management System")
    new.geometry("700x400")
    title2 = Label(new,text="DATABASE",fg="white",bg="green",
font=("Bahnschrift SemiBold","19"),padx="5",pady="7",relief=SUNKEN)
    title2.place(x=325,y=15)
    title2.pack()

    cols=("Book No","Books","Amount")
    lis = ttk.Treeview(new,height=15,column =cols,show="headings")

    lis.column('Book No',width=20,anchor=CENTER)
    lis.column('Books',width=400,anchor=CENTER)
    lis.column('Amount',width=40,anchor=CENTER)

    lis.heading('Book No',text='Book No ')
    lis.heading('Books',text='Books')
    lis.heading('Amount',text='Amount')

    try:
        query="SELECT * FROM books"
        cur.execute(query)
        row = cur.fetchall()
        for i in row:
            lis.insert('','end',values = i)
        
    except Exception as e:
        print(e)
        con.close()

    lis.pack(side=BOTTOM,fill=BOTH)

def deletebook():
    try:
        a= dele.get()
        cur.execute("delete from books where srno = {}".format(a))
        con.commit()
        messagebox.showinfo("Information ","Book Deleted Sucesfulluy...")
        dele.delete(0,END)
    except Exception as e:
        print(e)

def insertbook():
    try:
        a=sr.get()
        b=na.get()
        c=am.get()
        query="INSERT INTO books(srno,Name,amount) VALUES (%s,%s,%s)"
        val=(a,b,c)
        cur.execute(query,val)
        con.commit()
        messagebox.showinfo("Information ","Book Inserted Sucessfully....")
        sr.delete(0,END)
        na.delete(0,END)
        am.delete(0,END)
       
    except Exception as e:
        print(e)

def updatebooks():
    try:
        a=sru.get()
        b=nau.get()
        c=amu.get()
        querry="update books set Name='{}',amount='{}' where srno={}".format(b,c,a)
        cur.execute(querry)
        con.commit()
        messagebox.showinfo('Information','Updated Sucessfully...')
        sru.delete(0,END)
        nau.delete(0,END)
        amu.delete(0,END)

    except Exception as e:
        print(e)        


insert_data = Label(text="INSERT BOOK :",font=("Arial Black","12"),fg="white",bg="dark blue")
insert_data.place(x=20,y=65)

srno = Label(text="Book No        :",font=("Arial Black","10"))
srno.place(x=25,y=115)

name = Label(text="Book Name  :",font=("Arial Black","10"))
name.place(x=25,y=160)

amo = Label(text="Amount         :",font=("Arial Black","10"))
amo.place(x=25,y=205)

sr=Entry(width=25)
sr.place(x=160,y=115)

na=Entry(width=25)
na.place(x=160,y=160)

am=Entry(width=25)
am.place(x=160,y=205)

insert =Button(text="Insert Book",font=("Arial Black","11"),fg='white',bg="orange",relief=RAISED,command=insertbook)
insert.place(x=95,y=245)



delete_data = Label(text="DELETE BOOK :",font=("Arial Black","12"),fg="white",bg="dark blue")
delete_data.place(x=20,y=320)

name1 = Label(text="Book No      :",font=("Arial Black","10"))
name1.place(x=25,y=370)

dele=Entry(width=25)
dele.place(x=160,y=370)

delete =Button(text="Delete Book",font=("Arial Black","11"),fg='white',bg="orange",relief=RAISED,command = deletebook)
delete.place(x=95,y=410)



show = Label(text="Database :",font=("Arial Black","12"),fg="white",bg="dark blue")
show.place(x=375,y=330)

titl2 = Label(text="***Click below to get all records of students***",font=("Arial Black","9"),fg="white",bg="green")
titl2.place(x=380,y=370)

show =Button(text="Show All Books",font=("Arial Black","12"),fg='white',bg="orange",relief=RAISED,command=showbooks)
show.place(x=440,y=405)



update_data = Label(text="Update Into Records :",font=("Arial Black","12"),fg="white",bg="dark blue")
update_data.place(x=375,y=65)

srnou = Label(text="Book No                   :",font=("Arial Black","10"))
srnou.place(x=380,y=115)

nameu = Label(text="New Book's Name  :",font=("Arial Black","10"))
nameu.place(x=380,y=160)

amou = Label(text="Updated Amount    :",font=("Arial Black","10"))
amou.place(x=380,y=205)

sru=Entry(width=25)
sru.place(x=540,y=115)

nau=Entry(width=25)
nau.place(x=540,y=160)

amu=Entry(width=25)
amu.place(x=540,y=205)

update =Button(text="Update Book",font=("Arial Black","11"),relief=RAISED,fg='white',bg="orange",command = updatebooks)
update.place(x=450,y=245)



root.mainloop()