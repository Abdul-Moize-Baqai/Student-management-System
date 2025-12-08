class Student:
    def __init__(self, student_id, name, section):
        self.student_id = student_id
        self.name = name
        self.section = section
        self.enrolled_subjects = []  

    def enroll(self, subject_code):
        if subject_code not in self.enrolled_subjects:
            self.enrolled_subjects.append(subject_code)

    def __str__(self):
        return f"{self.name} ({self.student_id}) - {self.section}"