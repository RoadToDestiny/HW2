class Employee:
    """
    Базовый класс для всех сотрудников компании.
    
    Атрибуты:
        name (str): Имя сотрудника
        salary (float): Базовая зарплата сотрудника
    """

    def __init__(self, name, salary):
        """
        Конструктор базового класса Employee.
        
        Args:
            name (str): Имя сотрудника
            salary (float): Базовая зарплата
        """       
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        """
        Расчет зарплаты сотрудника.
        
        Returns:
            float: Базовая зарплата сотрудника
        """
        return self.salary
    
class Manager(Employee):
    """
    Класс менеджера, наследуется от Employee.
    
    Дополнительный атрибут:
        bonus (float): Бонус менеджера
    """
    
    def __init__(self, name, salary, bonus):
        """
        Конструктор класса Manager.
        
        Args:
            name (str): Имя менеджера
            salary (float): Базовая зарплата
            bonus (float): Бонус менеджера
        """
        super().__init__(name, salary)
        # Вызов конструктора родительского класса
        self.bonus = bonus
    
    def calculate_salary(self):
        """
        Расчет зарплаты менеджера с учетом бонуса.
        
        Returns:
            float: Общая зарплата (базовая + бонус)
        """
        return self.salary + self.bonus
    
class Developer(Employee):
    """
    Класс разработчика, наследуется от Employee.
    
    Дополнительные атрибуты:
        overtime_hours (float): Количество сверхурочных часов
        hourly_rate (float): Ставка за сверхурочный час
    """

    def __init__(self, name, salary, overtime_hours, hourly_rate):
        """
        Конструктор класса Developer.
        
        Args:
            name (str): Имя разработчика
            salary (float): Базовая зарплата
            overtime_hours (float): Сверхурочные часы
            hourly_rate (float): Ставка за час сверхурочной работы
        """
        # Вызов конструктора родительского класса
        super().__init__(name, salary)
        self.overtime_hours = overtime_hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        """
        Расчет зарплаты разработчика с учетом сверхурочных.
        
        Returns:
            float: Общая зарплата (базовая + оплата сверхурочных)
        """
        # Общая зарплата = базовая + сверхурочные
        return self.salary + (self.overtime_hours * self.hourly_rate)
    
# Пример использования
manager = Manager("Иван Иванов", 50000, 15000)
developer = Developer("Петр Петров", 40000, 10, 500)

print(f"Зарплата менеджера: {manager.calculate_salary()} руб.")
print(f"Зарплата разработчика: {developer.calculate_salary()} руб.")