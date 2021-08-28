from random import randint
import operator


class Student:

    student_list = []

    def __init__(self, name_surname, group, grades: list, md_gr):
        self.name_surname = name_surname
        self.group = group
        self.grades = grades
        self.md_gr = md_gr

    def student_info(self):
        print(
            'Имя, фамилия: {}\nГруппа: {}\nОценки: {}\nСредний балл: {}\n'.format(
                self.name_surname, self.group, self.grades, self.md_gr
            )
        )

    def print_info(self):
        for k_student in Student.student_list:
            k_student.student_info()


def grades_gen():
    gr_lst = [randint(2, 5) for _ in range(5)]
    return gr_lst


for i_student in range(10):
    name_surname = input('Введите имя и фамилию {} студента: '.format(i_student + 1))
    gr_list = grades_gen()
    st = Student(name_surname, randint(100, 999), gr_list, round(sum(gr_list) / 5, 1))
    Student.student_list.append(st)


for j_student in sorted(Student.student_list, key=operator.attrgetter('md_gr')):
    j_student.student_info()
