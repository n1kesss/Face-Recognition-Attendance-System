from tkinter import* #forgui
from tkinter import ttk #stylish toolkit
from PIL import Image,ImageTk #for image
from tkinter import messagebox
import mysql.connector 
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Data Train")

        # background
        
        img3=Image.open(r"D:\PROJECTS\Face Recognition Attendance System\images\pxfuel.jpg")
        img3=img3.resize((1920,1080),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1920,height=1080)

        

        #button    

        b1=Button(bg_img,text="[ TRAIN DATA ]",command=self.train_classifier,cursor="hand2",font=("Amasis MT Pro Black",15,),fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
        b1.place(x=740,y=700,width=400,height=80)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)] #getting data in path

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #grayscale image
            imageNp=np.array(img,'uint8') #changing in grid 
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        #==========train the classifier and save =================
        
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Data Completed!",parent=self.root)





#dont forget to put wallpaper with title 




if __name__ == "__main__":
        root=Tk()
        obj=Train(root)
        root.mainloop()