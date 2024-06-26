class Teacher:
    def __init__(self, name, education, experience):
        self._name = name
        self._education = education
        self._experience = experience

    def get_teacher_data(self):
        return f"Имя: {self._name}, Возраст: {self._age}, стаж: {self._experience}"

    def add_mark(self, student, mark, discipline):
        pass

    def remove_mark(self, student, mark, discipline):
        pass

    def give_a_consultation(self, group, discipline, job_title):
        pass

class DisciplineTeacher(Teacher):
    def __init__(self, name, education, experience, discipline, job_title):
        super().__init__(name, education, experience)
        self._discipline = discipline
        self._job_title = job_title

    @property
    def discipline(self):
        return self._discipline

    @property
    def job_title(self):
        return self._job_title

    @job_title.setter
    def job_title(self, new_job_title):
        self._job_title = new_job_title

    def get_teacher_data(self):
        return f"{self._name}, образование {self._education}, опыт работы {self._experience} лет, предмет: {self._discipline}, должность: {self._job_title}"

    def add_mark(self, student, mark, discipline):
        print(f"Поставил оценку {mark} студенту {student}. Предмет: {self._discipline}")

    def remove_mark(self, student, mark, discipline):
        print(f"Удалил оценку {mark} у студента {student}. Предмет: {self._discipline}")

    def give_a_consultation(self, group, discipline, job_title):
        print(f"Проведена консультация в классе {group} по предмету {discipline} как {job_title}")


class Employer:
    employers_list = []
    employers_phones = []

    def __init__(self, name, surname, phone):
        self.__name = name
        self.__surname = surname
        self.__phone = phone
        Employer.employers_list.append(self)
        Employer.employers_list.append(self.__phone)

    def get_name (self):
        return self.__name

    def get_surname (self):
        return self.__surname

    def get_phone (self):
        return self.__phone

    @staticmethod
    def print_employers_data(self):
        for employers in Employer.employers_list:
            print(employers.get_name)
            print(employers.get_surname)
            print(employers.get_phone)
            print()


# проверка

teacher = DisciplineTeacher("Иван Петров", "БПГУ", 10, "Химия", "Директор")
print(teacher.get_teacher_data())
teacher.add_mark("Николай Иванов", 4, "Химия")
teacher.remove_mark("Дмитрий Сидоров", 3, "Химия")
teacher.give_a_consultation("10Б", "Химия", "Директор")

