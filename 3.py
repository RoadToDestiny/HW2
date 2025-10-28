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

class ShoppingCart:
    """
    Класс для представления корзины покупок.
    
    Attributes:
        items (dict): Словарь товаров в корзине
    """
    
    def __init__(self):
        """Инициализирует пустую корзину покупок."""
        self.items = {}

    def add_product(self, product, quantity=1):
        """
        Добавляет товар в корзину.
        
        Args:
            product (Product): Объект товара для добавления
            quantity (int, optional): Количество товара. По умолчанию 1
        """
        if product.product_id in self.items:
            self.items[product.product_id]['quantity'] += quantity
        else:
            self.items[product.product_id] = {
                'product': product,
                'quantity': quantity
            }

    def remove_product(self, product_id):
        """
        Удаляет товар из корзины.
        
        Args:
            product_id (int): Идентификатор товара для удаления
        """
        if product_id in self.items:
            del self.items[product_id]

    def update_quantity(self, product_id, quantity):
        """
        Обновляет количество товара в корзине.
        
        Args:
            product_id (int): Идентификатор товара
            quantity (int): Новое количество товара
        """
        if product_id in self.items:
            if quantity <= 0:
                self.remove_product(product_id)
            else:
                self.items[product_id]['quantity'] = quantity

    def clear(self):
        """Очищает корзину от всех товаров."""
        self.items.clear()

    def get_total_price(self):
        """
        Рассчитывает общую стоимость товаров в корзине.
        
        Returns:
            float: Общая стоимость товаров в корзине
        """
        total = 0
        for item in self.items.values():
            total += item['product'].price * item['quantity']
        return total