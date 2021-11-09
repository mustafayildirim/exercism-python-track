class School:
    grades = {}
    def __init__(self):
        self.grades = {}

    def add_student(self, name, grade):
        grade_students = self.grades.get(grade)
        if grade_students:
            grade_students.append(name)
        else:
            grade_students = [name]
        self.grades[grade] = grade_students

    def roster(self):
        student_list = []
        if self.grades:
            for key in sorted(self.grades.keys()):
                students = self.grades[key]
                for student in sorted(students):
                    student_list.append(student)
        return student_list


    def grade(self, grade_number):
        grade_students = self.grades.get(grade_number)
        if grade_students:
            return sorted(grade_students)
        return []
