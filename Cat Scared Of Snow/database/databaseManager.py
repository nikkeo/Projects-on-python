import sqlite3


class databaseManager:
    def __init__(self, database_name="scores.db"):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS scores (name TEXT, score INTEGER)")
        self.connection.commit()

    def add_score(self, name, score):
        self.cursor.execute("INSERT INTO scores (name, score) VALUES (?, ?)", (name, score))
        self.connection.commit()

    def get_top_players(self, limit=5):
        self.cursor.execute("SELECT * FROM scores ORDER BY score DESC LIMIT ?", (limit,))
        top_players = self.cursor.fetchall()
        return top_players

    def close_connection(self):
        self.connection.close()