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
        