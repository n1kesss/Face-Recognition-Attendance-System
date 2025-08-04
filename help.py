from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import webbrowser


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

# This part is image labels setting start 

        # backgorund image 
        bg1=Image.open(r"D:\PROJECTS\Face Recognition Attendance System\images\forhelp.jpg")
        bg1=bg1.resize((1920,1080),Image.Resampling.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=1920,height=1080)


        # #title section
        # title_lb1 = Label(bg_img,text="Help Support",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        # title_lb1.place(x=0,y=0,width=1920,height=45)

        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1

        std_img_btn=Image.open(r"D:\PROJECTS\Face Recognition Attendance System\images\weblogo.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.website,image=self.std_img1,cursor="hand2")
        std_b1.place(x=1190,y=400,width=180,height=180)

        # std_b1_1 = Button(bg_img,command=self.website,text="Website",cursor="hand2",font=("tahoma",15,"bold"),bg="lightblue",fg="black")
        # std_b1_1.place(x=1190,y=580,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"D:\PROJECTS\Face Recognition Attendance System\images\fblogo.png")
        det_img_btn=det_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.facebook,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=500,y=400,width=180,height=180)

        # det_b1_1 = Button(bg_img,command=self.facebook,text="Facebook",cursor="hand2",font=("tahoma",15,"bold"),bg="lightblue",fg="black")
        # det_b1_1.place(x=500,y=580,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"D:\PROJECTS\Face Recognition Attendance System\images\youtubelogo.jpg")
        att_img_btn=att_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.youtube,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=730,y=400,width=180,height=180)

        # att_b1_1 = Button(bg_img,command=self.youtube,text="Youtube",cursor="hand2",font=("tahoma",15,"bold"),bg="lightblue",fg="black")
        # att_b1_1.place(x=730,y=580,width=180,height=45)

         # Help  Support  button 4
        hlp_img_btn=Image.open(r"D:\PROJECTS\Face Recognition Attendance System\images\outlooklogo.jpg")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,command=self.Mail,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=960,y=400,width=180,height=180)

        # hlp_b1_1 = Button(bg_img,command=self.Mail,text="Mail",cursor="hand2",font=("tahoma",15,"bold"),bg="lightblue",fg="black")
        # hlp_b1_1.place(x=960,y=580,width=180,height=45)


        # create function for button 
    
    
    def website(self):
        self.new = 1
        self.url = "https://towardsdatascience.com/face-recognition-how-lbph-works-90ec258c3d6b"
        webbrowser.open(self.url,new=self.new)
    
    def facebook(self):
        self.new = 1
        self.url = "https://www.facebook.com/"
        webbrowser.open(self.url,new=self.new)
    
    def youtube(self):
        self.new = 1
        self.url = "https://www.youtube.com/@n1kesjk"
        webbrowser.open(self.url,new=self.new)
    
    def Mail(self):
        self.new = 1
        #self.url = "https://mail.google.com"
        webbrowser.open("mailto:?to=nrougejk12@gmail.com&subject=Need help about: ", new=1)
        #webbrowser.open(self.url,new=self.new)





if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()