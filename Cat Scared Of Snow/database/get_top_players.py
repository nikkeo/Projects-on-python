import sqlite3


def get_top_players():
    connection = sqlite3.connect("scores.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM scores ORDER BY score DESC LIMIT 5")
    top_players = cursor.fetchall()
    connection.close()
    return top_players
