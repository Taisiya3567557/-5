import pandas as pd
from tabulate import tabulate

db = pd.DataFrame([
    {
        "item": "Ноутбук Asus",
        "category": "Электроника",
        "quantity": 12,
        "price": 55000,
        "supplier_name": "ООО ТехноПлюс",
        "supplier_country": "Россия",
        "arrival_date": "2023-10-01"
    },
    {
        "item": "Смартфон Samsung",
        "category": "Электроника",
        "quantity": 8,
        "price": 35000,
        "supplier_name": "ООО Связь",
        "supplier_country": "Россия",
        "arrival_date": "2023-09-15"
    },
    {
        "item": "Клавиатура Logitech",
        "category": "Компьютерные аксессуары",
        "quantity": 0,
        "price": 2500,
        "supplier_name": "ООО ТехноПлюс",
        "supplier_country": "Россия",
        "arrival_date": "2023-10-05"
    },
    {
        "item": "Монитор Dell",
        "category": "Электроника",
        "quantity": 5,
        "price": 18000,
        "supplier_name": "ООО МониторСервис",
        "supplier_country": "Россия",
        "arrival_date": "2023-09-20"
    },
])

def print_table(df, title=""):
    if title:
        print(f"\n{title}")
    print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))

def find_items_quantity_less_than_10(db):
    result = db[db['quantity'] < 10][['item', 'category', 'quantity', 'price']]
    print_table(result, "Товары с количеством меньше 10:")
    return result

def average_price_per_category(db):
    avg_price = db.groupby('category')['price'].mean().reset_index()
    print_table(avg_price, "Средняя цена по каждой категории:")
    return avg_price

def increase_price_electronics(db):
    db.loc[db['category'] == 'Электроника', 'price'] = db.loc[db['category'] == 'Электроника', 'price'] * 1.1
    print_table(db[['item', 'category', 'price']], "Цены товаров после увеличения на 10% в категории 'Электроника':")
    return db

def delete_items_no_quantity(db):
    db = db[db['quantity'] != 0]
    print_table(db[['item', 'quantity']], "Товары, у которых quantity != 0:")
    return db

if __name__ == "__main__":
    print_table(db, "Исходная таблица db:")
    find_items_quantity_less_than_10(db)
    average_price_per_category(db)
    db = increase_price_electronics(db)
    db = delete_items_no_quantity(db)
    print_table(db, "Итоговая таблица db после всех операций:")
