from tkinter import* #forgui
from tkinter import ttk #stylish toolkit
from PIL import Image,ImageTk #for image
from tkinter import messagebox
# import mysql.connector 
# import cv2


class Developer:
 def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1030+0+0")
        self.root.title("Developer")


        img3=Image.open(r"D:\PROJECTS\Face Recognition Attendance System\images\devs1.jpg")
        img3=img3.resize((1920,1080),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1920,height=1080)



if __name__ == "__main__":
        root=Tk()
        obj=Developer(root)
        root.mainloop()