class Record:
    def __init__(self, student_id, subject_code):
        self.student_id = student_id
        self.subject_code = subject_code
        self.grades = []
        self.attended = 0
        self.total_classes = 0

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            raise ValueError("Grade must be between 0 and 100")

    def mark_attendance(self, present):
        self.total_classes += 1
        if present:
            self.attended += 1

    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0.0

    def attendance_percentage(self):
        return (self.attended / self.total_classes * 100) if self.total_classes > 0 else 0.0