import sqlite3

# устанавливаем соединение с базой данных
connection = sqlite3.connect("C:/Users/aykerime2404/Downloads/sqlite/tutorial.db")

# создаем "курсор" для выполнения запросов
cursor = connection.cursor()

# создаем таблицу, если её нет
cursor.execute("CREATE TABLE IF NOT EXISTS countries("
               "id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "country TEXT,"
               "capital TEXT)")


class Country:
    def __init__(self, country, capital):
        self.country = country
        self.capital = capital

    @staticmethod
    def add_table(country, capital):
        # Вставляем данные в таблицу
        cursor.execute("INSERT INTO countries (country, capital) VALUES (?, ?)", (country, capital))
        connection.commit()  # Сохраняем изменения в базе данных

    @staticmethod
    def edit_table(country, capital, olddata):
        # Обновляем данные в таблице по capital
        cursor.execute("UPDATE countries SET country = ?, capital = ? WHERE capital = ?", (country, capital, olddata,))
        connection.commit()  # Сохраняем изменения

    @staticmethod
    def read_table():
        # Чтение всех записей из таблицы
        cursor.execute("SELECT * FROM countries")
        rows = cursor.fetchall()

        if rows:
            print("\nСодержимое таблицы:")
            columns = [description[0] for description in cursor.description]
            print(" | ".join(columns))
            print("_" * 40)
            for row in rows:
                print(" | ".join(str(r) for r in row))
        else:
            print("\nТаблица пуста.")

    @staticmethod
    def delete_table(capital):
        # Удаление записи по id
        cursor.execute("DELETE FROM countries WHERE capital = ?", (capital,))
        connection.commit()  # Сохраняем изменения


# Country.add_table("Germany", "Berlin")
# Country.add_table("Kazakhstan", "Astana")
Country.add_table("France", "Paris")
# Country.read_table()
# Country.edit_table("Great Britain", "London", "Berlin")
Country.read_table()
# Country.delete_table("Astana")
# Country.read_table()
