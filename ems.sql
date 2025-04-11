CREATE DATABASE IF NOT EXISTS EMS;
USE EMS;

CREATE TABLE Employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    role VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15),
    address TEXT
);

CREATE TABLE Tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    title VARCHAR(255),
    description TEXT,
    deadline DATE,
    status VARCHAR(50),
    FOREIGN KEY (employee_id) REFERENCES Employees(id)
);

CREATE TABLE Attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    date DATE,
    status VARCHAR(20),
    FOREIGN KEY (employee_id) REFERENCES Employees(id)
);

CREATE TABLE LeaveRequests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    from_date DATE,
    to_date DATE,
    reason TEXT,
    status VARCHAR(20),
    FOREIGN KEY (employee_id) REFERENCES Employees(id)
);
