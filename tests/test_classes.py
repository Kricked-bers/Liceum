import pytest

from src.classes import Category, Product  # Замените your_module на имя вашего модуля


class TestProduct:
    def test_product_creation(self):
        """Тест создания продукта и проверки его атрибутов"""
        product = Product("Ноутбук", "Мощный игровой ноутбук", 1500.00, 10)

        assert product.name == "Ноутбук"
        assert product.description == "Мощный игровой ноутбук"
        assert product.price == 1500.00
        assert product.quantity == 10

    def test_product_default_values(self):
        """Тест создания продукта с разными значениями"""
        product = Product("Мышь", "Беспроводная мышь", 25.50, 50)

        assert product.name == "Мышь"
        assert product.description == "Беспроводная мышь"
        assert product.price == 25.50
        assert product.quantity == 50


class TestCategory:
    def test_category_creation(self):
        """Тест создания категории и проверки ее атрибутов"""
        # Сбросим счетчики перед тестом
        Category.category_count = 0
        Category.product_count = 0

        product = Product("Ноутбук", "Мощный игровой ноутбук", 1500.00, 10)
        category = Category("Электроника", "Электронные устройства", [product])

        assert category.name == "Электроника"
        assert category.description == "Электронные устройства"
        assert len(category.products) == 1
        assert category.products[0].name == "Ноутбук"

    def test_category_counters(self):
        """Тест обновления счетчиков категорий и продуктов"""
        # Сбросим счетчики перед тестом
        Category.category_count = 0
        Category.product_count = 0

        # Создаем несколько продуктов и категорий
        product1 = Product("Ноутбук", "Мощный игровой ноутбук", 1500.00, 10)
        product2 = Product("Мышь", "Беспроводная мышь", 25.50, 50)

        category1 = Category("Электроника", "Электронные устройства", [product1, product2])

        # Проверяем счетчики после создания первой категории
        assert Category.category_count == 1
        assert Category.product_count == 2

        # Создаем еще одну категорию
        product3 = Product("Книга", "Программирование на Python", 35.00, 20)
        category2 = Category("Книги", "Книги и учебники", [product3])

        # Проверяем счетчики после создания второй категории
        assert Category.category_count == 2
        assert Category.product_count == 3

    def test_empty_category(self):
        """Тест создания категории без продуктов"""
        # Сбросим счетчики перед тестом
        Category.categories_count = 0
        Category.product_count = 0

        category = Category("Пустая категория", "Нет продуктов", [])

        assert category.name == "Пустая категория"
        assert category.description == "Нет продуктов"
        assert len(category.products) == 0
        assert Category.categories_count == 0
        assert Category.product_count == 0  # Продуктов нет, поэтому счетчик не увеличился


# Запуск тестов
if __name__ == "__main__":
    pytest.main([__file__, "-v"])