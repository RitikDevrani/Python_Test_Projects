import cv2
import os
import numpy as np
import mysql.connector
from tkinter import Tk, Label, Button
from tkinter import messagebox
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x768+0+0")
        self.root.title("Face Recognition Panel")
        self.root.wm_iconbitmap("face_recognition_icon.ico")

        # Header Image
        img = Image.open("Images_GUI/banner.jpg").resize((1530, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        Label(self.root, image=self.photoimg).place(x=0, y=0, width=1530, height=130)

        # Background Image
        bg1 = Image.open("Images_GUI/bg2.jpg").resize((1530, 768), Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1530, height=768)

        # Title Section
        title_lb1 = Label(bg_img, text="Welcome to Face Recognition Panel", font=("verdana", 30, "bold"), bg="white", fg="navyblue")
        title_lb1.place(x=0, y=0, width=1530, height=45)

        # Face Recognition Button
        btn_image = Image.open("Images_GUI/f_det.jpg").resize((180, 180), Image.LANCZOS)
        self.btn_photo = ImageTk.PhotoImage(btn_image)
        Button(bg_img, image=self.btn_photo, command=self.face_recog, cursor="hand2").place(x=600, y=170, width=180, height=180)
        Button(bg_img, text="Face Detector", command=self.face_recog, cursor="hand2", font=("tahoma", 15, "bold"), bg="white", fg="navyblue").place(x=600, y=350, width=180, height=45)

    def mark_attendance(self, student_id, roll_no, name):
        if not os.path.exists("attendance_report"):
            os.makedirs("attendance_report")
        with open("attendance_report/attendance.csv", "a+", newline="\n") as f:
            f.seek(0)
            data = f.readlines()
            attendance_list = [line.split(",")[0] for line in data]
            if student_id not in attendance_list:
                now = datetime.now()
                date = now.strftime("%y/%m/%d")
                time = now.strftime("%H:%M:%S")
                f.writelines(f"{student_id}, {roll_no}, {name}, {time}, {date}, Present\n")

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, clf):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
            for (x, y, w, h) in features:
                face = gray[y:y + h, x:x + w]
                id, confidence = clf.predict(face)
                confidence = int(100 * (1 - confidence / 300))

                conn = mysql.connector.connect(username='root', password='Ritik@2002', host='localhost', database='face_recognition', port=3306)
                cursor = conn.cursor()
                cursor.execute("SELECT Name, Roll_No, Student_ID FROM student_table WHERE Student_ID=%s", (id,))
                data = cursor.fetchone()

                if data and confidence > 85:
                    name, roll_no, student_id = data
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    cv2.putText(img, f"ID: {student_id}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Name: {name}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Roll No: {roll_no}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    self.mark_attendance(student_id, roll_no, name)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                conn.close()

        def recognize(img, clf, face_cascade):
            draw_boundary(img, face_cascade, 1.1, 10, clf)
            return img

        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")

        video_capture = cv2.VideoCapture(0)
        while True:
            ret, img = video_capture.read()
            if not ret:
                break
            img = recognize(img, clf, face_cascade)
            cv2.imshow("Face Detector", img)
            if cv2.waitKey(1) == 13:
                break

        video_capture.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    app = Face_Recognition(root)
    root.mainloop()


