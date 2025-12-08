README.txt
Student Management System - Assignment 2
Submitted by: Abdul Moize Baqai

================================================================
How to Run the System
================================================================
1. Make sure Python 3 is installed on your computer
2. Open command prompt or terminal
3. Go to the project folder: student_management_system
4. Run the program by typing:
   python main.py
5. Use the menu (options 1 to 12) to add students, subjects, enroll, record grades, attendance, view reports, etc.
6. Choose option 12 (Exit) to save all data and quit

The program automatically creates the "data" folder if it doesn't exist and loads any previous data when started.

================================================================
Features Implemented
================================================================
Core Requirements (All Fully Implemented):
- Add new students with unique IDs
- Add subjects with unique codes and credit hours
- Enroll students in multiple subjects
- Automatically create a record when a student enrolls in a subject
- Add multiple grades for each subject and calculate average
- Display grade history
- Mark attendance (present/absent) and track total classes
- Calculate attendance percentage per subject
- Generate detailed student report showing:
    • Student details
    • Subjects taken
    • Grade summaries and history
    • Attendance summaries
    • Overall performance snapshot
- View all registered students
- Clean and readable text-based menu and output
- Proper error handling (e.g., "Student not found!", "Subject not found!")

Optional Bonus Features (All 5 Implemented):
- GPA calculation (weighted 4.0 scale using credit hours)
- Student ranking by GPA
- Subject-wise statistics (average, highest, lowest grade)
- Update student name/section or delete a student completely
- Export individual student report as a .txt file

================================================================
How Data is Stored
================================================================
All data is saved in the "data" folder using simple, readable plain text files with pipe (|) delimiter.

students.txt format:
1001|Abdul Moize Baqai|MSAI-25

subjects.txt format:
101|Python|3

records.txt format:
1001|101|85,90,88|14/16
→ student_id | subject_code | grades list | present/total_classes

Files are created automatically if they do not exist.
Data is loaded when the program starts and saved when you exit.

================================================================
Summary of Classes Used
================================================================
Student class        (models/student.py)
   - student_id, name, section, list of enrolled subjects

Subject class        (models/subject.py)
   - subject_code, subject_name, credit_hours

Record class         (models/record.py)
   - Manages grades list and attendance for one student-subject pair
   - Calculates average grade and attendance percentage

SystemManager class  (models/manager.py)
   - Main controller class
   - Handles adding students/subjects, enrollment, grades, attendance
   - Generates reports, GPA, ranking, statistics
   - Loads and saves all data to text files
   - Contains update/delete and export functionality

Project uses proper OOP principles:
- Encapsulation
- No global variables
- All logic inside classes
- main.py only contains menu and method calls

================================================================
Project Structure
================================================================
student_management_system/
├── main.py
├── models/
│   ├── __init__.py
│   ├── student.py
│   ├── subject.py
│   ├── record.py
│   └── manager.py
├── data/                  (created automatically)
│   ├── students.txt
│   ├── subjects.txt
│   └── records.txt
└── README.txt             (this file)

Fully tested and working perfectly.
All core requirements + all bonus features implemented.

Abdul Moize Baqai
December 2025