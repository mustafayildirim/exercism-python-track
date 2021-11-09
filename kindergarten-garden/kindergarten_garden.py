children = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', \
    'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
plant_list = {'V': 'Violets', 'R': 'Radishes', 'C': 'Clover', 'G': 'Grass'}

class Garden:
    diagram = ''
    students = None
    def __init__(self, diagram, students=None):
        self.diagram = diagram
        if students:
            self.students = sorted(students)
        else:
            self.students = children


    def plants(self, student_name):
        student_index = self.students.index(student_name)
        plant_rows = self.diagram.splitlines()
        student_index = student_index * 2
        first = plant_list[plant_rows[0][student_index]]
        second = plant_list[plant_rows[0][student_index + 1]]
        third = plant_list[plant_rows[1][student_index]]
        fourth = plant_list[plant_rows[1][student_index + 1]]
        return [first, second, third, fourth]
