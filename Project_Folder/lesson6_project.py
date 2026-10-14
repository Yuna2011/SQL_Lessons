"""Lesson 6: Build a small books database script."""

import sqlite3

connection = sqlite3.connect("school.db")
# Cursor executes SQL commands and reads query results.
cursor = connection.cursor()

# Create the books table once, then reuse it on later runs.
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL
)
""")

# Reset demo data so lesson output says consistent.
cursor.execute("DELETE FROM books")

# Add sample book records.
cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("HOLES", "Louis Sachar"))
cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("Wonder", "R. J. Palacio"))
cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("The Hobbit", "J. R. R. Tolkien"))
cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("BOB", "Bobby Bob"))
cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("Bobbify", "Bobbify Bobby"))
# Query all books in alphabetical order by title.
cursor.execute("SELECT title, author FROM books ORDER BY title")

while True:
    book = input("""Menu :
1. Add a book
2. View all books
3. Exit
Please choose an option (1-3): """)
    print()

    if book == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
        connection.commit()
        print(f"Added book: {title} by {author}")
        print()
    elif book == "2":
        # fetchall() gives a list of (title, author) tuples to loop through.
        for title, author in cursor.fetchall():
            print(f"{title} by {author}")
            print()
    elif book == "3":
        break

# Commit saves inserted rows to the database file.
connection.commit()
connection.close()