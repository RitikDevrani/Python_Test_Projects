CREATE DATABASE face_recognition;
USE face_recognition;
CREATE TABLE regteach (
    fname VARCHAR(50),
    lname VARCHAR(50),
    contact VARCHAR(20),
    email VARCHAR(100) PRIMARY KEY,
    security_q VARCHAR(100),
    security_a VARCHAR(100),
    password VARCHAR(100)
);

CREATE TABLE student_table (
    Student_ID VARCHAR(20) PRIMARY KEY,
    Name VARCHAR(100),
    Department VARCHAR(50),
    Course VARCHAR(50),
    Year VARCHAR(20),
    Semester VARCHAR(20),
    Divi VARCHAR(20),
    Gender VARCHAR(10),
    DOB VARCHAR(20),
    Mobile_No VARCHAR(15),
    Address TEXT,
    Roll_No VARCHAR(20),
    Email VARCHAR(100),
    Teacher_Name VARCHAR(100),
    PhotoSample VARCHAR(10)
);

CREATE TABLE stdattendance (
    std_id VARCHAR(20),
    std_roll_no VARCHAR(20),
    std_name VARCHAR(100),
    std_time TIME,
    std_date DATE,
    std_attendance VARCHAR(20)
);



