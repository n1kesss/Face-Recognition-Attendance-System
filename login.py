from tkinter import*
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System
import webbrowser


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("810x770+550+80")

        self.bg=ImageTk.PhotoImage(file=r"D:\PROJECTS\Face Recognition Attendance System\images\bglogin.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="#007ACC")
        frame.place(x=200,y=150,width=400,height=500)

        img1=Image.open(r"D:\PROJECTS\Face Recognition Attendance System\images\loginIcon.png")
        img1=img1.resize((95,95),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="#007ACC",borderwidth=0)
        lblimg1.place(x=350,y=175,width=100,height=100)

        get_str=Label(frame,text="Login",font=("Comfortaa Light",18,"bold"),fg="black",bg="#007ACC")
        get_str.place(x=163,y=120)

        #===========lables username ===============

        username=Label(frame,text="Name:",font=("Comfortaa Light",14,""),fg="black",bg="#007ACC")
        username.place(x=80,y=160)
        #entry1 
        self.txtuser=ttk.Entry(frame,font=("Comfortaa Light",15))
        self.txtuser.place(x=60,y=190,width=270)

#==========================password======================
        password=Label(frame,text="Password:",font=("Comfortaa Light",14,""),fg="black",bg="#007ACC")
        password.place(x=80,y=230)

        
        self.txtpass=ttk.Entry(frame,font=("Comfortaa Light",15),show="•")
        self.txtpass.place(x=60,y=260,width=270)

        #---------------icon img username-------------

        img2=Image.open(r"D:\PROJECTS\Face Recognition Attendance System\images\userID1.png")
        img2=img2.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="#007ACC",borderwidth=0)
        lblimg1.place(x=256,y=315,width=25,height=25)

        #---------------icon img password -----------------

        img3=Image.open(r"D:\PROJECTS\Face Recognition Attendance System\images\lockuser1.png")
        img3=img3.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="#007ACC",borderwidth=0)
        lblimg1.place(x=256,y=385,width=25,height=25)

        #==============================buttons====================================

        loginbtn=Button(frame,command=self.login,text="Login",font=("Comfortaa Light",15,"bold"),bd=2,relief=RIDGE,fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=60,y=320,width=270,height=35)
        
        loginbtn=Button(frame,text="Register",command=self.register_window,font=("Comfortaa Light",15,"bold"),bd=2,relief=RIDGE,fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=60,y=370,width=270,height=35)

        loginbtn=Button(frame,text="Forget Password ?",command=self.forgot_password_window,font=("times new roman",12,"italic","bold"),bd=0,relief=RIDGE,fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=260,y=465,width=130,height=35)
#========================================================================================


    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if (self.txtuser.get()=="" or self.txtpass.get()==""):
            messagebox.showerror("Error","All fields are required.")
        else:
            conn = mysql.connector.connect(username='sqluser', password='password',host='localhost',database='mydata',port=3306)
            mycursor = conn.cursor()
            mycursor.execute("select * from register where email=%s and password=%s",(
                self.txtuser.get(),
                self.txtpass.get()
            ))

            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!")
            else:
                open_main=messagebox.askyesno("Alert","This system is only for authorized person please do not proceed without permission!")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

#=================================forgot pass functions==============================

    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the Security Question!",parent=self.root2)
        elif(self.txt_security.get()==""):
            messagebox.showerror("Error","Please Enter the Answer!",parent=self.root2)
        elif(self.txt_newpass.get()==""):
            messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
        else:
            conn = mysql.connector.connect(username='sqluser', password='password',host='localhost',database='mydata',port=3306)
            mycursor = conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Question and Answer!",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                mycursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Successfully Your password has been rest, Please login with new Password!",parent=self.root2)
                self.root2.destroy()

