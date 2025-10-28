class Product:
    """
    Класс для представления товара в онлайн-магазине.
    
    Attributes:
        product_id (int): Уникальный идентификатор товара
        name (str): Название товара
        price (float): Цена товара
        stock (int): Количество товара на складе
        category (str): Категория товара
    """
    
    def __init__(self, product_id, name, price, stock, category):
        """
        Инициализирует объект товара.
        
        Args:
            product_id (int): Уникальный идентификатор товара
            name (str): Название товара
            price (float): Цена товара
            stock (int): Количество товара на складе
            category (str): Категория товара
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category