import sqlite3

# Connect to SQLite
connection = sqlite3.connect('student.db')

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Create the table if it doesn't already exist
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME TEXT,
    CLASS TEXT,
    SECTION TEXT,
    MARKS INT
);
"""
cursor.execute(table_info)
# Insert records into the STUDENT table
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Samruddhi', 'Data Science', 'A', 100)''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Aishwarya', 'Machine Learning', 'B', 85)''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Harshada', 'Computer Science', 'A', 88)''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Vaishnavi', 'Data Science', 'B', 95)''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Neha', 'Computer Science', 'A', 79)''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Priya', 'Machine Learning', 'B', 90)''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Madhavi', 'Computer Science', 'A', 92)''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES (' Pratiksha', 'Data Science', 'C', 89)''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Sneha', 'Machine Learning', 'A', 87)''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Pooja', 'Computer Science', 'B', 93)''')

# Display all the records
print('The inserted records are:')
data = cursor.execute('''SELECT * FROM STUDENT''')

for row in data:
    print(row)

# Commit the changes and close the connection
connection.commit()
connection.close()
