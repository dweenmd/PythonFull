class student:
    def __init__(self, name, Class, id):
        self.name = name
        self.id = id
        self.Class = Class

    def __repr__(self) -> str:
        return f' Name: {self.name}  class: {self.Class}  id: {self.id}'


class Teacher:
    def __init__(self, name, subject, id) -> None:
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self) -> str:
        return f'Teacher: {self.name}, subject: {self.subject}'


class school:
    def __init__(self, name) -> None:
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee < 6500:
            return 'not enough fee'
        else:
            id = len(self.students) + 1
            Student = student(name, 'c', id)
            self.students.append(Student)
            return f'{name} is enrolled with id: {id}, extra money{fee-6500}'

    def __repr__(self) -> str:
        print('welcome to', self.name)
        print('------------Our Teachers------------')
        for teacher in self.teachers:
            print(teacher)
        print('-----------Our Students------------')
        for student in self.students:
            print(student)
        return 'All Done for now'


phitron = school('Phitron')
phitron.enroll('alia', 5200)
phitron.enroll('rani', 8000)
phitron.enroll('aishwaraiya', 7000)
phitron.enroll('vaijan', 9000)

phitron.add_teacher('mula kaku', 'DS')
phitron.add_teacher('sona kaku', 'Algo')
phitron.add_teacher('dhola kaku', 'oop')

print(phitron)
