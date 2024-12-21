import sqlite3


def initiate_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    # Создание таблицы Products
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                        id INTEGER PRIMARY KEY,
                        title TEXT NOT NULL,
                        description TEXT,
                        price INTEGER NOT NULL
                    )''')
    # Создание таблицы Users
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                        id INTEGER PRIMARY KEY,
                        username TEXT NOT NULL,
                        email TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        balance INTEGER NOT NULL DEFAULT 1000
                    )''')
    conn.commit()
    conn.close()


def fill_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Products')
    if cursor.fetchone()[0] == 0:
        products = [
            ('Product 1', 'Описание 1', 100),
            ('Product 2', 'Описание 2', 200),
            ('Product 3', 'Описание 3', 300),
            ('Product 4', 'Описание 4', 400)
        ]
        cursor.executemany('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', products)
        conn.commit()
    conn.close()


def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    conn.close()
    return products


def add_user(username, email, age):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, 1000)''',
                   (username, email, age))
    conn.commit()
    conn.close()


def is_included(username):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM Users WHERE username = ?', (username,))
    result = cursor.fetchone()
    conn.close()
    return result is not None
