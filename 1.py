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