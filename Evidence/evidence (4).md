# Lesson 04 Evidence Pro-Forma

## Commit evidence (minimum 2)
- Commit 1 hash + message:
Hash : 678a5b3
Message : I made my file and read through the theory
- Commit 2 hash + message:
Hash :
Message : 
- Optional Commit 3 hash + message:

## Run evidence
- Command run:
python Project_Folder/lesson4_filter.py
- Terminal output pasted below:
('Ava', 10)
Total students: 3

## Typed-work confirmation
- Briefly describe how you typed your changes step-by-step (including at least one pause to run and check output):
I first got rid of the 'year_group,' and ran it to make sure it worked and then put it back and switched its order with 'name'. Then I tested it again to make sure it worked

## Prediction before run
- Query version:
```
cursor.execute("SELECT COUNT(*) FROM students")
total_students = cursor.fetchone()[0]
print("Total students:", total_students)
```

- My prediction (filtered rows, order, or count):
('Ava', 10)
Total students : 1

- What actually happened:
('Ava', 10)
Total students: 3

## SQL/Python changes I made
- Change 1: 
I got rid of 'year_group,'
- Change 2: 
I switched the order between 'year_group,' and 'name' and added a comma after 'name'
- Why these changes were mine (not just starter code):
I manually erased, added and rearranged the code

## Error and fix
- Error I hit: 
When trying to make it output only one column it would show a '(year_group,) error
- How I fixed it:
I put whatvever I got rid of back and then erased 'year_group,'

## Understanding check (answer in your own words)
1. What does `WHERE` do?
It filters the rows in the table
2. Why is `?` used in the query?
Works as a placeholder for the values
3. What does `COUNT(*)` tell you in this lesson?
The matching number of rows

## Quality checklist
- [✓] Script runs without unhandled errors
- [✓] I included at least 2 lesson commits
- [✓] I included filtered/sorted summary evidence
- [✓] I showed a prediction and compared it to actual output
- [✓] I made at least 2 personal changes to the starter work
- [✓] I answered all questions in my own words
