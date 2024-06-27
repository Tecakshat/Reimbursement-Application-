from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import mysql.connector
import connector


app = Flask(__name__, template_folder='template')
app.secret_key = 'your_secret_key'


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    conn = mysql.connector.connect(
        host="localhost",
        database="reimbustment_database",
        username="root",
        password="@bhi2672"
    )

    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, password))
    user = cur.fetchone()
    
    print (user)
    cur.close()
    conn.close()

    if user:
        # print ("1")
        session['user_id'] = user[0]
        session['role'] = user[3]
        # for a, b, c, d, e in user:
        #     user[e] = 
        # if user['role'] == 'Admin':
        if user[3] == 'Admin':
            # print("mai admin tk pahuch raha hu")
            return render_template("admin_dashboard")
        elif user[3] == 'Manager':
            # print("mai manager tk pahuch raha hu")
            return redirect(url_for('manager_dashboard'))
        elif user[3] == 'Employee':
            # @app.route('/login', methods=['POST'])
            # def emp():
                # print("mai emp tk pahuch raha hu")
            return render_template('employee_dashboard')
    else:
        # print("0")
        return 'Invalid credentials', 401

@app.route('/admin_dashboard')
def admin_dashboard():
    if session.get('role') != 'Admin':
        return redirect(url_for('index'))
    conn = connector.conn
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE role != %s', ('Admin',))
    users = cur.fetchall()
    cur.execute('SELECT * FROM departments')
    departments = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('admin_dashboard.html', users=users, departments=departments)

@app.route('/add_user', methods=['POST'])
def add_user():
    if session.get('role') != 'Admin':
        return redirect(url_for('index'))
    email = request.form['email']
    password = request.form['password']
    role = request.form['role']
    department_id = request.form.get('department_id')
    conn = connector.conn
    cur = conn.cursor()
    cur.execute('INSERT INTO users (email, password, role, department_id) VALUES (%s, %s, %s, %s)', 
                (email, password, role, department_id))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('admin_dashboard'))

@app.route('/remove_user', methods=['POST'])
def remove_user():
    if session.get('role') != 'Admin':
        return redirect(url_for('index'))
    user_id = request.form['user_id']
    conn = connector.conn
    cur = conn.cursor()
    cur.execute('DELETE FROM users WHERE id = %s', (user_id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('admin_dashboard'))

@app.route('/add_department', methods=['POST'])
def add_department():
    if session.get('role') != 'Admin':
        return redirect(url_for('index'))
    name = request.form['name']
    conn = connector.conn
    cur = conn.cursor()
    cur.execute('INSERT INTO departments (name) VALUES (%s)', (name,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('admin_dashboard'))

@app.route('/manager_dashboard')
def manager_dashboard():
    if session.get('role') != 'Manager':
        return redirect(url_for('index'))
    conn = mysql.connector.connect(
    host="localhost",
    database="reimbustment_database",
    username="root",
    password="@bhi2672"
    )
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE role = %s', ('Employee',))
    employees = cur.fetchall()
    cur.execute('SELECT * FROM departments')
    departments = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('manager_dashboard.html')
    # return render_template('login.html')

@app.route('/assign_department', methods=['POST'])
def assign_department():
    if session.get('role') != 'Manager':
        return redirect(url_for('index'))
    user_id = request.form['user_id']
    department_id = request.form['department_id']
    conn = connector.conn
    cur = conn.cursor()
    cur.execute('UPDATE users SET department_id = %s WHERE id = %s', (department_id, user_id))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('manager_dashboard'))

@app.route('/employee_dashboard')
def employee_dashboard():
    if session.get('role') != 'Employee':
        return redirect(url_for('index'))
    conn = mysql.connector.connect(
        host="localhost",
        database="reimbustment_database",
        username="root",
        password="@bhi2672"
    )
    cur = conn.cursor()
    cur.execute('SELECT * FROM reimbursement_queries WHERE employee_id = %s', (session.get('user_id'),))
    queries = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('employee_dashboard.html', queries=queries)

@app.route('/raise_query')
def raise_query():
    if session.get('role') != 'Employee':
        return redirect(url_for('index'))
    return redirect('https://docs.google.com/forms/d/e/1FAIpQLSed-KyX4ppSTs0uFazjzc6NFZmtQPvFISoTYgu0LXpnAOUeRA/viewform?usp=sf_link')



if __name__ == '__main__':
    app.run(debug=True)