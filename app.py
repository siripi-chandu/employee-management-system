from flask import Flask, render_template, request, redirect, url_for
import database
from datetime import date

app = Flask(__name__)

# ---------------------------------------
# Home
# ---------------------------------------

@app.route('/')
def home():
    return redirect(url_for('list_employees'))

# ---------------------------------------
# Employees
# ---------------------------------------

@app.route('/employees')
def list_employees():
    employees = database.get_employees()
    return render_template('employees.html', employees=employees)

@app.route('/employees/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        database.add_employee(request.form)
        return redirect(url_for('list_employees'))
    return render_template('add_employee.html')

@app.route('/employees/edit/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    if request.method == 'POST':
        database.update_employee(id, request.form)
        return redirect(url_for('list_employees'))
    employee = database.get_employee(id)
    return render_template('edit_employee.html', employee=employee)

@app.route('/employees/delete/<int:id>')
def delete_employee(id):
    database.delete_employee(id)
    return redirect(url_for('list_employees'))

# ---------------------------------------
# Tasks
# ---------------------------------------

@app.route('/tasks')
def list_tasks():
    tasks = database.get_tasks()
    return render_template('tasks.html', tasks=tasks)

@app.route('/tasks/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        database.add_task(request.form)
        return redirect(url_for('list_tasks'))
    employees = database.get_all_employees()
    return render_template('add_task.html', employees=employees)

@app.route('/tasks/delete/<int:id>')
def delete_task(id):
    database.delete_task(id)
    return redirect(url_for('list_tasks'))

# ---------------------------------------
# Attendance
# ---------------------------------------

@app.route('/attendance')
def list_attendance():
    records = database.get_attendance()
    return render_template('attendance.html', records=records)

@app.route('/attendance/mark', methods=['GET', 'POST'])
def mark_attendance():
    if request.method == 'POST':
        data = {
            'employee_id': request.form['employee_id'],
            'date': request.form.get('date', str(date.today())),
            'status': request.form['status']
        }
        database.mark_attendance(data)
        return redirect(url_for('list_attendance'))
    employees = database.get_all_employees()
    return render_template('mark_attendance.html', employees=employees)

# ---------------------------------------
# Leave Requests
# ---------------------------------------

@app.route('/leave')
def list_leave():
    requests = database.get_leave_requests()
    return render_template('leave.html', requests=requests)

@app.route('/leave/apply', methods=['GET', 'POST'])
def apply_leave():
    if request.method == 'POST':
        data = {
            'employee_id': request.form['employee_id'],
            'from_date': request.form['from_date'],
            'to_date': request.form['to_date'],
            'reason': request.form['reason'],
            'status': 'Pending'
        }
        database.submit_leave(data)
        return redirect(url_for('list_leave'))
    employees = database.get_all_employees()
    return render_template('apply_leave.html', employees=employees)

# ---------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
