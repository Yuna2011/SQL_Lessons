# Lesson 05 Evidence Pro-Forma

## Commit evidence (minimum 2)
- Commit 1 hash + message:
Hash : 85633be
Message : Read through the notes and instructions and made my file
- Commit 2 hash + message:
- Optional Commit 3 hash + message:

## Run evidence
- Command run:
python Porject_Folder/lesson5_join.py
- Terminal output pasted below:

## Typed-work confirmation
- Briefly describe how you typed your changes step-by-step (including at least one pause to run and check output):
I kept erasing and retyping sections of the code until it worked

## Prediction before run
- JOIN query version:
cursor.execute(
    "INSERT INTO students (name, year_group) VALUES (?, ?)",
    ("Ava", 10)
)
ava_id = cursor.lastrowid

cursor.execute(
    "INSERT INTO students (name, year_group) VALUES (?, ?)",
    ("Leo", 11)
)
leo_id = cursor.lastrowid

cursor.execute(
    "INSERT INTO courses (course_name, student_id) VALUES (?, ?)",
    ("Science Club", ava_id)
)
cursor.execute(
    "INSERT INTO courses (course_name, student_id) VALUES (?, ?)",
    ("Math Team", leo_id)
)

- My prediction (student-course pairs):
("Ava", "Science Club")
("Leo", "Math Team")

- What actually happened:
('Ava', 'Science Club')
('Leo', 'Math Team')

## SQL/Python changes I made
- Change 1: Made a new team without adding a new student
- Change 2: Added a new student and a new team
- Why these changes were mine (not just starter code):
I typed them in one by one manually

## Error and fix
- Error I hit: 
It wasn't outputting at first for some reason
- How I fixed it:
I got rid of my old school.db and made the code make a new one

## Understanding check (answer in your own words)
1. Why do we use more than one table?
Makes the databade more powerful by using relational links rather than using one table for all

2. What is the purpose of `JOIN`?
It combines the data from multiple tables

3. Which columns connect your two tables?
The student id

## Quality checklist
- [✓] Script runs without unhandled errors
- [✓] I included at least 2 lesson commits
- [✓] I included joined output evidence
- [✓] I showed a prediction and compared it to actual output
- [✓] I made at least 2 personal changes to the starter work
- [✓] I answered all questions in my own words
