# Reimbursement Portal

## Overview
The Reimbursement Portal is an online system designed to streamline the submission, approval, and management of employee reimbursement claims related to relocation, medical expenses, and office supplies. The portal supports three types of users: Admin, Manager, and Employee, each with specific roles and functionalities.

## Features

### Admin
- **Register and remove employees and managers.**
- **Add and manage departments.**
- **Assign managers to departments.**

### Manager
- **Assign departments to employees.**
- **Approve or reject reimbursement claims.**

### Employee
- **Submit reimbursement requests.**
- **Check the status of submitted requests.**
- **Upload supporting documents.**

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Database**: SQLite (can be replaced with PostgreSQL or MySQL)
- **APIs**: RESTful APIs for backend communication

## Installation and Setup
1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/reimbursement-portal.git
    cd reimbursement-portal
    ```

2. **Set up a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    ```sh
    flask db init
    flask db migrate
    flask db upgrade
    ```

5. **Run the application**:
    ```sh
    flask run
    ```

6. **Access the application**:
    Open your browser and navigate to `http://127.0.0.1:5000`

## Project Structure
- `app.py`: Main application file.
- `models.py`: Database models.
- `templates/`: HTML templates.
- `static/`: Static files (CSS, JS).
- `requirements.txt`: Python dependencies.

## Usage
1. **Login**: Use the login page to sign in as Admin, Manager, or Employee.
2. **Admin Panel**: Manage users and departments.
3. **Manager Panel**: Assign departments and manage reimbursement claims.
4. **Employee Panel**: Submit and track reimbursement requests.

## Future Enhancements
- **Improved UI/UX**: Further enhance the interface for a better user experience.
- **Notifications**: Add email notifications for claim status updates.
- **Reports**: Generate reports on reimbursement claims.

## Contribution
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries or feedback, please contact:
- **Name**: Akshat rAnjan Sinha 
- **Email**: toakshatranjan@gmail.com
