class Category:
    # Атрибуты класса
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        # Атрибуты экземпляра
        self.name = name
        self.description = description
        self.products = products

        # Обновляем атрибуты класса
        Category.category_count += 1
        Category.product_count += len(products)


class Product:
    def __init__(self, name, description, price, quantity):
        # Атрибуты экземпляра
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
