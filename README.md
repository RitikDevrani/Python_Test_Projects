# Python_Test_Projects
## Face Recognition Attendance System

This is a Python-based Desktop Application for automated attendance using **Face Recognition**. It uses OpenCV, Tkinter GUI, MySQL database, and facial recognition via LBPH algorithm.

---

## 📸 Features

•  Face Detection using OpenCV  
•  Face Recognition using LBPH algorithm  
• Real-time Webcam Support  
•  Attendance CSV Auto Generation  
•  MySQL Database Integration  
•  Beautiful Tkinter GUI  
•  Standalone `.exe` Desktop App (via cx_Freeze)

---

## Technologies Used

- Python 3.12.5
  
- OpenCV (`opencv-contrib-python`)

- MySQL Connector (`mysql-connector-python`)

- Pillow (Image handling)

- NumPy

- Tkinter (GUI)

- cx_Freeze (to build `.exe`)

---

## Project Folder Structure

FaceRecognitionApp/

│

├── Face_Recognition_Software.py # Main application script

├── setup.py # cx_Freeze build script

├── clf.xml # Trained face recognition model

├── haarcascade_frontalface_default.xml # Face detection model

├── face_recognition_icon.ico # Application icon

│

├── Images_GUI/ # GUI images (buttons, banners, backgrounds)

├── data_img/ # Trained student face images

├── attendance_report/ # Auto-generated attendance CSV files

├── build/ # Contains final .exe (after build)

└── pycache/ # (auto-generated)


---

pip install -r requirements.txt

Run the app:


python Face_Recognition_Software.py
•  Make sure MySQL is installed & running, and database/table are properly created.

## How to Build Desktop .exe (Optional)
Install cx-Freeze:

pip install cx-Freeze

Build app:

python setup.py build

Go to build/exe.win-amd64-3.12/ and run Face_Recognition_Software.exe

