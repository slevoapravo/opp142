import unittest
from src.product import Product

class TestProduct(unittest.TestCase):
    def setUp(self):
        """Создаем объект продукта для тестов"""
        self.product_data = {
            "name": "Test Product",
            "description": "Test Description",
            "price": 100.0,
            "quantity": 10,
        }
        self.product = Product(**self.product_data)

    def test_new_product(self):
        """Тестируем создание нового продукта"""
        new_product = Product.new_product(self.product_data)
        self.assertIsInstance(new_product, Product)
        self.assertEqual(new_product.name, self.product_data["name"])
        self.assertEqual(new_product.description, self.product_data["description"])
        self.assertEqual(new_product.price, self.product_data["price"])
        self.assertEqual(new_product.quantity, self.product_data["quantity"])

    def test_price_setter_valid(self):
        """Тестируем установку корректной цены"""
        self.product.price = 150.0
        self.assertEqual(self.product.price, 150.0)

    def test_price_setter_negative(self):
        """Тестируем установку отрицательной цены и ожидаем ошибку"""
        with self.assertRaises(ValueError):
            self.product.price = -50

    def test_price_setter_zero(self):
        """Тестируем установку цены в ноль и ожидаем ошибку"""
        with self.assertRaises(ValueError):
            self.product.price = 0

    def test_price_setter_negative_after_zero(self):
        """Тестируем установку отрицательной цены после правильной цены"""
        self.product.price = 200
        self.assertEqual(self.product.price, 200)
        with self.assertRaises(ValueError):
            self.product.price = -100

if __name__ == '__main__':
    unittest.main()