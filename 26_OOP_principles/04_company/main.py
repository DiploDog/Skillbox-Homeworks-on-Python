class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_surname(self):
        return self.__surname


class Employee(Person):
    def salary(self):
        return 13000


class Manager(Employee):
    pass


class Agent(Employee):
    def __init__(self, name, surname, age, v_sell):
        super().__init__(name, surname, age)
        self.v_sell = v_sell

    def salary(self):
        return 5000 + round(5 * self.v_sell / 100)


class Worker(Employee):
    def __init__(self, name, surname, age, hours):
        super().__init__(name, surname, age)
        self.hours = hours

    def salary(self):
        return round(100 * self.hours)


emp_list = [
    Manager('Jack', 'Nikolson', 45),
    Manager('Marry', 'Poppins', 27),
    Manager('Larry', 'King', 54),
    Agent('Harry', 'Potter', 20, 7500),
    Agent('Peter', 'Parker', 27, 5000),
    Agent('Miles', 'Morales', 25, 4500),
    Worker('Homer', 'Simpson', 43, 100),
    Worker('Angel', 'Hamilton', 24, 170),
    Worker('Alex', 'Compton', 31, 124)
]

for emp in emp_list:
    print(
        '{} {}, {}; salary: {} rubles'.format(
            emp.get_name(), emp.get_surname(), emp.get_age(), emp.salary()
        )
    )
