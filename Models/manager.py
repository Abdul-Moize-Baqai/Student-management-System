import os
from .student import Student
from .subject import Subject
from .record import Record

class SystemManager:
    def __init__(self):
        self.students = {}
        self.subjects = {}
        self.records = {}
        self.data_dir = "data"
        os.makedirs(self.data_dir, exist_ok=True)
        self.load_all_data()

    def add_student(self, sid, name, section):
        if sid in self.students:
            raise ValueError("Student ID already exists!")
        self.students[sid] = Student(sid, name, section)

    def add_subject(self, code, name, credits):
        if code in self.subjects:
            raise ValueError("Subject code already exists!")
        self.subjects[code] = Subject(code, name, credits)

    def enroll_student(self, sid, code):
        if sid not in self.students:
            raise ValueError("Student not found! Add student first.")
        if code not in self.subjects:
            raise ValueError("Subject not found! Add subject first.")
        self.students[sid].enroll(code)
        key = (sid, code)
        if key not in self.records:
            self.records[key] = Record(sid, code)

    def add_grade(self, sid, code, grade):
        if sid not in self.students:
            raise ValueError("Student not found!")
        if code not in self.subjects:
            raise ValueError("Subject not found!")
        key = (sid, code)
        if key not in self.records:
            raise ValueError("Student not enrolled in this subject!")
        self.records[key].add_grade(grade)

    def mark_attendance(self, sid, code, present):
        if sid not in self.students:
            raise ValueError("Student not found!")
        key = (sid, code)
        if key not in self.records:
            raise ValueError("Student not enrolled in this subject!")
        self.records[key].mark_attendance(present)

    def generate_student_report(self, sid):
        if sid not in self.students:
            return "\nStudent not found!\n"
        student = self.students[sid]
        lines = [f"\n{'='*60}", "STUDENT REPORT", f"Name: {student.name} | ID: {sid} | Section: {student.section}", f"Enrolled Subjects: {len(student.enrolled_subjects)}", '='*60]
        total_avg = total_att = count = 0
        for code in student.enrolled_subjects:
            sub = self.subjects[code]
            rec = self.records[(sid, code)]
            avg = rec.average_grade()
            att = rec.attendance_percentage()
            total_avg += avg
            total_att += att
            count += 1
            lines.append(f"\n{sub.name} ({code}) - {sub.credits} credits")
            lines.append(f"   Grades: {rec.grades or 'None'}")
            lines.append(f"   Average: {avg:.2f} | Attendance: {rec.attended}/{rec.total_classes} ({att:.1f}%)")
        if count:
            lines.append(f"\nOVERALL AVERAGE: {total_avg/count:.2f} | OVERALL ATTENDANCE: {total_att/count:.1f}%")
            lines.append(f"GPA: {self.calculate_gpa(sid):.2f}/4.00")
        lines.append('='*60)
        return "\n".join(lines)

    def view_all_students(self):
        if not self.students:
            return "\nNo students registered.\n"
        lines = ["\nALL STUDENTS", "-"*50]
        for sid, s in sorted(self.students.items()):
            lines.append(f"{sid} | {s.name} | {s.section} | Subjects: {len(s.enrolled_subjects)}")
        return "\n".join(lines)

    def calculate_gpa(self, sid):
        student = self.students[sid]
        total_points = total_credits = 0
        for code in student.enrolled_subjects:
            avg = self.records[(sid, code)].average_grade()
            credits = self.subjects[code].credits
            if avg >= 90: gp = 4.0
            elif avg >= 80: gp = 3.7
            elif avg >= 70: gp = 3.3
            elif avg >= 60: gp = 2.7
            elif avg >= 50: gp = 2.0
            else: gp = 0.0
            total_points += gp * credits
            total_credits += credits
        return round(total_points / total_credits, 2) if total_credits else 0.0

    def get_gpa_ranking(self):
        ranked = []
        for sid in self.students:
            gpa = self.calculate_gpa(sid)
            ranked.append((gpa, self.students[sid].name, sid))
        ranked.sort(reverse=True)
        lines = ["\nGPA RANKING", "-"*50]
        for i, (gpa, name, sid) in enumerate(ranked, 1):
            lines.append(f"{i}. {name} ({sid}) → GPA: {gpa:.2f}")
        return "\n".join(lines)

    def get_subject_statistics(self, code):
        if code not in self.subjects:
            return "Subject not found!"
        grades = []
        for (sid, sc), rec in self.records.items():
            if sc == code and rec.grades:
                grades.extend(rec.grades)
        if not grades:
            return f"No grades for {self.subjects[code].name} yet."
        return f"\n{self.subjects[code].name} ({code})\nAverage: {sum(grades)/len(grades):.2f}\nHighest: {max(grades)}\nLowest: {min(grades)}\nStudents: {len([r for (s,c),r in self.records.items() if c==code])}\n"

    def update_student(self, sid, new_name=None, new_section=None):
        if sid not in self.students:
            raise ValueError("Student not found!")
        if new_name:
            self.students[sid].name = new_name
        if new_section:
            self.students[sid].section = new_section
        print("Student updated!")

    def delete_student(self, sid):
        if sid not in self.students:
            raise ValueError("Student not found!")
        keys = [k for k in self.records if k[0] == sid]
        for k in keys:
            del self.records[k]
        del self.students[sid]
        print("Student deleted!")

    def export_report(self, sid, filename):
        report = self.generate_student_report(sid)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"Report saved as {filename}")

    def save_all_data(self):
        with open(f"{self.data_dir}/students.txt", "w") as f:
            for s in self.students.values():
                f.write(f"{s.student_id}|{s.name}|{s.section}\n")
        with open(f"{self.data_dir}/subjects.txt", "w") as f:
            for sub in self.subjects.values():
                f.write(f"{sub.code}|{sub.name}|{sub.credits}\n")
        with open(f"{self.data_dir}/records.txt", "w") as f:
            for (sid, code), rec in self.records.items():
                grades = ",".join(map(str, rec.grades)) if rec.grades else ""
                f.write(f"{sid}|{code}|{grades}|{rec.attended}/{rec.total_classes}\n")

    def load_all_data(self):
        if os.path.exists(f"{self.data_dir}/students.txt"):
            with open(f"{self.data_dir}/students.txt") as f:
                for line in f:
                    if line.strip():
                        sid, name, sec = line.strip().split("|", 2)
                        self.add_student(sid, name, sec)
        if os.path.exists(f"{self.data_dir}/subjects.txt"):
            with open(f"{self.data_dir}/subjects.txt") as f:
                for line in f:
                    if line.strip():
                        code, name, cred = line.strip().split("|", 2)
                        self.add_subject(code, name, int(cred))
        if os.path.exists(f"{self.data_dir}/records.txt"):
            with open(f"{self.data_dir}/records.txt") as f:
                for line in f:
                    if not line.strip(): continue
                    parts = line.strip().split("|")
                    sid, code = parts[0], parts[1]
                    if sid in self.students and code in self.subjects:
                        self.enroll_student(sid, code)
                        rec = self.records[(sid, code)]
                        if len(parts) > 2 and parts[2]:
                            rec.grades = [float(x) for x in parts[2].split(",") if x]
                        if len(parts) > 3 and "/" in parts[3]:
                            a, t = map(int, parts[3].split("/"))
                            rec.attended = a
                            rec.total_classes = t