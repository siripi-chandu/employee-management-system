import mysql.connector

# ✅ Database connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="siripi",
        password="Chandu#143",
        database="EMS",
        port=3306
    )

# ✅ Employee CRUD Functions

def get_employees():
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Employees")
    employees = cursor.fetchall()
    db.close()
    return employees

def get_employee(emp_id):
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Employees WHERE id = %s", (emp_id,))
    employee = cursor.fetchone()
    db.close()
    return employee

def add_employee(data):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO Employees (name, department, role, email, phone, address)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (data['name'], data['department'], data['role'], data['email'], data['phone'], data['address']))
    db.commit()
    db.close()

def update_employee(emp_id, data):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("""
        UPDATE Employees
        SET name=%s, department=%s, role=%s, email=%s, phone=%s, address=%s
        WHERE id=%s
    """, (data['name'], data['department'], data['role'], data['email'], data['phone'], data['address'], emp_id))
    db.commit()
    db.close()

def delete_employee(emp_id):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM Employees WHERE id = %s", (emp_id,))
    db.commit()
    db.close()

# ✅ Task Management Functions

def get_tasks():
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT Tasks.*, Employees.name AS employee_name
        FROM Tasks
        JOIN Employees ON Tasks.employee_id = Employees.id
    """)
    tasks = cursor.fetchall()
    db.close()
    return tasks

def get_all_employees():
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT id, name FROM Employees")
    employees = cursor.fetchall()
    db.close()
    return employees

def add_task(data):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO Tasks (employee_id, title, description, deadline, status)
        VALUES (%s, %s, %s, %s, %s)
    """, (data['employee_id'], data['title'], data['description'], data['deadline'], data['status']))
    db.commit()
    db.close()

def delete_task(task_id):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM Tasks WHERE id = %s", (task_id,))
    db.commit()
    db.close()

# ✅ Attendance Functions

def mark_attendance(data):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO Attendance (employee_id, date, status)
        VALUES (%s, %s, %s)
    """, (data['employee_id'], data['date'], data['status']))
    db.commit()
    db.close()

def get_attendance():
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT Attendance.*, Employees.name 
        FROM Attendance
        JOIN Employees ON Attendance.employee_id = Employees.id
        ORDER BY date DESC
    """)
    records = cursor.fetchall()
    db.close()
    return records

# ✅ Leave Request Functions

def submit_leave(data):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO LeaveRequests (employee_id, from_date, to_date, reason, status)
        VALUES (%s, %s, %s, %s, %s)
    """, (data['employee_id'], data['from_date'], data['to_date'], data['reason'], data['status']))
    db.commit()
    db.close()

def get_leave_requests():
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT LeaveRequests.*, Employees.name 
        FROM LeaveRequests
        JOIN Employees ON LeaveRequests.employee_id = Employees.id
        ORDER BY from_date DESC
    """)
    requests = cursor.fetchall()
    db.close()
    return requests
