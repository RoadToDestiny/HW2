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

class Order:
    """
    Класс для представления заказа в онлайн-магазине.
    
    Attributes:
        order_id (int): Уникальный идентификатор заказа
        customer (Customer): Покупатель, сделавший заказ
        items (dict): Товары в заказе
        total_price (float): Итоговая стоимость заказа
        tax_rate (float): Ставка налога
        discount (float): Размер скидки (в долях от 1)
    """
    
    def __init__(self, order_id, customer, cart):
        """
        Инициализирует объект заказа.
        
        Args:
            order_id (int): Уникальный идентификатор заказа
            customer (Customer): Покупатель, сделавший заказ
            cart (ShoppingCart): Корзина с товарами для заказа
        """
        self.order_id = order_id
        self.customer = customer
        self.items = cart.items.copy()
        self.total_price = 0
        self.tax_rate = 0.1
        self.discount = 0

    def calculate_total(self):
        """
        Рассчитывает итоговую стоимость заказа с учетом скидок и налогов.
        
        Returns:
            float: Итоговая стоимость заказа
        """
        subtotal = 0
        for item in self.items.values():
            subtotal += item['product'].price * item['quantity']
        
        discount_amount = subtotal * self.discount
        taxed_amount = (subtotal - discount_amount) * self.tax_rate
        self.total_price = subtotal - discount_amount + taxed_amount
        return self.total_price

    def set_discount(self, discount_percent):
        """
        Устанавливает скидку на заказ.
        
        Args:
            discount_percent (float): Процент скидки (от 0 до 100)
        """
        self.discount = discount_percent / 100

    def process_order(self):
        """
        Обрабатывает заказ: проверяет наличие товаров, обновляет склад,
        рассчитывает стоимость и добавляет заказ в историю покупателя.
        
        Returns:
            bool: True если заказ успешно обработан
        
        Raises:
            Exception: Если товара недостаточно на складе
        """
        for product_id, item in self.items.items():
            product = item['product']
            quantity = item['quantity']
            if product.stock >= quantity:
                product.stock -= quantity
            else:
                raise Exception(f"Недостаточно товара {product.name} на складе")
        
        self.calculate_total()
        self.customer.add_order(self)
        return True

# Демонстрация работы

# Создание товаров
product1 = Product(1, "Ноутбук", 50000, 10, "Электроника")
product2 = Product(2, "Мышь", 1500, 25, "Электроника")
product3 = Product(3, "Книга", 500, 50, "Книги")

# Создание покупателя
customer = Customer(1, "Иван Иванов", "ivan@mail.ru")

# Работа с корзиной
cart = ShoppingCart()
cart.add_product(product1)
cart.add_product(product2, 2)
cart.add_product(product3)

print(f"Товары в корзине: {len(cart.items)}")
print(f"Общая стоимость корзины: {cart.get_total_price()} руб.")

# Оформление заказа
order = Order(1, customer, cart)
order.set_discount(10)
order.process_order()

print(f"Итоговая стоимость заказа: {order.total_price:.2f} руб.")
print(f"История заказов клиента: {len(customer.order_history)} заказ(ов)")
print(f"Остаток ноутбуков на складе: {product1.stock}")