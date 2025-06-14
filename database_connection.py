import mysql.connector

# Connect to MySQL Server
cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="SUBHAN1234@"
)

cur = cnx.cursor()
# Step 1: Create database
cur.execute("CREATE DATABASE IF NOT EXISTS studentdb")
cur.execute("USE studentdb")

# Step 2: Create table
cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        roll_no INT PRIMARY KEY,
        name VARCHAR(100),
        phone VARCHAR(15),
        email VARCHAR(100),
        department VARCHAR(100)
    )
""")

# Step 3: Collect and insert data
keys = ["Roll no", "Name", "Phone", "Email", "Department"]


for _ in range(3):  # Loop 3 times to enter 3 students
    data = {}
    for i in keys:
        value_user = input(f"Enter the value of {i}: ")
        if i == "Roll no":
            value_user = int(value_user)  # Ensure roll_no is int
        data[i] = value_user

    # Insert into table
    cur.execute("""
        INSERT INTO students (roll_no, name, phone, email, department)
        VALUES (%s, %s, %s, %s, %s)
    """, (data["Roll no"], data["Name"], data["Phone"], data["Email"], data["Department"]))
    cnx.commit()  # Save changes to database

    print("Data inserted successfully:\n")
    for key, value in data.items():
        print(f"{key} : {value}")
    print("-" * 30)

# Step 4: Show current date
cur.execute("SELECT CURDATE()")
row = cur.fetchone()
print("Current date is:", row[0])

cur.close()
cnx.close()