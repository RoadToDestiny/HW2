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
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
    
    def calculate_salary(self):
        return self.salary + self.bonus