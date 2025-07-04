from src.category import Category
from src.product import Product

if __name__ == "__main__":
    # Создаем продукты
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создаем категорию и добавляем продукты в нее
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    # Выводим список продуктов в категории
    print("Список продуктов в категории:")
    print(category1.get_product_list)

    # Добавляем новый продукт в категорию
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)

    # Выводим обновленный список продуктов
    print("Обновленный список продуктов в категории:")
    print(category1.get_product_list)

    # Выводим общее количество продуктов в категории
    print("Общее количество продуктов в категории:", Category.product_count)

    # Создаем новый продукт из словаря
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )

    # Выводим информацию о новом продукте
    print(f"Создан новый продукт: {new_product.name}, {new_product.description}, {new_product.price}, Остаток: {new_product.quantity}")

    # Изменяем цену нового продукта и выводим ее
    try:
        new_product.price = 800
        print("Новая цена продукта:", new_product.price)

        # Пытаемся установить отрицательную цену
        new_product.price = -100
    except ValueError as e:
        print(e)

    # Пытаемся установить цену в 0
    try:
        new_product.price = 0
    except ValueError as e:
        print(e)

    # Проверка на установку корректной цены после ошибки
    new_product.price = 1500
    print("Переприсвоенная цена продукта:", new_product.price)