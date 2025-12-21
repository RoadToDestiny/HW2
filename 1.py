from abc import ABC, abstractmethod


class Employee(ABC):
    """
    Абстрактный базовый класс для всех сотрудников компании.

    Attributes:
        name (str): Имя сотрудника
        base_salary (float): Базовая зарплата сотрудника
    """

    def __init__(self, name: str, base_salary: float) -> None:
        """
        Конструктор базового класса Employee.

        Args:
            name (str): Имя сотрудника
            base_salary (float): Базовая зарплата сотрудника

        Raises:
            ValueError: Если имя пустое или зарплата отрицательная
        """
        if not name or not name.strip():
            raise ValueError("Имя сотрудника не может быть пустым")
        if base_salary < 0:
            raise ValueError("Зарплата не может быть отрицательной")
        
        self._name = name.strip()
        self._base_salary = base_salary

    @property
    def name(self) -> str:
        """
        Возвращает имя сотрудника.

        Returns:
            str: Имя сотрудника
        """
        return self._name

    @property
    def base_salary(self) -> float:
        """
        Возвращает базовую зарплату сотрудника.

        Returns:
            float: Базовая зарплата
        """
        return self._base_salary

    @abstractmethod
    def calculate_salary(self) -> float:
        """
        Абстрактный метод для расчета зарплаты.
        Должен быть реализован в каждом дочернем классе.

        Returns:
            float: Общая зарплата сотрудника
        """
        pass

    def __str__(self) -> str:
        """
        Возвращает строковое представление сотрудника.

        Returns:
            str: Информация о сотруднике
        """
        return f"Сотрудник: {self._name}, Базовая зарплата: {self._base_salary} руб."


class Manager(Employee):
    """
    Класс менеджера, наследуется от Employee.

    Attributes:
        bonus (float): Бонус менеджера
    """

    def __init__(self, name: str, base_salary: float, bonus: float) -> None:
        """
        Конструктор класса Manager.

        Args:
            name (str): Имя менеджера
            base_salary (float): Базовая зарплата
            bonus (float): Бонус менеджера

        Raises:
            ValueError: Если бонус отрицательный
        """
        super().__init__(name, base_salary)
        if bonus < 0:
            raise ValueError("Бонус не может быть отрицательным")
        self._bonus = bonus

    @property
    def bonus(self) -> float:
        """
        Возвращает бонус менеджера.

        Returns:
            float: Размер бонуса
        """
        return self._bonus

    def calculate_salary(self) -> float:
        """
        Расчет зарплаты менеджера с учетом бонуса.

        Returns:
            float: Общая зарплата (базовая + бонус)
        """
        return self._base_salary + self._bonus

    def __str__(self) -> str:
        """
        Возвращает строковое представление менеджера.

        Returns:
            str: Информация о менеджере
        """
        return f"Менеджер: {self._name}, Зарплата: {self.calculate_salary()} руб. (базовая: {self._base_salary}, бонус: {self._bonus})"


class Developer(Employee):
    """
    Класс разработчика, наследуется от Employee.

    Attributes:
        overtime_hours (float): Количество сверхурочных часов
        hourly_rate (float): Ставка за сверхурочный час
    """

    def __init__(self, name: str, base_salary: float, 
                 overtime_hours: float, hourly_rate: float) -> None:
        """
        Конструктор класса Developer.

        Args:
            name (str): Имя разработчика
            base_salary (float): Базовая зарплата
            overtime_hours (float): Сверхурочные часы
            hourly_rate (float): Ставка за час сверхурочной работы

        Raises:
            ValueError: Если сверхурочные часы или ставка отрицательные
        """
        super().__init__(name, base_salary)
        if overtime_hours < 0:
            raise ValueError("Сверхурочные часы не могут быть отрицательными")
        if hourly_rate < 0:
            raise ValueError("Ставка за час не может быть отрицательной")
        
        self._overtime_hours = overtime_hours
        self._hourly_rate = hourly_rate

    @property
    def overtime_hours(self) -> float:
        """
        Возвращает количество сверхурочных часов.

        Returns:
            float: Количество часов
        """
        return self._overtime_hours

    @property
    def hourly_rate(self) -> float:
        """
        Возвращает ставку за сверхурочный час.

        Returns:
            float: Ставка за час
        """
        return self._hourly_rate

    def calculate_salary(self) -> float:
        """
        Расчет зарплаты разработчика с учетом сверхурочных.

        Returns:
            float: Общая зарплата (базовая + оплата сверхурочных)
        """
        return self._base_salary + (self._overtime_hours * self._hourly_rate)

    def __str__(self) -> str:
        """
        Возвращает строковое представление разработчика.

        Returns:
            str: Информация о разработчике
        """
        overtime_pay = self._overtime_hours * self._hourly_rate
        return f"Разработчик: {self._name}, Зарплата: {self.calculate_salary()} руб. (базовая: {self._base_salary}, сверхурочные: {overtime_pay})"


def display_employee_info(employee: Employee) -> None:
    """
    Выводит информацию о сотруднике и его зарплате.

    Args:
        employee (Employee): Объект сотрудника
    """
    print(f"{employee}")
    print(f"  Рассчитанная зарплата: {employee.calculate_salary():.2f} руб.")
    print()


def main() -> None:
    """
    Основная функция для демонстрации работы классов сотрудников.
    """
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ СИСТЕМЫ УПРАВЛЕНИЯ СОТРУДНИКАМИ")
    print("=" * 60)
    
    try:
        # Создаем сотрудников
        manager = Manager("Иван Иванов", 50000, 15000)
        developer = Developer("Пётр Петров", 40000, 10, 500)
        
        # Выводим информацию о сотрудниках
        display_employee_info(manager)
        display_employee_info(developer)
        
        # Дополнительные примеры
        print("-" * 60)
        print("ДОПОЛНИТЕЛЬНЫЕ ПРИМЕРЫ:")
        print("-" * 60)
        
        senior_manager = Manager("Анна Сидорова", 80000, 30000)
        senior_developer = Developer("Мария Козлова", 60000, 5, 1000)
        
        display_employee_info(senior_manager)
        display_employee_info(senior_developer)
        
        # Демонстрация обработки ошибок
        print("-" * 60)
        print("ПРОВЕРКА ВАЛИДАЦИИ ДАННЫХ:")
        print("-" * 60)
        
        try:
            invalid_employee = Manager("", 50000, 10000)
        except ValueError as e:
            print(f"Ошибка при создании сотрудника: {e}")
        
        try:
            invalid_salary = Developer("Тест", -10000, 10, 500)
        except ValueError as e:
            print(f"Ошибка при создании сотрудника: {e}")
            
        print("=" * 60)
        print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
        print("=" * 60)
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