#=================================forgot password window===========================

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter email to reset")
        else:
            conn = mysql.connector.connect(username='sqluser', password='password',host='localhost',database='mydata',port=3306)
            mycursor = conn.cursor()
            query=("select *  from register where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please Enter the Valid Email ID!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("400x500+750+230")   


                loginlbl_lbl=Label(self.root2,text="Forgot Password",font=("times new roman",25,"bold"),fg="#002B53",bg="#F2F2F2")
                loginlbl_lbl.place(x=80,y=20)

                #label1 
                security_Q=Label(self.root2,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                security_Q.place(x=80,y=80)

                #Combo Box1
                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
                self.combo_security_Q.current(0)
                self.combo_security_Q.place(x=80,y=110,width=270)


                #label2 
                security_A=Label(self.root2,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                security_A.place(x=80,y=150)

                #entry2 
                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=80,y=180,width=270)


                #label 2-1
                new_password=Label(self.root2,text="Choose new password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                new_password.place(x=80,y=220)

                #entry 2-2 
                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=80,y=250,width=270)

                btn=Button(self.root2,text="Reset Password",command=self.reset_pass,font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
                btn.place(x=80,y=350,width=280,height=35)




#============================================register window=============================

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1200x770+400+80")

        #variables===============

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"D:\PROJECTS\Face Recognition Attendance System\images\bglogin.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relheight=1,relwidth=1)





        #===========main frame-------------------------

        frame=Frame(self.root,bg="#F2F2F2")
        frame.place(x=150,y=100,width=900,height=580)

        register_lbl=Label(frame,text="Registration",font=("Comfortaa Light",25,"bold"),fg="#002B53",bg="#F2F2F2")
        register_lbl.place(x=345,y=25)


        #======================lables / entrys / check boxes======================


        #first name
        fname=Label(frame,text="First Name:",font=("Comfortaa Light",15,"bold"),fg="#002B53",bg="#F2F2F2")
        fname.place(x=100,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("Comfortaa Light",15,""))
        fname_entry.place(x=103,y=125,width=270)

        #last name
        lname=Label(frame,text="Last Name:",font=("Comfortaa Light",15,"bold"),fg="#002B53",bg="#F2F2F2")
        lname.place(x=100,y=170)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("Comfortaa Light",15,""))
        self.txt_lname.place(x=103,y=195,width=270)


        #contact
        contact=Label(frame,text="Contact No:",font=("Comfortaa Light",15,"bold"),fg="#002B53",bg="#F2F2F2")
        contact.place(x=530,y=100)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("Comfortaa Light",15,""))
        self.txt_contact.place(x=533,y=125,width=270)


        #email
        email=Label(frame,text="Email:",font=("Comfortaa Light",15,"bold"),fg="#002B53",bg="#F2F2F2")
        email.place(x=530,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("Comfortaa Light",15,""))
        self.txt_email.place(x=533,y=195,width=270)


        #security question
        security_Q=Label(frame,text="Select Security Question:",font=("Comfortaa Light",15,"bold"),fg="#002B53",bg="#F2F2F2")
        security_Q.place(x=100,y=240)

        #Combo Box
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("Comfortaa Light",15,""),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
        self.combo_security_Q.current(0)
        self.combo_security_Q.place(x=103,y=265,width=270)


        #security answer
        security_A=Label(frame,text="Security Answer:",font=("Comfortaa Light",15,""),fg="#002B53",bg="#F2F2F2")
        security_A.place(x=100,y=325)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("Comfortaa Light",15,""))
        self.txt_security.place(x=103,y=350,width=270)

        # ========================= Section 4-----Column 2=============================

        #password
        pswd=Label(frame,text="Password:",font=("Comfortaa Light",15,"bold"),fg="#002B53",bg="#F2F2F2")
        pswd.place(x=530,y=240)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("Comfortaa Light",15,""))
        self.txt_pswd.place(x=533,y=265,width=270)


        #confirm password
        confirm_pswd=Label(frame,text="Confirm Password:",font=("Comfortaa Light",15,"bold"),fg="#002B53",bg="#F2F2F2")
        confirm_pswd.place(x=530,y=325)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("Comfortaa Light",15,""))
        self.txt_confirm_pswd.place(x=533,y=350,width=270)

        #==================check====================

        #check terms and conditions
        self.var_check=IntVar()
        checkbtn = Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("Comfortaa Light",13,"bold"),fg="#002B53",bg="#F2F2F2")
        checkbtn.place(x=100,y=480,width=270)




#================================button===============================

        #Button Register

        loginbtn=Button(frame,text="Register",command=self.register_data,font=("Comfortaa Light",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=103,y=510,width=270,height=35)

        #Button  back to Login

        loginbtn1=Button(frame,text="Back to Login",command=self.return_login,font=("Comfortaa Light",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
        loginbtn1.place(x=533,y=510,width=270,height=35)

#+_+_+_+_+_+_+_+_+_+_+_++_+_++_+_

        terms_cond=Button(frame,text="See terms and conditions",command=self.termsandcond,font=("Comfortaa Light",12,""),bd=0,relief=RIDGE,fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
        terms_cond.place(x=533,y=450,width=270,height=35)
        
    def return_login(self):
        self.root.destroy() #to destroy window




#=========================functions===================

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
                messagebox.showerror("Error","All fields are required",parent=self.root)
        elif(self.var_pass.get() != self.var_confpass.get()):
                messagebox.showerror("Error","Password and confirm password must be same !",parent=self.root)
        elif(self.var_check.get()==0):
                messagebox.showerror("Error","Please Check the Agree Terms and Conditons!",parent=self.root)
        else:
            
                conn = mysql.connector.connect(username='sqluser', password='password',host='localhost',database='mydata',port=3306)
                mycursor = conn.cursor()
                query=("select * from register where email=%s")
                value=(self.var_email.get(),)
                mycursor.execute(query,value)
                row=mycursor.fetchone()
                
                if row!=None:
                        messagebox.showerror("Error","User already exist,please try another email",parent=self.root)
                
                else:
                        mycursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_securityQ.get(),
                        self.var_securityA.get(),
                        self.var_pass.get()
                                                ))
                        messagebox.showinfo("Success","Successfully Registerd!",parent=self.root)
                
                conn.commit()
                conn.close()
                



#=========================================terms and condition rakhna xa vane site banaune ane tala halne================================
    def termsandcond(self):
        self.new = 1
        self.url = "file:///D:/html/LANDING%20PAGE/index.html"
        webbrowser.open(self.url,new=self.new)








if __name__ == "__main__":
    main()