document.addEventListener('DOMContentLoaded', (event) => {
    const assignDepartmentForm = document.getElementById('assignDepartmentForm');
    const departmentSelect = document.getElementById('department');
    const queryList = document.getElementById('queryList');

    // Fetch and populate departments
    fetch('/get_departments')
        .then(response => response.json())
        .then(data => {
            departmentSelect.innerHTML = '';
            data.departments.forEach(department => {
                const option = document.createElement('option');
                option.value = department.id;
                option.textContent = department.name;
                departmentSelect.appendChild(option);
            });
        })
        .catch(error => console.error('Error fetching departments:', error));

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

    if (queryList) {
        queryList.addEventListener('click', (e) => {
            if (e.target.classList.contains('approveButton') || e.target.classList.contains('rejectButton')) {
                const queryId = e.target.getAttribute('data-id');
                const action = e.target.classList.contains('approveButton') ? 'approve' : 'reject';
                fetch(`/manage_query/${action}`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ queryId: queryId })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        alert(`Query ${action}d successfully`);
                        location.reload();
                    } else {
                        alert(`Error ${action}ing query: ` + data.message);
                    }
                })
                .catch(error => console.error('Error:', error));
            }
        });
    }
});