class Employee:
    """
    Базовый класс сотрудника.
    """

    def __init__(self, name, salary):
        """
        Инициализация сотрудника.

        :param name: имя сотрудника
        :param salary: базовая зарплата
        """
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        """
        Возвращает базовую зарплату сотрудника.
        """
        return self.salary


class Manager(Employee):
    """
    Класс менеджера.
    """

    def __init__(self, name, salary, bonus):
        """
        Инициализация менеджера.

        :param name: имя менеджера
        :param salary: базовая зарплата
        :param bonus: бонус менеджера
        """
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_salary(self):
        """
        Зарплата менеджера = базовая + бонус.
        """
        return self.salary + self.bonus


class Developer(Employee):
    """
    Класс разработчика.
    """

    def __init__(self, name, salary, overtime_hours, hourly_rate):
        """
        Инициализация разработчика.

        :param name: имя разработчика
        :param salary: базовая зарплата
        :param overtime_hours: количество сверхурочных часов
        :param hourly_rate: оплата за час
        """
        super().__init__(name, salary)
        self.overtime_hours = overtime_hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        """
        Зарплата разработчика = базовая + сверхурочные.
        """
        return self.salary + self.overtime_hours * self.hourly_rate


# Пример использования
manager = Manager("Иван Иванов", 50000, 15000)
developer = Developer("Пётр Петров", 40000, 10, 500)

print("Зарплата менеджера:", manager.calculate_salary(), "руб.")
print("Зарплата разработчика:", developer.calculate_salary(), "руб.")
