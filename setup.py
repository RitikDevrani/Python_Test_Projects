import cx_Freeze
import sys
import os

# Set base for Windows app (No console)
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# For Tcl/Tk with Python 3.12
os.environ['TCL_LIBRARY'] = r"C:\Users\HP\AppData\Local\Programs\Python\Python312\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\HP\AppData\Local\Programs\Python\Python312\tcl\tk8.6"

executables = [cx_Freeze.Executable(
    script="Face_Recognition_Software.py",
    base=base,
    icon="face_recognition_icon.ico"
)]

packages = ["tkinter", "os", "cv2", "PIL", "mysql", "numpy"]
include_files = [
    (r"C:\Users\HP\AppData\Local\Programs\Python\Python312\DLLs\tcl86t.dll", "tcl86t.dll"),
    (r"C:\Users\HP\AppData\Local\Programs\Python\Python312\DLLs\tk86t.dll", "tk86t.dll"),
    "Images_GUI/",
    "data_img/",
    "attendance_report/",
    "clf.xml",
    "haarcascade_frontalface_default.xml",
    "face_recognition_icon.ico"
]

cx_Freeze.setup(
    name="Facial Recognition Software",
    version="1.0",
    description="Face Recognition Automatic Attendance System",
    options={"build_exe": {
        "packages": packages,
        "include_files": include_files
    }},
    executables=executables
)
