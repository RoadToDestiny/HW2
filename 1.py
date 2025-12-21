class Employee:
    """
    Класс для представления сотрудника в компании.
    
    Attributes:
        employee_id (int): Уникальный идентификатор сотрудника
        name (str): Имя сотрудника
        base_salary (float): Базовая зарплата сотрудника
        department (str): Отдел, в котором работает сотрудник
    """
    
    def __init__(self, employee_id, name, base_salary, department):
        """
        Инициализирует объект сотрудника.
        
        Args:
            employee_id (int): Уникальный идентификатор сотрудника
            name (str): Имя сотрудника
            base_salary (float): Базовая зарплата сотрудника
            department (str): Отдел, в котором работает сотрудник
        """
        self.employee_id = employee_id
        self.name = name
        self.base_salary = base_salary
        self.department = department

    def calculate_salary(self):
        """
        Рассчитывает зарплату сотрудника.
        
        Returns:
            float: Зарплата сотрудника
        """
        return self.base_salary

    def get_info(self):
        """
        Возвращает информацию о сотруднике.
        
        Returns:
            str: Строка с информацией о сотруднике
        """
        return f"ID: {self.employee_id}, {self.name}, Отдел: {self.department}"


class Manager(Employee):
    """
    Класс для представления менеджера в компании.
    
    Attributes:
        employee_id (int): Уникальный идентификатор сотрудника
        name (str): Имя сотрудника
        base_salary (float): Базовая зарплата сотрудника
        department (str): Отдел, в котором работает сотрудник
        bonus_percent (float): Процент бонуса от базовой зарплаты
        team_size (int): Размер команды под руководством менеджера
    """
    
    def __init__(self, employee_id, name, base_salary, department, bonus_percent, team_size):
        """
        Инициализирует объект менеджера.
        
        Args:
            employee_id (int): Уникальный идентификатор сотрудника
            name (str): Имя сотрудника
            base_salary (float): Базовая зарплата сотрудника
            department (str): Отдел, в котором работает сотрудник
            bonus_percent (float): Процент бонуса от базовой зарплаты
            team_size (int): Размер команды под руководством менеджера
        """
        super().__init__(employee_id, name, base_salary, department)
        self.bonus_percent = bonus_percent
        self.team_size = team_size

    def calculate_salary(self):
        """
        Рассчитывает зарплату менеджера с учетом бонуса.
        
        Returns:
            float: Зарплата менеджера
        """
        bonus = self.base_salary * (self.bonus_percent / 100)
        return self.base_salary + bonus

    def get_info(self):
        """
        Возвращает информацию о менеджере.
        
        Returns:
            str: Строка с информацией о менеджере
        """
        base_info = super().get_info()
        return f"{base_info}, Должность: Менеджер, Команда: {self.team_size} чел."


class Developer(Employee):
    """
    Класс для представления разработчика в компании.
    
    Attributes:
        employee_id (int): Уникальный идентификатор сотрудника
        name (str): Имя сотрудника
        base_salary (float): Базовая зарплата сотрудника
        department (str): Отдел, в котором работает сотрудник
        programming_language (str): Основной язык программирования
        experience_years (int): Опыт работы в годах
        overtime_hours (int): Количество сверхурочных часов в месяц
        overtime_rate (float): Ставка оплаты сверхурочных часов
    """
    
    def __init__(self, employee_id, name, base_salary, department, 
                 programming_language, experience_years, overtime_hours, overtime_rate):
        """
        Инициализирует объект разработчика.
        
        Args:
            employee_id (int): Уникальный идентификатор сотрудника
            name (str): Имя сотрудника
            base_salary (float): Базовая зарплата сотрудника
            department (str): Отдел, в котором работает сотрудник
            programming_language (str): Основной язык программирования
            experience_years (int): Опыт работы в годах
            overtime_hours (int): Количество сверхурочных часов в месяц
            overtime_rate (float): Ставка оплаты сверхурочных часов
        """
        super().__init__(employee_id, name, base_salary, department)
        self.programming_language = programming_language
        self.experience_years = experience_years
        self.overtime_hours = overtime_hours
        self.overtime_rate = overtime_rate

    def calculate_salary(self):
        """
        Рассчитывает зарплату разработчика с учетом сверхурочных.
        
        Returns:
            float: Зарплата разработчика
        """
        overtime_payment = self.overtime_hours * self.overtime_rate
        return self.base_salary + overtime_payment

    def get_info(self):
        """
        Возвращает информацию о разработчике.
        
        Returns:
            str: Строка с информацией о разработчике
        """
        base_info = super().get_info()
        return f"{base_info}, Должность: Разработчик, Язык: {self.programming_language}, Опыт: {self.experience_years} лет"


