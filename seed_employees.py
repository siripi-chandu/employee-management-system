from faker import Faker
import mysql.connector
import random

# Database connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="siripi",
        password="Chandu#143",
        database="EMS",
        port=3306
    )

# Generate and insert fake employees
def seed_employees(n=100):
    fake = Faker()
    departments = ['HR', 'IT', 'Finance', 'Sales', 'Marketing']
    roles = ['Manager', 'Analyst', 'Engineer', 'Consultant', 'Intern']

    db = connect_db()
    cursor = db.cursor()

    for _ in range(n):
        name = fake.name()
        department = random.choice(departments)
        role = random.choice(roles)
        email = fake.email()
        phone = fake.phone_number()
        address = fake.address().replace("\n", ", ")

        cursor.execute("""
            INSERT INTO Employees (name, department, role, email, phone, address)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (name, department, role, email, phone, address))

    db.commit()
    db.close()
    print(f"✅ {n} fake employee records inserted successfully.")

if __name__ == '__main__':
    seed_employees()
