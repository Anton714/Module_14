import sqlite3

def initiate_db():
    connection = sqlite3.connect('pr_db.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    price INT NOT NULL
    )
    ''')

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('pr_db.db')
    cursor = connection.cursor()

    cursor.execute("SELECT title, description, price FROM Products")
    return cursor.fetchall()


    connection.commit()
    connection.close()
    return users
