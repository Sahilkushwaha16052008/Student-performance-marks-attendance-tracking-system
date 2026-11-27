import json
import os
DATA_FILE = "students.json"

SUBJECTS = ["Maths", "Physics", "Chemistry","English", "Computer Science"]

# ACTIVITY 6: Object Modeling
class Student:

    def __init__(self, roll, name, marks, attended, total):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.attended = attended
        self.total = total

    def percentage(self):
        return sum(self.marks.values()) / len(self.marks)

    def attendance(self):
        if self.total == 0:
            return 0
        return (self.attended / self.total) * 100

    # ACTIVITY 5: Decision Making
    def grade(self):
        p = self.percentage()

        if min(self.marks.values()) < 33:
            return "Fail"
        elif p >= 90:
            return "A+"
        elif p >= 80:
            return "A"
        elif p >= 70:
            return "B"
        elif p >= 60:
            return "C"
        elif p >= 50:
            return "D"
        else:
            return "E"

    def eligibility(self):
        if self.attendance() >= 75:
            return "Eligible"
        else:
            return "Not Eligible"

    def display(self):
        print("\nRoll Number:", self.roll)
        print("Name:", self.name)

        for subject, mark in self.marks.items():
            print(subject, ":", mark)

        print("Percentage:", round(self.percentage(), 2), "%")
        print("Grade:", self.grade())
        print("Attendance:", round(self.attendance(), 2), "%")
        print("Exam Status:", self.eligibility())

    def to_dict(self):
        return {
            "roll": self.roll,
            "name": self.name,
            "marks": self.marks,
            "attended": self.attended,
            "total": self.total
        }


# ACTIVITY 3: Problem Decomposition
class TrackingSystem:

    def __init__(self):
        self.students = []
        self.load_data()

    # File Handling
    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file:
                data = json.load(file)

                for record in data:
                    student = Student(
                        record["roll"],
                        record["name"],
                        record["marks"],
                        record["attended"],
                        record["total"]
                    )
                    self.students.append(student)

    def save_data(self):
        data = []

        for student in self.students:
            data.append(student.to_dict())

        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)

    def add_student(self):
        roll = input("Enter roll number: ")

        for student in self.students:
            if student.roll == roll:
                print("Roll number already exists!")
                return

        name = input("Enter student name: ")
        marks = {}

        for subject in SUBJECTS:
            while True:
                mark = float(input(f"Enter {subject} marks: "))

                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break

                print("Enter marks between 0 and 100.")

        total = int(input("Total classes: "))
        attended = int(input("Classes attended: "))

        if total <= 0 or not 0 <= attended <= total:
            print("Invalid attendance!")
            return

        student = Student(roll, name, marks, attended, total)

        self.students.append(student)
        self.save_data()

        print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No student records found.")
            return

        for student in self.students:
            student.display()
            print("-" * 35)

    def search_student(self):
        roll = input("Enter roll number to search: ")

        for student in self.students:
            if student.roll == roll:
                student.display()
                return

        print("Student not found!")

    def delete_student(self):
        roll = input("Enter roll number to delete: ")

        for student in self.students:
            if student.roll == roll:
                self.students.remove(student)
                self.save_data()
                print("Student deleted successfully!")
                return

        print("Student not found!")

    # ACTIVITY 7: Data Analysis
    def analytics(self):
        if not self.students:
            print("No records available.")
            return

        total_percentage = 0
        total_attendance = 0

        for student in self.students:
            total_percentage += student.percentage()
            total_attendance += student.attendance()

        n = len(self.students)

        print("\n--- CLASS ANALYTICS ---")
        print("Total Students:", n)
        print("Class Average:", round(total_percentage / n, 2), "%")
        print("Average Attendance:", round(total_attendance / n, 2), "%")

        topper = max(self.students,
                     key=lambda s: s.percentage())

        print("Highest Scorer:", topper.name)
        print("Percentage:", round(topper.percentage(), 2), "%")

        print("\nSubject-wise Average:")

        for subject in SUBJECTS:
            total = 0

            for student in self.students:
                total += student.marks[subject]

            print(subject, ":", round(total / n, 2))

        print("\nStudents with Low Attendance:")

        for student in self.students:
            if student.attendance() < 75:
                print(student.name, "-",
                      round(student.attendance(), 2), "%")

    # ACTIVITY 4: Algorithm and Control Flow
    def menu(self):
        while True:
            print("\n===== SPMAT SYSTEM =====")
            print("1. Add Student")
            print("2. View All Students")
            print("3. Search Student")
            print("4. Delete Student")
            print("5. Class Analytics")
            print("6. Exit")

            choice = input("Enter your choice: ")

            try:
                if choice == "1":
                    self.add_student()

                elif choice == "2":
                    self.view_students()

                elif choice == "3":
                    self.search_student()

                elif choice == "4":
                    self.delete_student()

                elif choice == "5":
                    self.analytics()

                elif choice == "6":
                    print("Thank you for using SPMAT!")
                    break

                else:
                    print("Invalid choice!")

            except ValueError:
                print("Please enter valid numerical values.")


# ACTIVITY 8: Final Integrated Project
if __name__ == "__main__":
    system = TrackingSystem()
    system.menu()