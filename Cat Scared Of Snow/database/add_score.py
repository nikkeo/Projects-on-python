import sqlite3


def add_score(name, score):
    connection = sqlite3.connect("scores.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO scores (name, score) VALUES (?, ?)", (name, score))
    connection.commit()
    connection.close()