import sqlite3
import os
class DataBase:
    def __init__(self) -> None:
        self.path = os.getcwd() + r'/documents/database.db'

    def add_user(self, tele_user_id):
        connection = sqlite3.connect(self.path)
        cursor = connection.cursor()
        cursor.execute('INSERT INTO Users (tele_id, class) VALUES (?, ?)', (tele_user_id, None))
        connection.commit()
        connection.close()

    def change_group(self, tele_user_id, class_name):
        connection = sqlite3.connect(self.path)
        cursor = connection.cursor()
        cursor.execute(f'UPDATE Users SET class = ? WHERE tele_id = ?', (class_name, tele_user_id))
        connection.commit()
        connection.close()

    def get_group(self, tele_user_id):
        connection = sqlite3.connect(self.path)
        cursor = connection.cursor()
        cursor.execute('SELECT class FROM Users WHERE tele_id = ?', (tele_user_id, ))
        
        group_name = cursor.fetchone()[0]
        connection.commit()
        connection.close()
        return group_name
    
    def get_all_users(self):
        connection = sqlite3.connect(self.path)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Users')
        users = cursor.fetchall()
        connection.commit()
        connection.close()
        return users
        