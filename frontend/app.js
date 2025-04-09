// Base url for the backend API
const apiBase = 'http://localhost:5000/api/tasks';

// Event listener for form submission
document.getElementById('task-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const input = document.getElementById('task-input');
    const taskText = input.value;

    await fetch(apiBase, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ description: taskText })
    });

    input.value = '';
    loadTasks();
});

async function loadTasks() {
    const res = await fetch(apiBase);
    const tasks = await res.json();

    const taskList = document.getElementById('task-list');
    taskList.innerHTML = '';

    tasks.forEach(task => {
        const li = document.createElement('li');
        li.classList.add('task-item');  // Apply task-item class for styling
        
        // Add a class for completed tasks
        if (task.completed) {
            li.classList.add('completed');
        }
    
        // Display task description
        const taskText = document.createElement('span');
        taskText.textContent = task.description;
        li.appendChild(taskText);
    
        // Add the delete button for each task
        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';
        deleteButton.addEventListener('click', (e) => {
            e.stopPropagation();  // Prevent toggling task when clicking delete
            deleteTask(task.id);  // Implement deleteTask function as needed
        });
    
        li.appendChild(deleteButton);
    
        // Toggle the completed status when clicking on the task item
        li.addEventListener('click', () => toggleTask(task.id));
    
        taskList.appendChild(li);
    });    
}

async function toggleTask(id) {
    await fetch(`${apiBase}/${id}`, { method: 'PUT' });
    loadTasks();
}

async function deleteTask(id) {
    await fetch(`${apiBase}/${id}`, {
        method: 'DELETE'
    });
    loadTasks();
}

loadTasks();