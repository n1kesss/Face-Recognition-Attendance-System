from tkinter import*
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


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

        #======================lable and entry======================

        fname=Label(frame,text="First Name:",font=("Comfortaa Light",15,"bold"),fg="#002B53",bg="#F2F2F2")
        fname.place(x=100,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("Comfortaa Light",15,""))
        fname_entry.place(x=103,y=125,width=270)

        #label2 
        lname=Label(frame,text="Last Name:",font=("Comfortaa Light",15,"bold"),fg="#002B53",bg="#F2F2F2")
        lname.place(x=100,y=170)

        #entry2 
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("Comfortaa Light",15,""))
        self.txt_lname.place(x=103,y=195,width=270)

                # ==================== section 2 -------- 2nd Columan===================

        #label1 
        contact=Label(frame,text="Contact No:",font=("Comfortaa Light",15,"bold"),fg="#002B53",bg="#F2F2F2")
        contact.place(x=530,y=100)

        #entry1 
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("Comfortaa Light",15,""))
        self.txt_contact.place(x=533,y=125,width=270)


        #label2 
        email=Label(frame,text="Email:",font=("Comfortaa Light",15,"bold"),fg="#002B53",bg="#F2F2F2")
        email.place(x=530,y=170)

        #entry2 
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("Comfortaa Light",15,""))
        self.txt_email.place(x=533,y=195,width=270)

                # ========================= Section 3 --- 1 Columan=================

        #label1 
        security_Q=Label(frame,text="Select Security Question:",font=("Comfortaa Light",15,"bold"),fg="#002B53",bg="#F2F2F2")
        security_Q.place(x=100,y=240)

        #Combo Box1
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("Comfortaa Light",15,""),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
        self.combo_security_Q.current(0)
        self.combo_security_Q.place(x=103,y=265,width=270)


        #label2 
        security_A=Label(frame,text="Security Answer:",font=("Comfortaa Light",15,"bold"),fg="#002B53",bg="#F2F2F2")
        security_A.place(x=100,y=325)

        #entry2 
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("Comfortaa Light",15,""))
        self.txt_security.place(x=103,y=350,width=270)

        # ========================= Section 4-----Column 2=============================

        #label1 
        pswd=Label(frame,text="Password:",font=("Comfortaa Light",15,"bold"),fg="#002B53",bg="#F2F2F2")
        pswd.place(x=530,y=240)

        #entry1 
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("Comfortaa Light",15,""))
        self.txt_pswd.place(x=533,y=265,width=270)


        #label2 
        confirm_pswd=Label(frame,text="Confirm Password:",font=("Comfortaa Light",15,"bold"),fg="#002B53",bg="#F2F2F2")
        confirm_pswd.place(x=530,y=325)

        #entry2 
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("Comfortaa Light",15,""))
        self.txt_confirm_pswd.place(x=533,y=350,width=270)

        #==================check====================

        self.var_check=IntVar()
        checkbtn = Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("Comfortaa Light",13,"bold"),fg="#002B53",bg="#F2F2F2")
        checkbtn.place(x=100,y=480,width=270)

        # Creating Button Register

        loginbtn=Button(frame,text="Register",command=self.register_data,font=("Comfortaa Light",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=103,y=510,width=270,height=35)

        # Creating Button  back to Login

        loginbtn1=Button(frame,text="Back to Login",font=("Comfortaa Light",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        loginbtn1.place(x=533,y=510,width=270,height=35)
        

        #================functions===================

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
                messagebox.showerror("Error","All fields are required")
        elif(self.var_pass.get() != self.var_confpass.get()):
                messagebox.showerror("Error","Password and confirm password must be same !")
        elif(self.var_check.get()==0):
                messagebox.showerror("Error","Please Check the Agree Terms and Conditons!")
        else:
                conn = mysql.connector.connect(username='sqluser', password='password',host='localhost',database='mydata',port=3306)
                mycursor = conn.cursor()
                query=("select * from register where email=%s")
                value=(self.var_email.get(),)
                mycursor.execute(query,value)
                row=mycursor.fetchone()

                if row!=None:
                        messagebox.showerror("Error","User already exist,please try another email")
                
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








if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()