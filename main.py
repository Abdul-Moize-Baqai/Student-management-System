from Models.manager import SystemManager

def display_menu():
    print("\n" + "="*60)
    print("     STUDENT MANAGEMENT SYSTEM - BONUS EDITION")
    print("="*60)
    print("1. Add Student")
    print("2. Add Subject")
    print("3. Enroll Student")
    print("4. Add Grade")
    print("5. Mark Attendance")
    print("6. View Student Report")
    print("7. View All Students")
    print("8. View GPA Ranking")
    print("9. Subject Statistics")
    print("10. Update/Delete Student")
    print("11. Export Student Report to File")
    print("12. Exit")
    print("-"*60)

def main():
    manager = SystemManager()

    while True:
        display_menu()
        choice = input("Choose (1-12): ").strip()

        try:
            if choice == '1':
                sid = input("Student ID: ").strip()
                name = input("Name: ").strip()
                section = input("Section: ").strip()
                manager.add_student(sid, name, section)
                print("Student added | ", "Reg No= ",sid, "|" , "Name= ", name, "|" , "Section= ", section)
            elif choice == '2':
                code = input("Subject Code: ").strip()
                name = input("Subject Name: ").strip()
                credits = int(input("Credit Hours: "))
                manager.add_subject(code, name, credits)
                print("Subject added!")

            elif choice == '3':
                sid = input("Student ID: ").strip()
                code = input("Subject Code: ").strip()
                manager.enroll_student(sid, code)
                print("Enrolled!")

            elif choice == '4':
                sid = input("Student ID: ").strip()
                code = input("Subject Code: ").strip()
                grade = float(input("Grade: "))
                manager.add_grade(sid, code, grade)
                print("Grade added!")

            elif choice == '5':
                sid = input("Student ID: ").strip()
                code = input("Subject Code: ").strip()
                present = input("Present? (y/n): ").lower() == 'y'
                manager.mark_attendance(sid, code, present)
                print("Attendance marked!")

            elif choice == '6':
                sid = input("Student ID: ").strip()
                print(manager.generate_student_report(sid))

            elif choice == '7':
                print(manager.view_all_students())

            elif choice == '8':
                print(manager.get_gpa_ranking())

            elif choice == '9':
                code = input("Subject Code: ").strip()
                print(manager.get_subject_statistics(code))

            elif choice == '10':
                sid = input("Student ID: ").strip()
                print("1. Update Name/Section  2. Delete Student")
                opt = input("Choose: ")
                if opt == '1':
                    name = input("New Name (blank to skip): ").strip()
                    sec = input("New Section (blank to skip): ").strip()
                    manager.update_student(sid, name or None, sec or None)
                elif opt == '2':
                    if input(f"Delete {sid}? Type YES: ") == "YES":
                        manager.delete_student(sid)
                        print("Student deleted!")

            elif choice == '11':
                sid = input("Student ID: ").strip()
                filename = input("Filename (e.g. report.txt): ").strip() or f"{sid}_report.txt"
                manager.export_report(sid, filename)

            elif choice == '12':
                manager.save_all_data()
                print("All data saved. Goodbye!")
                break

        except ValueError as e:
            print(f"ERROR: {e}")

if __name__ == "__main__":
    main()