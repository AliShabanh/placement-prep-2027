import sqlite3


DATABASE_NAME = "placement.db"


def connect_to_database():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def row_to_dict(row):
    return dict(row)


def rows_to_dicts(rows):
    return [row_to_dict(row) for row in rows]