# Lesson 03 Evidence Pro-Forma

## Commit evidence (minimum 2)
- Commit 1 hash + message:
Hash : 9ae80d8
Message : Made my file and read through what is expected for lesson 3

- Commit 2 hash + message:
Hash : 0e3006e
Message : Finished all of my questions, the code and ticked all of the boxes.

- Optional Commit 3 hash + message:

## Run evidence
- Command run:
python Project_Folder/lesson3_select.py
- Terminal output pasted below:
Before Changes : 
(1, 'Ava', 10)
(2, 'Leo', 11)
(3, 'Mark', 12)

('Ava',)                             
('Leo',)
('Mark',)
('Bob',)

## Typed-work confirmation
- Briefly describe how you typed your changes step-by-step (including at least one pause to run and check output):
I got rid of everything except the 'Name' inside my cursor.execute and then from lesson 2, I used the cursor.execute line to insert a new student into the students table

## Prediction before run
- Query version: 
```
# Run a SELECT query to read columns from the students table.
cursor.execute("SELECT id, name, year_group FROM students")
# fetchall() returns a list of all rows from the most recent query.
rows = cursor.fetchall()
```

- My prediction (rows/columns or sample output):
1, Ava, 10
2, Leo, 11
3, Mark, 12

- What actually happened:
(1, 'Ava', 10)
(2, 'Leo', 11)
(3, 'Mark', 12)

## SQL/Python changes I made
- Change 1: I got rid of "id, , year_group" from the cursor.execute line
- Change 2: I added "cursor.execute("INSERT INTO students (name, year_group, favourite_subject) VALUES (?, ?, ?)", ("Bob", 1, "Sport"))" to add in a new student into the student table
- Why these changes were mine (not just starter code):
Because I manually erased and added them, typing it out

## Error and fix
- Error I hit: 
It wouldn't print and apparently had an error with "cursor.execute("SELECT id, name, year_group FROM students")"
- How I fixed it:
I moved my school.db out of the Created_db folder as it was in there originally

## Understanding check (answer in your own words)
1. What is the job of `SELECT`?
To read the data

2. What type of value does `fetchall()` return?
A list of all rows from the most recent query

3. How did your output change when you selected fewer columns?
It only outputed the values I requested but left a comma at the end

## Quality checklist
- [✓] Script runs without unhandled errors
- [✓] I included at least 2 lesson commits
- [✓] I included query output evidence
- [✓] I showed a prediction and compared it to actual output
- [✓] I made at least 2 personal changes to the starter work
- [✓] I answered all questions in my own words
