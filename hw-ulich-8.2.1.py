class Teacher:
    def __init__(self, name, education, experience):
        self._name = name
        self._education = education
        self._experience = experience
        self._student_marks = {}

    @property
    def name(self):
        return self._name

    @property
    def education(self):
        return self._education

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, years):
        self._experience = years

    def get_teacher_data(self):
        if self._experience < 5:
            return f"{self._name}, образование {self._education}, опыт работы {self._experience} года"
        else:
            return f"{self._name}, образование {self._education}, опыт работы {self._experience} лет"

    def add_mark(self, student_name, mark):
        self._student_marks[student_name] = mark
        return f"{self._name} поставил оценку {mark} студенту {student_name}"

    def remove_mark(self, student_name, mark):
        if student_name in self._student_marks and self._student_marks[student_name] == mark:
            del self._student_marks[student_name]
            return f"{self._name} удалил оценку {mark} студенту {student_name}"
        else:
            return f"Оценка {mark} студента {student_name} не найдена"

    def give_a_consultation(self, class_name):
        return f"{self._name} провел консультацию в классе {class_name}"


# проверка

teacher = Teacher("Иван Петров", "БГПУ", 4)
print(teacher.get_teacher_data())
print(teacher.add_mark("Петр Сидоров", 4))
print(teacher.remove_mark("Дмитрий Степанов", 3))
print(teacher.give_a_consultation("9Б"))
teacher.experience = 5
print(teacher.get_teacher_data())
