"""Lesson 3: Query students with SELECT and print the results."""

import sqlite3

connection = sqlite3.connect("school.db")
# The cursor runs SQL queries and returns their results to Python.
cursor = connection.cursor()

cursor.execute("INSERT INTO students (name, year_group, favourite_subject) VALUES (?, ?, ?)", ("Bob", 1, "Sport"))

# Run a SELECT query to read columns from the students table.
cursor.execute("SELECT name FROM students")
# fetchall() returns a list of all rows from the most recent query.
rows = cursor.fetchall()

# Each row is a tuple like (id, name, year_group).
for row in rows:
    print(row)

# Close the connection when all reading is complete.
connection.close()