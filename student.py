from tkinter import* #forgui
from tkinter import ttk #stylish toolkit
from PIL import Image,ImageTk #for image
from tkinter import messagebox
#import mysql.connector 
import cv2


class Student:
 def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Student Management")


        #===variables===

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


#bg image
        img3=Image.open(r"D:\PROJECTS\Face Recognition Attendance System\images\bgstd.jpg")
        img3=img3.resize((1920,1080),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1920,height=1080)



#main frame 

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=60,y=150,width=1800,height=800)

#left lable frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details:",font=("Comfortaa Light",16,"bold","underline"))
        Left_frame.place(x=30,y=10,width=850,height=770)

#current course info
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information:",font=("Comfortaa Light",16,"bold"))
        current_course_frame.place(x=5,y=100,width=840,height=150)

#Department

        dep_lable=Label(current_course_frame,text="Department:",font=("Comfortaa Light",15,"bold"),bg="white")
        dep_lable.grid(row=0,column=0)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("Comfortaa Light",16,"italic"),state="readonly",width=17)
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)

#course
        course_label=Label(current_course_frame,text="Course:",font=("Comfortaa Light",16,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("Comfortaa Light",16,"italic"),state="readonly",width=17)
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=5,pady=10,sticky=W)

#year
        year_lable=Label(current_course_frame,text="Year:",font=("Comfortaa Light",16,"bold"),bg="white")
        year_lable.grid(row=1,column=0,padx=5,pady=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("Comfortaa Light",16,"italic"),state="readonly",width=17)
        year_combo["values"]=("Select Year","1st year","2nd year","3rd year","4th year")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=5,pady=10,sticky=W)

#semester
        semester_lable=Label(current_course_frame,text="Semester:",font=("Comfortaa Light",16,"bold"),bg="white")
        semester_lable.grid(row=1,column=2,padx=5,pady=10,sticky=W)
        
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("Comfortaa Light",16,"italic"),state="readonly",width=17)
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=5,pady=10,sticky=W) #cell widget vanda thulo vayo vane stickey=W


#class student info
        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("Comfortaa Light",16,"bold"))
        class_Student_frame.place(x=5,y=260,width=840,height=480)

#student ID
        student_ID=Label(class_Student_frame,text="StudentID:",font=("Comfortaa Light",16,"bold"),bg="white")
        student_ID.grid(row=0,column=0,padx=10,sticky=W)

        studentID_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=15,font=("Comfortaa Light",16,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,sticky=W)

#student name
        studenName_label=Label(class_Student_frame,text="Student Name:",font=("Comfortaa Light",16,"bold"),bg="white")
        studenName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=15,font=("Comfortaa Light",16))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

#class division
        class_div_lable=Label(class_Student_frame,text="Class Division:",font=("Comfortaa Light",16,"bold"),bg="white")
        class_div_lable.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("Comfortaa Light",16),state="readonly",width=13)
        div_combo["values"]=("Select Division","A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

#Roll number
        roll_no_lable=Label(class_Student_frame,text="Roll no:",font=("Comfortaa Light",16,"bold"),bg="white")
        roll_no_lable.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=15,font=("Comfortaa Light",16))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

#gender
        gender_lable_lable=Label(class_Student_frame,text="Gender:",font=("Comfortaa Light",16,"bold"),bg="white")
        gender_lable_lable.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("Comfortaa Light",16),state="readonly",width=13)
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

#dob
        dob_lable_lable=Label(class_Student_frame,text="DOB:",font=("Comfortaa Light",16,"bold"),bg="white")
        dob_lable_lable.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=15,font=("Comfortaa Light",16))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

#email
        email_lable_lable=Label(class_Student_frame,text="E-mail:",font=("Comfortaa Light",16,"bold"),bg="white")
        email_lable_lable.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=15,font=("Comfortaa Light",16))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

#phone no
        phone_lable_lable=Label(class_Student_frame,text="Phone No:",font=("Comfortaa Light",16,"bold"),bg="white")
        phone_lable_lable.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=15,font=("Comfortaa Light",16))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

#Address
        address_lable_lable=Label(class_Student_frame,text="Address:",font=("Comfortaa Light",16,"bold"),bg="white")
        address_lable_lable.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=15,font=("Comfortaa Light",16))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

#teachers name
        teacher_lable_lable=Label(class_Student_frame,text="Teacher's Name:",font=("Comfortaa Light",16,"bold"),bg="white")
        teacher_lable_lable.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=15,font=("Comfortaa Light",16))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

#radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take a photo sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        
        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No photo sample",value="No")
        radiobtn2.grid(row=6,column=1)

#buttons frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=18,y=250,width=800,height=36)

#======================================================= ALL BUTTONS =======================================================================
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=19,font=("Comfortaa Light",13,"bold"),fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=19,font=("Comfortaa Light",13,"bold"),fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=19,font=("Comfortaa Light",13,"bold"),fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("Comfortaa Light",13,"bold"),fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=18,y=300,width=800,height=36)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo",width=40,font=("Comfortaa Light",13,"bold"),fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Update Photo Sample",width=40,font=("Comfortaa Light",13,"bold"),fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
        update_photo_btn.grid(row=0,column=1)

#=====================================================================================================================================

#Right lable frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Database:",font=("Comfortaa Light",16,"bold","underline"))
        Right_frame.place(x=900,y=10,width=850,height=770)


