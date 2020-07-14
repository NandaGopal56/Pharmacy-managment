import tkinter
from tkinter import *
import tkinter.messagebox
import random
import time
import datetime
import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',passwd='12345',database='pharmacy_managment_system')
mycursor=mydb.cursor()



#sql='create table user_details (username VARCHAR(40),password VARCHAR(20))'
#mycursor.execute(sql)


def main():
    root = Tk()
    app = window1(root)
    root.mainloop()

class window1:
    def __init__(self,master):
        self.master=master
        self.master.title('pharmacy manangment system')
        self.master.geometry('1300x700')
        self.frame=Frame(self.master)
        self.frame.pack()

        self.username=StringVar()
        self.password=StringVar()
 # ============================================================================================================================================#

        self.labletitle=Label(self.frame,text='Pharmacy Managmeny System ',font=('arial',50,'bold'),bd=20)
        self.labletitle.grid(row=0,column=0)

        self.loginframe1=Frame(self.frame,width=1010,height=100,bd=10,relief='ridge')
        self.loginframe1.grid(row=1,column=0)

        self.loginframe2=Frame(self.frame,width=1000,height=100,bd=20,relief='ridge')
        self.loginframe2.grid(row=2,column=0)

        self.loginframe3=Frame(self.frame,width=1000,height=200,bd=20,relief='ridge')
        self.loginframe3.grid(row=3,column=0,pady=2)

#============================================================================================================================================#
        self.lblusername=Label(self.loginframe1,text='username',font=('arial',50,'bold'),bd=20)
        self.lblusername.grid(row=0,column=0)
        self.lblusername = Entry(self.loginframe1, text='username', font=('arial', 50, 'bold'), bd=20,textvariable=self.username)
        self.lblusername.grid(row=0, column=1)

        self.lblpassword=Label(self.loginframe1,text='password',font=('arial',50,'bold'),bd=20)
        self.lblpassword.grid(row=1,column=0)
        self.lblpassword = Entry(self.loginframe1, text='password',show="*", font=('arial', 50, 'bold'), bd=20,textvariable=self.password)
        self.lblpassword.grid(row=1, column=1,padx=20)



# ============================================================================================================================================#

        self.btnlogin=Button(self.loginframe2,text='login',width=19,font=('arial',20,'bold'),command=self.login_system)
        self.btnlogin.grid(row=0,column=0)

        self.btnsignup = Button(self.loginframe2, text='Sign up',width=19,font=('arial',20,'bold'), command=self.sign_up_system)
        self.btnsignup.grid(row=0, column=1)

        self.btnreset = Button(self.loginframe2, text='Reset',width=19,font=('arial',20,'bold'), command=self.reset)
        self.btnreset.grid(row=0, column=2)

        self.btnexit = Button(self.loginframe2, text='exit', width=19, font=('arial', 20, 'bold'),command=self.iexit)
        self.btnexit.grid(row=0, column=3)

# ============================================================================================================================================#

        self.btnregistration=Button(self.loginframe3,state=DISABLED,text='patient registration system',command=self.registration_window)
        self.btnregistration.grid(row=0,column=0)

        self.btnhospital = Button(self.loginframe3,state=DISABLED,text='hospital manangment system', command=self.hospital_window)
        self.btnhospital.grid(row=0, column=1,pady=5,padx=5)

# ============================================================================================================================================#
    def login_system(self):
        user=(self.username.get())
        pas=(self.password.get())

        t=(user,str(pas))
        #print(t)

        sql="select * from user_details where username=%s and password=%s"
        mycursor.execute(sql,(user,pas,))
        record=mycursor.fetchall()
        #print(record)

        if t in record:
            print('login success')
            tkinter.messagebox.showinfo('pharmacy managment system','login successfull')
            self.btnregistration.config(state=NORMAL)
            self.btnhospital.config(state=NORMAL)

        else:
           print('login unsucess')
           tkinter.messagebox.showerror('pharmacy managment system', 'login unsuccessfull (wrong credentials)')
           self.btnregistration.config(state=DISABLED)
           self.btnhospital.config(state=DISABLED)
           self.username.set("")
           self.password.set("")


#============================================================================================================================================#
    def sign_up_system(self):
        user = (self.username.get())
        pas = (self.password.get())

        print(pas,type(pas))

        sql=('select username from user_details where username=%s')
        mycursor.execute(sql,(user,))

        record=mycursor.fetchall()
        print(record)
        old_user=len(record)
        if old_user!=0:
            print('username already exists')
            tkinter.messagebox.showerror('pharmacy managment system', 'username already exists')
            self.username.set("")
            self.password.set("")
        else:
            sql = ('insert into user_details(username,password)value(%s,%s)')
            val = (user, pas)
            mycursor.execute(sql, val)
            mydb.commit()
            self.btnregistration.config(state=DISABLED)
            self.btnhospital.config(state=DISABLED)
            print('registered successfully')
            tkinter.messagebox.showinfo('pharmacy managment system', 'user registration successfull')
            self.username.set("")
            self.password.set("")
# ============================================================================================================================================#

    def reset(self):
        self.btnregistration.config(state=DISABLED)
        self.btnhospital.config(state=DISABLED)
        self.username.set("")
        self.password.set("")

# ============================================================================================================================================#
    def iexit(self):
       x=tkinter.messagebox.askyesno('pharmacy managment system','do you want to exit ?')
       if x > 0:
           self.master.destroy()
           return

# ============================================================================================================================================#
    def registration_window(self):
        self.newwindow=Toplevel(self.master)
        self.app=window2(self.newwindow)

    def hospital_window(self):
        self.newwindow=Toplevel(self.master)
        self.app=window3(self.newwindow)
class window2:
    def __init__(self,master):
        self.master=master
        self.master.title('patient registration system')
        self.master.geometry('1300x700')
        self.frame=Frame(self.master)
        self.frame.pack()

class window3:
    def __init__(self,master):
        self.master=master
        self.master.title('hospital manangment system')
        self.master.geometry('1300x700')
        self.frame=Frame(self.master)
        self.frame.pack()

if __name__ == '__main__':
    main()