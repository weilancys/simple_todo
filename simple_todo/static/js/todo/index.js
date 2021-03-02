window.addEventListener("DOMContentLoaded", function (e) {
    const todos = document.querySelectorAll(".todo-item");
    const btn_finish = document.querySelector(".btn-finish");
    const todo_list_form = document.querySelector(".todo-list form");

    todo_list_form.addEventListener("submit", function (e) {
        let non_checked = true;
        for (const todo of todos) {
            if (todo.checked) {
                non_checked = false;
            }
        }
        if (non_checked) {
            e.preventDefault();
        }
    });
    
});