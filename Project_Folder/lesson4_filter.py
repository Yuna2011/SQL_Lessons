"""Lesson 4: Filter, sort and count rows with SQL."""

import sqlite3

connection = sqlite3.connect("school.db")

# Cursor sends SQL to SQLite and reads results back into Python.
cursor = connection.cursor()

# Pyhton value used in a parameterized query below.
year_group = 11
cursor.execute(
    "SELECT year_group, name FROM students WHERE year_group = ? ORDER BY name", (year_group,)
)

rows = cursor.fetchall()
for row in rows:
    print(row)

# COUNT(*) returns one row with one value, so fetchone()[0] gets the number.
cursor.execute("SELECT COUNT(*) FROM students")
total_students = cursor.fetchone()[0]
print("Total students:", total_students)

connection.close()