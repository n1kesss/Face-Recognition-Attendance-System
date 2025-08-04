from tkinter import* #forgui
from tkinter import ttk #stylish toolkit
from PIL import Image,ImageTk #for image
from tkinter import messagebox
import mysql.connector 
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Student Management")

        #========================variables====================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        

        #bg image
        img3=Image.open(r"D:\PROJECTS\Face Recognition Attendance System\images\foratten.jpg")
        img3=img3.resize((1920,1080),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1920,height=1080)

        #main frame 

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=60,y=150,width=1800,height=800)

        #left lable frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details:",font=("Comfortaa Light",16,"bold","underline"))
        Left_frame.place(x=30,y=10,width=850,height=770)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=12,y=150,width=820,height=400)

        #lables entry
        #attendence id 

        attendanceID_Label=Label(left_inside_frame,text="AttendanceID:",font=("Comfortaa Light",14,"bold"),bg="white")
        attendanceID_Label.grid(row=0,column=0,sticky=W)

        attendanceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("Comfortaa Light",14,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=5,pady=20,sticky=W)

#rool
        rollLabel=Label(left_inside_frame,text="Roll:",bg="white",font="comicsansns 14 bold")
        rollLabel.grid(row=0,column=2)

        atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font="comicsansns 14 bold")
        atten_roll.grid(row=0,column=3,padx=10,pady=20)

#name
        nameLabel=Label(left_inside_frame,text="Name:",bg="white",font="comicsansns 14 bold")
        nameLabel.grid(row=1,column=0)

        atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font="comicsansns 14 bold")
        atten_name.grid(row=1,column=1,padx=5,pady=20)

#dep 
        depLabel=Label(left_inside_frame,text="Department:",bg="white",font="comicsansns 14 bold")
        depLabel.grid(row=1,column=2)

        atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font="comicsansns 14 bold")
        atten_dep.grid(row=1,column=3,pady=20)

        # time  
        timeLabel=Label(left_inside_frame,text="Time:",bg="white",font="comicsansns 14 bold")
        timeLabel.grid(row=2,column=0)

        atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font="comicsansns 14 bold")
        atten_time.grid(row=2,column=1,pady=20)

# Date
        dateLabel=Label(left_inside_frame,text="Date:",bg="white",font="comicsansns 14 bold")
        dateLabel.grid(row=2,column=2)

        atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font="comicsansns 14 bold")
        atten_date.grid(row=2,column=3,pady=20)

# attendance staat
        attendanceLabel=Label(left_inside_frame,text="Attendance Status:",bg="white",font="comicsansns 14 bold")
        attendanceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 14 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=25)
        self.atten_status.current(0)

        #buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=100,y=330,width=600,height=36)

#======================================================= ALL BUTTONS =======================================================================
        save_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=19,font=("Comfortaa Light",13,"bold"),fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv,width=19,font=("Comfortaa Light",13,"bold"),fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
        update_btn.grid(row=0,column=1)


        reset_btn=Button(btn_frame,text="Clear all",width=19,command=self.reset_data,font=("Comfortaa Light",13,"bold"),fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
        reset_btn.grid(row=0,column=2)
#===========================================================================================================================================

        #Right lable frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Database:",font=("Comfortaa Light",16,"bold","underline"))
        Right_frame.place(x=900,y=10,width=850,height=770)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=12,y=10,width=820,height=720)

        #scrool bar table 

        scrool_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrool_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scrool_x.set,yscrollcommand=scrool_y.set)

        scrool_x.pack(side=BOTTOM,fill=X)
        scrool_y.pack(side=RIGHT,fill=Y)

        scrool_x.config(command=self.AttendanceReportTable.xview)
        scrool_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings" #removing the space try remoing it u will understannd
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


#=================================fetch data=====================


    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
                self.AttendanceReportTable.insert("",END,values=i)

#==================import csv =====================
        
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File",".*csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
                csvread=csv.reader(myfile,delimiter=",")
                for i in csvread:
                        mydata.append(i)
                self.fetchData(mydata)

#==================export csv =====================

    def exportCsv(self):
        # try:
                if len(mydata)<1:
                        messagebox.showerror("ERROR","No data found to export",parent=self.root)
                        return False
                fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File",".*csv"),("All File","*.*")),parent=self.root)
                with open(fln,mode="w",newline="") as myfile:
                        exp_write=csv.writer(myfile,delimiter=",")
                        for i in mydata:
                                exp_write.writerow(i)
                        messagebox.showinfo("Data export","Your data is exported to"+os.path.basename(fln)+"Successfully")

        # except Exception as es:
        #         messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("Status")






if __name__ == "__main__":
        root=Tk()
        obj=Attendance(root)
        root.mainloop()