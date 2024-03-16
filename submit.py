#!/usr/bin/env python3

import cgi
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('userdata.db')
cursor = conn.cursor()

# Retrieve form data
form = cgi.FieldStorage()
name = form.getvalue('name')
email = form.getvalue('email')
age = form.getvalue('age')
dob = form.getvalue('dob')

# Validate email format
def is_valid_email(email):
    return '@' in email and '.' in email

# Validate age
def is_valid_age(age):
    try:
        age = int(age)
        return age > 0
    except ValueError:
        return False

# Handle form submission
if name and email and age and dob:
    if is_valid_email(email) and is_valid_age(age):
        # Insert data into the database
        cursor.execute("INSERT INTO users (name, email, age, dob) VALUES (?, ?, ?, ?)", (name, email, age, dob))
        conn.commit()
        conn.close()
        print("Content-Type: text/html")
        print("Location: index.html?success=true\n\n")
    else:
        print("Content-Type: text/html\n\n")
        print("<h2>Error: Invalid email format or age</h2>")
else:
    print("Content-Type: text/html\n\n")
    print("<h2>Error: Please fill in all fields</h2>")
