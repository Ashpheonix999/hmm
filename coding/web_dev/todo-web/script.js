const input = document.getElementById('todo-input');
const button = document.getElementById('add-task');
const list = document.getElementById('todo-list');

let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

// 🧠 Add task on button click
button.addEventListener('click', function () {
    const task = input.value.trim();

    if (task !== '') {
        addTaskToUI(task);
        tasks.push(task);
        localStorage.setItem('tasks', JSON.stringify(tasks));
        input.value = '';
    }
});

// 🧠 Reusable function to add task + delete button
function addTaskToUI(task) {
    const li = document.createElement('li');
    li.innerText = task;

    const deleteBtn = document.createElement('button');
    deleteBtn.innerText = '❌';
    deleteBtn.style.marginLeft = '10px';

    deleteBtn.addEventListener('click', function () {
        li.remove();
        tasks = tasks.filter(t => t !== task);
        localStorage.setItem('tasks', JSON.stringify(tasks));
    });

    li.appendChild(deleteBtn);
    list.appendChild(li);
}

// 🧠 Load tasks on page load
function loadTasks() {
    tasks.forEach(task => addTaskToUI(task));
}

loadTasks();
