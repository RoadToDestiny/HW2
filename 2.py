from typing import Dict, List


class Vehicle:
    """
    Класс для представления транспортного средства.

    Attributes:
        brand (str): Марка транспортного средства
        model (str): Модель транспортного средства
        year (int): Год выпуска
        max_speed (float): Максимальная скорость (км/ч)
        fuel_type (str): Тип топлива
    """

    def __init__(self, brand: str, model: str, year: int,
                 max_speed: float, fuel_type: str) -> None:
        """
        Инициализирует объект транспортного средства.

        Args:
            brand (str): Марка транспортного средства
            model (str): Модель транспортного средства
            year (int): Год выпуска
            max_speed (float): Максимальная скорость (км/ч)
            fuel_type (str): Тип топлива
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.fuel_type = fuel_type

    def get_description(self) -> str:
        """
        Возвращает описание транспортного средства.

        Returns:
            str: Описание транспортного средства
        """
        return (f"{self.brand} {self.model} ({self.year}), "
                f"Макс. скорость: {self.max_speed} км/ч, "
                f"Топливо: {self.fuel_type}")

    def start_engine(self) -> str:
        """
        Запускает двигатель транспортного средства.

        Returns:
            str: Сообщение о запуске двигателя
        """
        return "Двигатель запущен"


class Car(Vehicle):
    """
    Класс для представления автомобиля.

    Attributes:
        brand (str): Марка автомобиля
        model (str): Модель автомобиля
        year (int): Год выпуска
        max_speed (float): Максимальная скорость (км/ч)
        fuel_type (str): Тип топлива
        doors (int): Количество дверей
        body_type (str): Тип кузова
        trunk_capacity (float): Объем багажника (литры)
    """

    def __init__(self, brand: str, model: str, year: int,
                 max_speed: float, fuel_type: str, doors: int,
                 body_type: str, trunk_capacity: float) -> None:
        """
        Инициализирует объект автомобиля.

        Args:
            brand (str): Марка автомобиля
            model (str): Модель автомобиля
            year (int): Год выпуска
            max_speed (float): Максимальная скорость (км/ч)
            fuel_type (str): Тип топлива
            doors (int): Количество дверей
            body_type (str): Тип кузова
            trunk_capacity (float): Объем багажника (литры)
        """
        super().__init__(brand, model, year, max_speed, fuel_type)
        self.doors = doors
        self.body_type = body_type
        self.trunk_capacity = trunk_capacity

    def get_description(self) -> str:
        """
        Возвращает описание автомобиля.

        Returns:
            str: Описание автомобиля
        """
        base_description = super().get_description()
        return (f"Автомобиль: {base_description}, "
                f"Двери: {self.doors}, Кузов: {self.body_type}, "
                f"Багажник: {self.trunk_capacity} л")

    def start_engine(self) -> str:
        """
        Запускает двигатель автомобиля.

        Returns:
            str: Сообщение о запуске двигателя автомобиля
        """
        return ("Двигатель автомобиля запущен с помощью ключа "
                "или кнопки")


class Motorcycle(Vehicle):
    """
    Класс для представления мотоцикла.

    Attributes:
        brand (str): Марка мотоцикла
        model (str): Модель мотоцикла
        year (int): Год выпуска
        max_speed (float): Максимальная скорость (км/ч)
        fuel_type (str): Тип топлива
        engine_cc (int): Объем двигателя (куб. см)
        bike_type (str): Тип мотоцикла
        has_sidecar (bool): Наличие бокового прицепа
    """

    def __init__(self, brand: str, model: str, year: int,
                 max_speed: float, fuel_type: str, engine_cc: int,
                 bike_type: str, has_sidecar: bool = False) -> None:
        """
        Инициализирует объект мотоцикла.

        Args:
            brand (str): Марка мотоцикла
            model (str): Модель мотоцикла
            year (int): Год выпуска
            max_speed (float): Максимальная скорость (км/ч)
            fuel_type (str): Тип топлива
            engine_cc (int): Объем двигателя (куб. см)
            bike_type (str): Тип мотоцикла
            has_sidecar (bool): Наличие бокового прицепа
        """
        super().__init__(brand, model, year, max_speed, fuel_type)
        self.engine_cc = engine_cc
        self.bike_type = bike_type
        self.has_sidecar = has_sidecar

    def get_description(self) -> str:
        """
        Возвращает описание мотоцикла.

        Returns:
            str: Описание мотоцикла
        """
        base_description = super().get_description()
        sidecar_info = "с коляской" if self.has_sidecar else "без коляски"
        return (f"Мотоцикл: {base_description}, "
                f"Объем: {self.engine_cc} см³, Тип: {self.bike_type}, "
                f"{sidecar_info}")

    def start_engine(self) -> str:
        """
        Запускает двигатель мотоцикла.

        Returns:
            str: Сообщение о запуске двигателя мотоцикла
        """
        return ("Двигатель мотоцикла запущен с помощью "
                "кик-стартера или кнопки")


class Truck(Vehicle):
    """
    Класс для представления грузовика.

    Attributes:
        brand (str): Марка грузовика
        model (str): Модель грузовика
        year (int): Год выпуска
        max_speed (float): Максимальная скорость (км/ч)
        fuel_type (str): Тип топлива
        cargo_capacity (float): Грузоподъемность (тонны)
        axle_count (int): Количество осей
        trailer_type (str): Тип прицепа
    """

    def __init__(self, brand: str, model: str, year: int,
                 max_speed: float, fuel_type: str,
                 cargo_capacity: float, axle_count: int,
                 trailer_type: str) -> None:
        """
        Инициализирует объект грузовика.

        Args:
            brand (str): Марка грузовика
            model (str): Модель грузовика
            year (int): Год выпуска
            max_speed (float): Максимальная скорость (км/ч)
            fuel_type (str): Тип топлива
            cargo_capacity (float): Грузоподъемность (тонны)
            axle_count (int): Количество осей
            trailer_type (str): Тип прицепа
        """
        super().__init__(brand, model, year, max_speed, fuel_type)
        self.cargo_capacity = cargo_capacity
        self.axle_count = axle_count
        self.trailer_type = trailer_type

    def get_description(self) -> str:
        """
        Возвращает описание грузовика.

        Returns:
            str: Описание грузовика
        """
        base_description = super().get_description()
        return (f"Грузовик: {base_description}, "
                f"Грузоподъемность: {self.cargo_capacity} т, "
                f"Оси: {self.axle_count}, Прицеп: {self.trailer_type}")

    def start_engine(self) -> str:
        """
        Запускает двигатель грузовика.

        Returns:
            str: Сообщение о запуске двигателя грузовика
        """
        return ("Двигатель грузовика запущен, требуется прогрев "
                "перед началом движения")


class Bus(Vehicle):
    """
    Класс для представления автобуса.

    Attributes:
        brand (str): Марка автобуса
        model (str): Модель автобуса
        year (int): Год выпуска
        max_speed (float): Максимальная скорость (км/ч)
        fuel_type (str): Тип топлива
        passenger_capacity (int): Вместимость пассажиров
        bus_type (str): Тип автобуса
        has_air_conditioning (bool): Наличие кондиционера
    """

    def __init__(self, brand: str, model: str, year: int,
                 max_speed: float, fuel_type: str,
                 passenger_capacity: int, bus_type: str,
                 has_air_conditioning: bool) -> None:
        """
        Инициализирует объект автобуса.

        Args:
            brand (str): Марка автобуса
            model (str): Модель автобуса
            year (int): Год выпуска
            max_speed (float): Максимальная скорость (км/ч)
            fuel_type (str): Тип топлива
            passenger_capacity (int): Вместимость пассажиров
            bus_type (str): Тип автобуса
            has_air_conditioning (bool): Наличие кондиционера
        """
        super().__init__(brand, model, year, max_speed, fuel_type)
        self.passenger_capacity = passenger_capacity
        self.bus_type = bus_type
        self.has_air_conditioning = has_air_conditioning

    def get_description(self) -> str:
        """
        Возвращает описание автобуса.

        Returns:
            str: Описание автобуса
        """
        base_description = super().get_description()
        ac_info = ("с кондиционером" if self.has_air_conditioning
                   else "без кондиционера")
        return (f"Автобус: {base_description}, "
                f"Вместимость: {self.passenger_capacity} пасс., "
                f"Тип: {self.bus_type}, {ac_info}")

    def start_engine(self) -> str:
        """
        Запускает двигатель автобуса.

        Returns:
            str: Сообщение о запуске двигателя автобуса
        """
        return ("Двигатель автобуса запущен, "
                "проверка систем завершена")


# Демонстрация работы и полиморфизма

# Создание объектов различных транспортных средств
print("=== СОЗДАНИЕ ТРАНСПОРТНЫХ СРЕДСТВ ===")

car1 = Car("Toyota", "Camry", 2022, 220, "Бензин", 4, "Седан", 480)
motorcycle1 = Motorcycle("Harley-Davidson", "Sportster", 2021,
                         180, "Бензин", 1200, "Круизер", False)
truck1 = Truck("Volvo", "FH16", 2020, 120, "Дизель",
               25, 3, "Рефрижератор")
bus1 = Bus("Mercedes-Benz", "Sprinter", 2023, 140, "Дизель",
           20, "Микроавтобус", True)

# Создаем список всех транспортных средств
vehicles: List[Vehicle] = [car1, motorcycle1, truck1, bus1]

# Демонстрация полиморфизма: вызов метода get_description()
print("\n=== ПОЛИМОРФИЗМ: ВЫЗОВ МЕТОДА get_description() ===")
for i, vehicle in enumerate(vehicles, 1):
    print(f"{i}. {vehicle.get_description()}")

# Демонстрация полиморфизма: вызов метода start_engine()
print("\n=== ПОЛИМОРФИЗМ: ВЫЗОВ МЕТОДА start_engine() ===")
for i, vehicle in enumerate(vehicles, 1):
    print(f"{i}. {vehicle.start_engine()}")

# Создание дополнительных объектов для демонстрации
print("\n=== ДОПОЛНИТЕЛЬНЫЕ ТРАНСПОРТНЫЕ СРЕДСТВА ===")

car2 = Car("Tesla", "Model S", 2023, 250, "Электричество",
           4, "Седан", 793)
motorcycle2 = Motorcycle("Honda", "CBR600RR", 2022, 240,
                         "Бензин", 599, "Спортивный", False)
truck2 = Truck("MAN", "TGX", 2021, 110, "Дизель",
               18, 2, "Тентованный")
bus2 = Bus("ЛиАЗ", "5292", 2020, 90, "Газ",
           85, "Городской", False)

# Список всех транспортных средств
all_vehicles: List[Vehicle] = [car1, car2, motorcycle1, motorcycle2,
                               truck1, truck2, bus1, bus2]

# Группировка по типам транспортных средств
print("\n=== ГРУППИРОВКА ТРАНСПОРТНЫХ СРЕДСТВ ПО ТИПАМ ===")

vehicle_types: Dict[str, List[Vehicle]] = {
    "Автомобили": [v for v in all_vehicles if isinstance(v, Car)],
    "Мотоциклы": [v for v in all_vehicles if isinstance(v, Motorcycle)],
    "Грузовики": [v for v in all_vehicles if isinstance(v, Truck)],
    "Автобусы": [v for v in all_vehicles if isinstance(v, Bus)]
}

for vehicle_type, vehicles_list in vehicle_types.items():
    print(f"\n{vehicle_type} ({len(vehicles_list)} шт.):")
    for vehicle in vehicles_list:
        print(f"  - {vehicle.get_description()}")

# Демонстрация работы с отдельными объектами
print("\n=== ДЕТАЛЬНАЯ ИНФОРМАЦИЯ О ТРАНСПОРТНЫХ СРЕДСТВАХ ===")

print("1. Автомобиль:")
print(f"   {car1.get_description()}")
print(f"   {car1.start_engine()}")

print("\n2. Мотоцикл:")
print(f"   {motorcycle1.get_description()}")
print(f"   {motorcycle1.start_engine()}")

print("\n3. Грузовик:")
print(f"   {truck1.get_description()}")
print(f"   {truck1.start_engine()}")

print("\n4. Автобус:")
print(f"   {bus1.get_description()}")
print(f"   {bus1.start_engine()}")

# Подсчет общего количества транспортных средств
print("\n=== СВОДНАЯ ИНФОРМАЦИЯ ===")
print(f"Всего транспортных средств: {len(all_vehicles)}")
for vehicle_type, vehicles_list in vehicle_types.items():
    print(f"{vehicle_type}: {len(vehicles_list)}")
