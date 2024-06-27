from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)

class Query(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

@app.route('/get_departments', methods=['GET'])
def get_departments():
    departments = Department.query.all()
    return jsonify({'departments': [{'id': dept.id, 'name': dept.name} for dept in departments]})

@app.route('/assign_department', methods=['POST'])
def assign_department():
    data = request.form
    employee_id = data.get('employeeId')
    department_id = data.get('department')
    return jsonify({'success': True, 'message': 'Department assigned successfully'})

@app.route('/manage_query/approve', methods=['POST'])
def approve_query():
    data = request.json
    query_id = data.get('queryId')
    query = Query.query.get(query_id)
    if query:
        query.status = 'Approved'
        db.session.commit()
        return jsonify({'success': True, 'message': 'Query approved successfully'})
    return jsonify({'success': False, 'message': 'Query not found'})

@app.route('/manage_query/reject', methods=['POST'])
def reject_query():
    data = request.json
    query_id = data.get('queryId')
    query = Query.query.get(query_id)
    if query:
        query.status = 'Rejected'
        db.session.commit()
        return jsonify({'success': True, 'message': 'Query rejected successfully'})
    return jsonify({'success': False, 'message': 'Query not found'})

if __name__ == '_main_':
    app.run(debug=True)