#search system
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search Student Database:",font=("Comfortaa Light",16,"bold"))
        Search_frame.place(x=5,y=100,width=840,height=150)

        search_lable=Label(Search_frame,text="Search By:",font=("Comfortaa Light",16,"bold"),bg="white")
        search_lable.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        self.var_searchTX=StringVar()

        search_combo=ttk.Combobox(Search_frame,textvariable=self.var_searchTX,font=("Comfortaa Light",16,""),state="readonly",width=17)
        search_combo["values"]=("Roll No.",)
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)

        self.var_search=StringVar()

        search_entry=ttk.Entry(Search_frame,textvariable=self.var_search,width=12,font=("Comfortaa Light",16,""))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        search_btn=Button(Search_frame,text="Search",command=self.search_data,width=12,font=("Comfortaa Light",13,"bold"),fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(Search_frame,command=self.fetch_data,text="Show All",width=12,font=("Comfortaa Light",13,"bold"),fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
        showAll_btn.grid(row=0,column=4,padx=4)

#table frame

        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE,)
        table_frame.place(x=5,y=200,width=840,height=450)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="RollNo")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")

        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

#     ==========function declair=========== 
 def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
                try:
                        conn=mysql.connector.connect(host="localhost",username="sqluser",password="password",database="face_recognizer")
                        my_cursor=conn.cursor()
                        my_cursor.execute("Insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                                                        
                                                                                                        ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success","Student details has been added successfully.",parent=self.root)
                except Exception as es:
                        messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

        #fetch data
        
 def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",username="sqluser",password="password",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                data=my_cursor.fetchall()

                if len(data)!=0:
                        self.student_table.delete(*self.student_table.get_children())
                        for i in data:
                                self.student_table.insert("",END,values=i)
                        conn.commit()
                conn.close()

# ============auto fill the boxes=======

 def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])


#=============update function=================

 def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
                try:
                        Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                        if Update>0:

                                conn=mysql.connector.connect(host="localhost",username="sqluser",password="password",database="face_recognizer")
                                my_cursor=conn.cursor()
                                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.var_std_id.get()
                                                                                                        ))
                        else:
                                if not Update:
                                        return
                        messagebox.showinfo("Success","Student details has been updated successfully",parent=self.root)
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                except Exception as es:
                        messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


#=============================delete============

 def delete_data(self):
        if self.var_std_id.get()=="":
                messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
                try:
                        delete=messagebox.askyesno("Delete Student","Do you want to delete this student ?",parent=self.root)
                        if delete>0:
                                conn=mysql.connector.connect(host="localhost",username="sqluser",password="password",database="face_recognizer")
                                my_cursor=conn.cursor()
                                sql="delete from student where Student_id=%s"
                                val=(self.var_std_id.get(),)
                                my_cursor.execute(sql,val)
                        else:
                                if not delete:
                                        return

                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
                except Exception as es:
                        messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)       


#=====================reset=====================

 def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

        #=================================right panel Search=============================================== 

 def search_data(self):
        if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
                messagebox.showerror("Error","Student Roll number is required",parent=self.root)
        else:
                try:
                        conn = mysql.connector.connect(username='sqluser', password='password',host='localhost',database='face_recognizer',port=3306)
                        my_cursor = conn.cursor()
                        sql = "SELECT Dep,course,Year,Semester,Student_id,Name,Division,Roll,Gender,Dob,Email,Phone,Address,Teacher,PhotoSample FROM student where Roll='" +str(self.var_search.get()) + "'" 
                        my_cursor.execute(sql)
                        rows=my_cursor.fetchall()      
                        if len(rows)!=0:
                                self.student_table.delete(*self.student_table.get_children())
                                for i in rows:
                                        self.student_table.insert("",END,values=i)
                        # if rows==None:
                        #         messagebox.showerror("Error","Data Not Found",parent=self.root)
                                conn.commit()
                        conn.close()
                except Exception as es:
                        messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)







#=============================Generate data set take photo sample============================

 def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
                try:
                        conn=mysql.connector.connect(host="localhost",username="sqluser",password="password",database="face_recognizer")
                        my_cursor=conn.cursor()
                        my_cursor.execute("select * from student")
                        myresult=my_cursor.fetchall() #storing all data in myresult var
                        id=0 
                        for x in myresult:
                                id+=1
                        my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.var_std_id.get()==id+1
                                                                                                        ))
                        conn.commit()
                        self.fetch_data()
                        self.reset_data()
                        conn.close()

                                #load predefined data frontal face  from open cv 

                        face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #for  detection

                        def face_cropped(img):
                                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert into grayscale
                                        faces=face_classifier.detectMultiScale(gray,1.3,5)
                                        #1.3 = scaling factor , #5 = minimum neighbor

                                        for (x,y,w,h) in faces: #for rect
                                                face_cropped=img[y:y+h,x:x+w] #setting size
                                                return face_cropped
                                
                        cap=cv2.VideoCapture(0) #open camera
                        img_id=0
                        while True:
                                        ret,my_frame=cap.read()
                                        if face_cropped(my_frame) is not None:
                                                img_id+=1
                                                face=cv2.resize(face_cropped(my_frame),(450,450)) #crop resize img
                                                face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                                                file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg" #naming img
                                                cv2.imwrite(file_name_path,face)
                                                cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2) 
                                                cv2.imshow("Crpoped Face",face)

                                        if cv2.waitKey(1)==13 or int(img_id)==100: #samples
                                                break
                        cap.release()
                        cv2.destroyAllWindows()
                        messagebox.showinfo("Result","Generating data set complited!!!",parent=self.root)
                
                except Exception as es:
                        messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

























if __name__ == "__main__":
        root=Tk()
        obj=Student(root)
        root.mainloop()