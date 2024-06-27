-- Create the departments table
CREATE TABLE departments (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Create the users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL,
    department_id INTEGER REFERENCES departments(id)
);

-- Create the reimbursement queries table
CREATE TABLE reimbursement_queries (
    id SERIAL PRIMARY KEY,
    employee_id INTEGER REFERENCES users(id),
    query TEXT NOT NULL,
    status VARCHAR(50) DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert departments
INSERT INTO departments (name) VALUES
('Marketing'),
('Finance'),
('Production');

-- Insert users (1 admin, 3 managers, 6 employees)
INSERT INTO users (email, password, role, department_id) VALUES
('admin@company.com', 'adminpassword', 'Admin', NULL),          -- Admin
('manager1@company.com', 'managerpassword1', 'Manager', 1),    -- Marketing Manager
('manager2@company.com', 'managerpassword2', 'Manager', 2),    -- Finance Manager
('manager3@company.com', 'managerpassword3', 'Manager', 3),    -- Production Manager
('employee1@company.com', 'employeepassword1', 'Employee', 1), -- Marketing Employee 1
('employee2@company.com', 'employeepassword2', 'Employee', 1), -- Marketing Employee 2
('employee3@company.com', 'employeepassword3', 'Employee', 2), -- Finance Employee 1
('employee4@company.com', 'employeepassword4', 'Employee', 2), -- Finance Employee 2
('employee5@company.com', 'employeepassword5', 'Employee', 3), -- Production Employee 1
('employee6@company.com', 'employeepassword6', 'Employee', 3); -- Production Employee 2
