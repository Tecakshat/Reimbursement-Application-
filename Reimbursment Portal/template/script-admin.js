document.addEventListener('DOMContentLoaded', (event) => {
    const addUserForm = document.getElementById('addUserForm');
    if (addUserForm) {
        addUserForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const formData = new FormData(addUserForm);
            fetch('/add_user', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('User added successfully');
                    location.reload();
                } else {
                    alert('Error adding user: ' + data.message);
                }
            })
            .catch(error => console.error('Error:', error));
        });
    }

    const removeUserForm = document.getElementById('removeUserForm');
    if (removeUserForm) {
        removeUserForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const formData = new FormData(removeUserForm);
            fetch('/remove_user', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('User removed successfully');
                    location.reload();
                } else {
                    alert('Error removing user: ' + data.message);
                }
            })
            .catch(error => console.error('Error:', error));
        });
    }

    const addDepartmentForm = document.getElementById('addDepartmentForm');
    if (addDepartmentForm) {
        addDepartmentForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const formData = new FormData(addDepartmentForm);
            fetch('/add_department', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Department added successfully');
                    location.reload();
                } else {
                    alert('Error adding department: ' + data.message);
                }
            })
            .catch(error => console.error('Error:', error));
        });
    }

    const assignDepartmentForm = document.getElementById('assignDepartmentForm');
    if (assignDepartmentForm) {
        assignDepartmentForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const formData = new FormData(assignDepartmentForm);
            fetch('/assign_department', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Department assigned successfully');
                    location.reload();
                } else {
                    alert('Error assigning department: ' + data.message);
                }
            })
            .catch(error => console.error('Error:', error));
        });
    }
});