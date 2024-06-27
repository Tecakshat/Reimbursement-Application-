document.addEventListener('DOMContentLoaded', function () {
    const adminLoginBtn = document.getElementById('admin-login');
    const managerLoginBtn = document.getElementById('manager-login');
    const employeeLoginBtn = document.getElementById('employee-login');
    const loginForm = document.getElementById('login-form');
    const loginFormContainer = document.getElementById('login-form-container');

    adminLoginBtn.addEventListener('click', function () {
        showLoginForm('Admin');
    });

    managerLoginBtn.addEventListener('click', function () {
        showLoginForm('Manager');
    });

    employeeLoginBtn.addEventListener('click', function () {
        showLoginForm('Employee');
    });

    loginForm.addEventListener('submit', function (event) {
        event.preventDefault();
        // Add form validation and submit logic here
        document.getElementById('login-form').addEventListener('submit', function(event) {
            event.preventDefault();
        
            var email = document.getElementById('email').value;
            var password = document.getElementById('password').value;
        
            fetch('/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: 'email=' + encodeURIComponent(email) + '&password=' + encodeURIComponent(password)
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    if (data.role === 'Admin') {
                        window.location.href = 'admin_pannel.html';
                    } else if (data.role === 'Manager') {
                        window.location.href = 'manager_pannel.html';
                    } else if (data.role === 'Employee') {
                        window.location.href = 'employee_pannel.html';
                    }
                } else {
                    document.getElementById('error-message').textContent = 'Invalid credentials. Please try again.';
                }
            })
            .catch(error => console.error('Error:', error));
        });
        alert('Logging in as ' + loginForm.getAttribute('data-role'));
    });

    function showLoginForm(role) {
        loginFormContainer.style.display = 'flex';
        loginForm.setAttribute('data-role', role);
        loginForm.querySelector('button[type="submit"]').textContent = `Login as ${role}`;
    }

    // document.getElementById("myButton").onclick = function () {
    //     location.href = "employee_pannel.html";
    // };
});


// document.getElementById('login-form').addEventListener('submit', function(event) {
//     event.preventDefault();

//     var email = document.getElementById('email').value;
//     var password = document.getElementById('password').value;

//     fetch('/login', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/x-www-form-urlencoded'
//         },
//         body: 'email=' + encodeURIComponent(email) + '&password=' + encodeURIComponent(password)
//     })
//     .then(response => response.json())
//     .then(data => {
//         if (data.status === 'success') {
//             if (data.role === 'Admin') {
//                 window.location.href = '/admin_pannel';
//             } else if (data.role === 'Manager') {
//                 window.location.href = '/manager_pannel.html';
//             } else if (data.role === 'Employee') {
//                 window.location.href = '/employee_pannel,html';
//             }
//         } else {
//             document.getElementById('error-message').textContent = 'Invalid credentials. Please try again.';
//         }
//     })
//     .catch(error => console.error('Error:', error));
// });
