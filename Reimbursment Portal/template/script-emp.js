document.addEventListener('DOMContentLoaded', (event) => {
    const raiseQueryButton = document.getElementById('raiseQueryButton');
    const viewPreviousQueriesButton = document.getElementById('viewPreviousQueriesButton');
    const queryList = document.getElementById('queryList');

    if (raiseQueryButton) {
        raiseQueryButton.addEventListener('click', () => {
            window.location.href = '/raise_query';
        });
    }

    if (viewPreviousQueriesButton) {
        viewPreviousQueriesButton.addEventListener('click', () => {
            fetch('/previous_queries')
                .then(response => response.json())
                .then(data => {
                    queryList.innerHTML = '';
                    if (data.queries.length > 0) {
                        data.queries.forEach(query => {
                            const listItem = document.createElement('li');
                            listItem.textContent = `${query.description} - ₹${query.amount} - ${query.status}`;
                            queryList.appendChild(listItem);
                        });
                    } else {
                        queryList.innerHTML = '<li>No previous queries found.</li>';
                    }
                })
                .catch(error => console.error('Error:', error));
        });
    }
});