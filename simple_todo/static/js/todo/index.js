window.addEventListener("DOMContentLoaded", function (e) {
    const todos = document.querySelectorAll(".todo-item");
    const btn_finish = document.querySelector(".btn-finish");
    const todo_list_form = document.querySelector(".todo-list-form");
    const new_todo_form = document.querySelector(".new-todo-form");
    const new_todo = document.querySelector("#new-todo");

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

    new_todo_form.addEventListener("submit", function (e) {
        if (new_todo.value.trim() == "") {
            e.preventDefault();
            return false;
        }
    });
    
});