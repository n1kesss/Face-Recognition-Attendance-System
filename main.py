from tkinter import* #forgui
from tkinter import ttk #stylish toolkit
from PIL import Image,ImageTk #for image
import tkinter
import os
from student import Student
from train import Train
from face_recognition import Face_Recognization
from attendance  import Attendance
from developer import Developer
from help import Help



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1030+0+0")
        self.root.title("Face Attendance Recognition System")



#bg image
        img3=Image.open(r"D:\PROJECTS\Face Recognition Attendance System\images\11111.jpg")
        img3=img3.resize((1920,1080),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1920,height=1080)



#====================time=======================


#student button======================================================
        img4=Image.open(r"D:\PROJECTS\Face Recognition Attendance System\images\std1.jpg")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=350,width=350,height=150)

        b1=Button(bg_img,text="STUDENT DETAILS",command=self.student_details,cursor="hand2",font=("Myriad Pro Regular",15,),fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
        b1.place(x=200,y=500,width=350,height=40)

#detect face
        img5=Image.open(r"D:\PROJECTS\Face Recognition Attendance System\images\det1.jpg")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=600,y=350,width=350,height=150)

        b1=Button(bg_img,text="FACE RECOGNITION",cursor="hand2",command=self.face_data,font=("Amasis MT Pro Black",15,),fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
        b1.place(x=600,y=500,width=350,height=40)

#Attendence
        img6=Image.open(r"D:\PROJECTS\Face Recognition Attendance System\images\att.jpg")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=1000,y=350,width=350,height=150)

        b1=Button(bg_img,text="ATTENDENCE",cursor="hand2",command=self.attendance_data,font=("Amasis MT Pro Black",15,),fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
        b1.place(x=1000,y=500,width=350,height=40)

#help
        img7=Image.open(r"D:\PROJECTS\Face Recognition Attendance System\images\hlp.jpg")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1400,y=350,width=350,height=150)

        b1=Button(bg_img,text="HELP",cursor="hand2",command=self.help_data,font=("Amasis MT Pro Black",15,),fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
        b1.place(x=1400,y=500,width=350,height=40)

#train
        img8=Image.open(r"D:\PROJECTS\Face Recognition Attendance System\images\tra1.jpg")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=650,width=350,height=150)

        b1=Button(bg_img,text="TRAIN DATA",cursor="hand2",command=self.train_data,font=("Amasis MT Pro Black",15,),fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
        b1.place(x=200,y=800,width=350,height=40)

#photos btn
        img9=Image.open(r"D:\PROJECTS\Face Recognition Attendance System\images\cam.jpg")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=600,y=650,width=350,height=150)

        b1=Button(bg_img,text="PHOTOS",cursor="hand2",command=self.open_img,font=("Amasis MT Pro Black",15,),fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
        b1.place(x=600,y=800,width=350,height=40)

#developers btn
        img10=Image.open(r"D:\PROJECTS\Face Recognition Attendance System\images\dev.jpg")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=1000,y=650,width=350,height=150)

        b1=Button(bg_img,text="DEVELOPERS",cursor="hand2",command=self.developer_data,font=("Amasis MT Pro Black",15,),fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
        b1.place(x=1000,y=800,width=350,height=40)

#exit btn
        img11=Image.open(r"D:\PROJECTS\Face Recognition Attendance System\images\exi.jpg")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1400,y=650,width=350,height=150)

        b1=Button(bg_img,text="EXIT",cursor="hand2",command=self.iExit,font=("Amasis MT Pro Black",15,),fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
        b1.place(x=1400,y=800,width=350,height=40)


    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recogniation","Do you really want to exit this project ?",parent=self.root)
        if self.iExit >0:
                self.root.destroy()
        else:
                return


# =============function buttions==============

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognization(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
        





if __name__ == "__main__":
        root=Tk()
        obj=Face_Recognition_System(root)
        root.mainloop()
