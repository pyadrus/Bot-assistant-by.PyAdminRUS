import sqlite3


# Определение функции для операций с базой данных
def perform_database_operations(user_id, username, timestamp, file_name):
    conn = sqlite3.connect('settings/database.db')
    cursor = conn.cursor()
    # Создайте таблицу, если она не существует
    cursor.execute("""CREATE TABLE IF NOT EXISTS user_requests (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER,
                                                                username TEXT, timestamp TEXT, file_name TEXT)""")
    # Вставка записи в таблицу
    cursor.execute("""INSERT INTO user_requests (user_id, username, timestamp, file_name) 
                      VALUES (?, ?, ?, ?)""", (user_id, username, timestamp, file_name))
    # Зафиксируйте изменения в базе данных
    conn.commit()
    conn.close()