class Company:
    """
    Класс для представления компании и управления сотрудниками.
    
    Attributes:
        name (str): Название компании
        employees (list): Список сотрудников компании
    """
    
    def __init__(self, name):
        """
        Инициализирует объект компании.
        
        Args:
            name (str): Название компании
        """
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        """
        Добавляет сотрудника в компанию.
        
        Args:
            employee (Employee): Объект сотрудника для добавления
        """
        self.employees.append(employee)

    def remove_employee(self, employee_id):
        """
        Удаляет сотрудника из компании.
        
        Args:
            employee_id (int): Идентификатор сотрудника для удаления
        """
        self.employees = [e for e in self.employees if e.employee_id != employee_id]

    def calculate_total_payroll(self):
        """
        Рассчитывает общий фонд заработной платы компании.
        
        Returns:
            float: Общая сумма зарплат всех сотрудников
        """
        total = 0
        for employee in self.employees:
            total += employee.calculate_salary()
        return total

    def get_employees_by_department(self, department):
        """
        Возвращает список сотрудников указанного отдела.
        
        Args:
            department (str): Название отдела
            
        Returns:
            list: Список сотрудников отдела
        """
        return [e for e in self.employees if e.department == department]

    def print_all_employees(self):
        """
        Выводит информацию обо всех сотрудниках компании.
        """
        print(f"=== Сотрудники компании '{self.name}' ===")
        for employee in self.employees:
            salary = employee.calculate_salary()
            print(f"{employee.get_info()}, Зарплата: {salary:.2f} руб.")
        print(f"Всего сотрудников: {len(self.employees)}")
        print(f"Общий фонд зарплат: {self.calculate_total_payroll():.2f} руб.")
        print()


# Демонстрация работы

# Создание компании
company = Company("ТехноПрогресс")

# Создание менеджеров
manager1 = Manager(1, "Иван Иванов", 80000, "Управление", 20, 5)
manager2 = Manager(2, "Анна Сидорова", 90000, "Разработка", 25, 8)

# Создание разработчиков
developer1 = Developer(3, "Петр Петров", 70000, "Разработка", 
                       "Python", 3, 10, 1000)
developer2 = Developer(4, "Мария Козлова", 75000, "Разработка", 
                       "JavaScript", 5, 5, 1200)
developer3 = Developer(5, "Алексей Смирнов", 65000, "Тестирование", 
                       "Java", 2, 8, 800)

# Добавление сотрудников в компанию
company.add_employee(manager1)
company.add_employee(manager2)
company.add_employee(developer1)
company.add_employee(developer2)
company.add_employee(developer3)

# Вывод информации о сотрудниках
company.print_all_employees()

# Расчет зарплат отдельных сотрудников
print("=== Расчет зарплат ===")
print(f"Зарплата менеджера {manager1.name}: {manager1.calculate_salary():.2f} руб.")
print(f"Зарплата разработчика {developer1.name}: {developer1.calculate_salary():.2f} руб.")
print()

# Получение сотрудников по отделам
print("=== Сотрудники отдела Разработка ===")
dev_department = company.get_employees_by_department("Разработка")
for emp in dev_department:
    print(f"- {emp.name}: {emp.calculate_salary():.2f} руб.")

# Добавление нового сотрудника
print("\n=== Добавление нового сотрудника ===")
new_developer = Developer(6, "Ольга Новикова", 68000, "Разработка", 
                          "Python", 4, 7, 1100)
company.add_employee(new_developer)
print(f"Добавлен новый сотрудник: {new_developer.name}")

# Обновленная информация
company.print_all_employees()
