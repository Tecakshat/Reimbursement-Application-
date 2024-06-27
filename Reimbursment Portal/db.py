import mysql.connector

conn = mysql.connector.connect(
        host="localhost",
        database="reimbustment_database",
        username="root",
        password="@bhi2672"
    )

my_cursor = conn.cursor()
# my_cursor.execute("CREATE TABLE reimbursement_queries (id SERIAL PRIMARY KEY, employee_id INTEGER REFERENCES users(id), query TEXT NOT NULL, status VARCHAR(50) DEFAULT 'Pending', created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
# print("Table created!")
# my_cursor.execute("INSERT INTO users (email, password, role, department_id) VALUES ('admin@company.com', 'adminpassword', 'Admin', NULL), ('manager1@company.com', 'managerpassword1', 'Manager', 1), ('manager2@company.com', 'managerpassword2', 'Manager', 2), ('manager3@company.com', 'managerpassword3', 'Manager', 3), ('employee1@company.com', 'employeepassword1', 'Employee', 1), ('employee2@company.com', 'employeepassword2', 'Employee', 1), ('employee3@company.com', 'employeepassword3', 'Employee', 2), ('employee4@company.com', 'employeepassword4', 'Employee', 2), ('employee5@company.com', 'employeepassword5', 'Employee', 3), ('employee6@company.com', 'employeepassword6', 'Employee', 3)")
# print("row updated!")
my_cursor.execute("select * from users") 
view = my_cursor.fetchall()
print (view)

