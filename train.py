from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox

class Train:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x768+0+0")
        self.root.title("Train Panel")

        try:
            self.root.wm_iconbitmap("face_recognition_icon.ico")
        except Exception as e:
            print(f"Icon load error: {e}")

        # -------------------- Images --------------------
        try:
            img = Image.open(r"C:\\Users\\HP\\Documents\\Python_Test_Projects\\Images_GUI\\banner.jpg")
            img = img.resize((1530,130), Image.LANCZOS)
            self.photoimg = ImageTk.PhotoImage(img)

            f_lb1 = Label(self.root, image=self.photoimg)
            f_lb1.place(x=0, y=0, width=1530, height=130)

            bg1 = Image.open(r"C:\\Users\\HP\\Documents\\Python_Test_Projects\\Images_GUI\\t_bg1.jpg")
            bg1 = bg1.resize((1530,768), Image.LANCZOS)
            self.photobg1 = ImageTk.PhotoImage(bg1)

            bg_img = Label(self.root, image=self.photobg1)
            bg_img.place(x=0, y=130, width=1530, height=768)
        except Exception as e:
            print(f"Image load error: {e}")

        title_lb1 = Label(bg_img, text="Welcome to Training Panel", font=("verdana", 30, "bold"), bg="white", fg="navyblue")
        title_lb1.place(x=0, y=0, width=1530, height=45)

        # ------------------ Training Button ------------------
        try:
            std_img_btn = Image.open(r"C:\\Users\\HP\\Documents\\Python_Test_Projects\\Images_GUI\\t_btn1.png")
            std_img_btn = std_img_btn.resize((180,180), Image.LANCZOS)
            self.std_img1 = ImageTk.PhotoImage(std_img_btn)

            std_b1 = Button(bg_img, command=self.train_classifier, image=self.std_img1, cursor="hand2")
            std_b1.place(x=600, y=170, width=180, height=180)

            std_b1_1 = Button(bg_img, command=self.train_classifier, text="Train Dataset", cursor="hand2", font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
            std_b1_1.place(x=600, y=350, width=180, height=45)
        except Exception as e:
            print(f"Training Button error: {e}")

    # ================= Training Function =================
    def train_classifier(self):
        data_dir = "data_img"

        if not os.path.exists(data_dir):
            messagebox.showerror("Error", f"'{data_dir}' folder not found!", parent=self.root)
            return

        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        if len(path) == 0:
            messagebox.showerror("Error", "No images found in the training folder!", parent=self.root)
            return

        faces = []
        ids = []

        print(f"Total images found: {len(path)}")

        for image in path:
            try:
                img = Image.open(image).convert('L')  # grayscale
                imageNp = np.array(img, 'uint8')
                id = int(os.path.split(image)[1].split('.')[1])

                faces.append(imageNp)
                ids.append(id)

                # Show only every 10th image to avoid freezing
                if len(faces) % 10 == 0:
                    cv2.imshow("Training", imageNp)
                    cv2.waitKey(1)

                print(f"Processed: {image}")
            except Exception as e:
                print(f"Error in image '{image}': {e}")
                continue

        ids = np.array(ids)

        try:
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            clf.write("clf.xml")
        finally:
            try:
                cv2.destroyAllWindows()
            except:
                pass
            messagebox.showinfo("Result", "Training Dataset Completed!", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
