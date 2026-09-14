"""Lesson 1: Connect to a SQLite database file."""

import sqlite3

print("It's gonna open")
# Open a connection to school.db (SQLite creates the file if needed)
connection = sqlite3.connect("library.db")
print("Database connected!")

# Close the connection so the file is safely released
connection.close()
print("Database closed!")