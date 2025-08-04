from tkinter import* #forgui
from tkinter import ttk #stylish toolkit
from PIL import Image,ImageTk #for image
from tkinter import messagebox
import mysql.connector 
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Recognization:
    def __init__(self,root):
        self.root=root
        
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognization")

        #bg img


        img_bottom=Image.open(r"D:\PROJECTS\Face Recognition Attendance System\images\facerecog.jpg")
        img_bottom=img_bottom.resize((1920,1080),Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl1=Label(self.root,image=self.photoimg_bottom)
        f_lbl1.place(x=0,y=0,width=1920,height=1080)

        

        #train button

        b1=Button(f_lbl1,text="[ Detect Face ]",cursor="hand2",command=self.face_recog,font=("Amasis MT Pro Black",15,),fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
        b1.place(x=740,y=450,width=400,height=80)



        #===================attendence=================
        
    def mark_attendance(self,i,r,n,d):
        with open("attendence.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_List=[]
            for line in myDataList:
                entry=line.split((","))
                name_List.append(entry[0])
            if ((i not in name_List) and (r not in name_List) and (n not in name_List) and (d not in name_List)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")


        #face rec=====================================

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf): #agrument haru 
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #gray ma convert gareko 
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[] 

            for (x,y,w,h) in features: 
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3) 
                id,predict=clf.predict(gray_image[y:y+h,x:x+w]) #predict formula 
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="sqluser",password="password",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)




                if confidence>81:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    self.mark_attendance(i,r,n,d)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)    #unknown ko lagi 
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,y]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml") #training gareko photo ko data clasifier.xml vitra hunxa 

        video_cap=cv2.VideoCapture(0)  # 0 le laptop ko cam auxa aagadi ko 1 le pachadi ne xa vane arko cam auxa 

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:  #jaba samma enter thichdaina taba samma jadaina window 
                break
        video_cap.release()
        cv2.destroyAllWindows()






if __name__ == "__main__":
        root=Tk()
        obj=Face_Recognization(root)
        root.mainloop()