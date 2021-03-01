window.addEventListener("DOMContentLoaded", function (e) {
    const todos = document.querySelectorAll(".todo-item");
    const btn_finish = document.querySelector(".btn-finish");

    btn_finish.addEventListener("click", function (e) {
        let text = "";
        for (const todo of todos) {
            if (todo.checked) {
                text += todo.value + " ";
            }
        }
        alert(text);
    });
});