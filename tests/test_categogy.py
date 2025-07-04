import unittest
from src.category import Category
from src.product import Product  # Убедитесь, что у вас есть класс Product

class TestCategory(unittest.TestCase):
    def setUp(self):
        """Создаем объект категории для тестов"""
        self.category_name = "Electronics"
        self.category_description = "Electronic devices"
        self.product1 = Product(name="Laptop", price=1000, quantity=5)
        self.product2 = Product(name="Smartphone", price=500, quantity=10)
        self.category = Category(self.category_name, self.category_description, [self.product1, self.product2])

    def test_category_initialization(self):
        """Тестируем инициализацию категории"""
        self.assertEqual(self.category.name, self.category_name)
        self.assertEqual(self.category.description, self.category_description)
        self.assertEqual(len(self.category.get_product_list.splitlines()), 2)  # Проверяем количество продуктов

    def test_add_product(self):
        """Тестируем добавление нового продукта в категорию"""
        new_product = Product(name="Tablet", price=300, quantity=15)
        self.category.add_product(new_product)
        self.assertIn(new_product, self.category._Category__products)
        self.assertEqual(len(self.category.get_product_list.splitlines()), 3)

    def test_add_invalid_product(self):
        """Тестируем добавление невалидного продукта и ожидаем ошибку"""
        with self.assertRaises(TypeError):
            self.category.add_product("Not a Product instance")

    def test_get_product_list(self):
        """Тестируем получение списка продуктов"""
        expected_output = "Laptop, 1000 руб. Остаток: 5 шт.\nSmartphone, 500 руб. Остаток: 10 шт.\n"
        self.assertEqual(self.category.get_product_list, expected_output)

if __name__ == '__main__':
    unittest.main()