from tkinter import *
from tkinter import ttk,font,messagebox
from PIL import ImageTk,Image
import pymysql as mysql
import re
win=Tk()
win.attributes("-fullscreen",True)
f1=Frame(win,width=1500,height=60,bg="Orchid")
f1.pack()
label_font=font.Font(weight="bold",family="Times New Roman",size=25)
l=Label(f1,text="Student Registration",font=label_font,bg="Orchid")
l.place(relx=0.4,rely=0.004)

def exit():
    answer=messagebox.askquestion("exit","Do you want to exit the application?")
    if(answer=="yes"):
        win.destroy()

ext=Button(f1,text="Exit",font=label_font,bg="Orchid",command=lambda:exit())
ext.place(relx=0.94,rely=0.004)
img=ImageTk.PhotoImage(Image.open('studentregistration image.jpg'))
canvas=Canvas(win)
canvas.create_image(380,350,image=img)
canvas.pack(fill="both",expand=True)
label_font=font.Font(weight="bold",family="Helvetica",size=18)
canvas.create_text(95,145,text="Name",fill="Black",font=label_font)
name=Entry(win)
name.place(relx=0.13,rely=0.25,width=200,height=30)
canvas.create_text(95,205,text="DOB",fill="Black",font=label_font)
dob=Entry(win)
dob.place(relx=0.13,rely=0.33,width=200,height=30)
canvas.create_text(95,256,text="Gender",fill="Black",font=label_font)
var=IntVar()
g1=Radiobutton(win,text="Male",variable=var,value=1)
g1.place(relx=0.13,rely=0.4)
g2=Radiobutton(win,text="Female",variable=var,value=2)
g2.place(relx=0.18,rely=0.4)
g3=Radiobutton(win,text="Others",variable=var,value=3)
g3.place(relx=0.23,rely=0.4)
canvas.create_text(95,325,text="Email_ID",fill="Black",font=label_font)
email=Entry(win)
email.place(relx=0.13,rely=0.48,width=200,height=30)
canvas.create_text(460,145,text="Contact",fill="Black",font=label_font)
contact=Entry(win)
contact.place(relx=0.42,rely=0.25,width=200,height=30)
canvas.create_text(460,200,text="Course",fill="Black",font=label_font)
course=ttk.Combobox(win,values=["Python","Machine Learning","Artificial Intelligence","DataScience","Fullstack Development","Ms-Office","Tally Prime","Advanced Excel","Java","Statistics","Software Testing","Blockchain Technology","C Programming","C++ Programming","Asp.net","Django","Robotics"])
course.place(relx=0.42,rely=0.33,width=200,height=30)
course.set("select the course")
canvas.create_text(470,263,text="Qualification",fill="Black",font=label_font)
qualification=Entry(win)
qualification.place(relx=0.42,rely=0.4,width=200,height=30)
canvas.create_text(460,330,text="Address",fill="Black",font=label_font)
address=Text(win)
address.place(relx=0.42,rely=0.48,width=250,height=100)

def insert():
    Pattern = re.compile("[6-9][0-9]{9}")
    regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if(name.get()=="" or dob.get()=="" or  email.get()=="" or contact.get()=="" or course.get()=="" or qualification.get()==""):
        messagebox.showerror("student registration","Please Fill all the field")
    elif(not(re.fullmatch(regex,email.get()))):
        messagebox.showerror("student registration","Invalid email_id")
    elif(not(Pattern.match(contact.get()))):
        messagebox.showerror("student registration","Invalid contact")
    else:
        connection=mysql.connect(host="localhost",user="root",password="subhani",database="studentregistration")
        cursor=connection.cursor()
        if(var.get()==1):
            gender="Male"
        if(var.get()==2):
            gender="Female"
        else:
            gender="other"
    
        s="insert studentregistrationtable(name,dob,gender,email,contact,course,qualification,address) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        t=(name.get(),dob.get(),gender,email.get(),contact.get(),course.get(),qualification.get(),address.get(1.0,END))
        cursor.execute(s,t)
        connection.commit()
        messagebox.showinfo("student registration","Insert Successfully")
        name.delete(0,END);dob.delete(0,END);email.delete(0,END);contact.delete(0,END);course.delete(0,END);qualification.delete(0,END);address.delete(1.0,END)

def update():
    connection=mysql.connect(host="localhost",user="root",password="subhani",database="studentregistration")
    cursor=connection.cursor()

    if(var.get()==1):
        gender="Male"
    elif(var.get()==2):
        gender="Female"
    else:
        gender="other"
        
    sql="update studentregistrationtable set name='"+str(name.get())+"',dob='"+str(dob.get())+"',gender='"+gender+"',email='"+str(email.get())+"',contact='"+str(contact.get())+"',course='"+str(course.get())+"',qualification='"+str(qualification.get())+"',address='"+str(address.get("1.0",END))+"'where name='"+name.get()+"'"
    cursor.execute(sql)
    connection.commit() 
    messagebox.showinfo("student registration","Update Successfully")
    name.delete(0,END);dob.delete(0,END);email.delete(0,END);contact.delete(0,END);course.delete(0,END);qualification.delete(0,END);address.delete(1.0,END)

def delete():
    connection=mysql.connect(host="localhost",user="root",password="subhani",database="studentregistration")
    cursor=connection.cursor()
    sql="delete from studentregistrationtable where name='"+name.get()+"'"
    cursor.execute(sql)
    connection.commit()
    messagebox.showinfo("student registration","Delete Successfully")
    name.delete(0,END);dob.delete(0,END);email.delete(0,END);contact.delete(0,END);course.delete(0,END);qualification.delete(0,END);address.delete(1.0,END)

label_font=font.Font(weight="bold",family="Times New Roman",size=15)
b=Button(win,text="Insert",font=label_font,command=lambda:insert(),bg="limegreen")
b.place(relx=0.42,rely=0.65)
b1=Button(win,text="Update",font=label_font,command=lambda:update(),bg="limegreen")
b1.place(relx=0.48,rely=0.65)
b2=Button(win,text="Delete",font=label_font,command=lambda:delete(),bg="limegreen")
b2.place(relx=0.55,rely=0.65)
frame=Frame(win,width=1500,height=60,bg="orchid")
frame.place(relx=0,rely=0.93)
label_font=font.Font(weight="bold",family="Times New Roman",size=25)
frame1=Label(win,text="--Copyrights @ 2024--",font=label_font,bg="orchid")
frame1.place(relx=0.4,rely=0.93)
win.mainloop()