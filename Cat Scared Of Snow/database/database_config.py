import sqlite3


def database_config():
    connection = sqlite3.connect("scores.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS scores (name TEXT, score INTEGER)")
    connection.commit()
    connection.close()
