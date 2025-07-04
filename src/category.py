
from typing import Any
from src.product import Product

class Category:
    """Категория товара"""

    category_count = 0
    product_count = 0

    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products if isinstance(products, list) else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: dict):
        """Метод добавления нового продукта в список"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError(f"Expected an instance of Product, got {type(product).__name__} instead.")

    @property
    def get_product_list(self) -> str:
        product_list = ""
        for product in self.__products:
            product_list += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_list


result = Category("Product", "Description", ["product1", "product2", "product3"])
print(result)
