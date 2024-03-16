#!/usr/bin/env python3

import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('userdata.db')
cursor = conn.cursor()

# Retrieve user data from the database
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

# Print HTML output
print("Content-Type: text/html\n\n")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Data</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h2>User Data</h2>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Age</th>
                    <th>Date of Birth</th>
                </tr>
            </thead>
            <tbody>
""")
for user in users:
    print(f"""
                <tr>
                    <td>{user[0]}</td>
                    <td>{user[1]}</td>
                    <td>{user[2]}</td>
                    <td>{user[3]}</td>
                    <td>{user[4]}</td>
                </tr>
""")
print("""
            </tbody>
        </table>
    </div>
</body>
</html>
""")
