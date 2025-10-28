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

class Customer:
    """
    Класс для представления покупателя в онлайн-магазине.
    
    Attributes:
        customer_id (int): Уникальный идентификатор покупателя
        name (str): Имя покупателя
        email (str): Email покупателя
        order_history (list): История заказов покупателя
    """
    
    def __init__(self, customer_id, name, email):
        """
        Инициализирует объект покупателя.
        
        Args:
            customer_id (int): Уникальный идентификатор покупателя
            name (str): Имя покупателя
            email (str): Email покупателя
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.order_history = []

    def add_order(self, order):
        """
        Добавляет заказ в историю заказов покупателя.
        
        Args:
            order (Order): Объект заказа для добавления
        """
        self.order_history.append(order)
