<template>
  <div class="todo-container">
    <div class="todo-header">
      <h1>Todo List</h1>
      <div class="todo-input">
        <input v-model="newTodo" placeholder="할 일을 입력하세요" />
        <button @click="addTodo">추가</button>
      </div>
    </div>
    <ul class="todo-list">
      <li v-for="(todo, index) in todos" :key="index">
        <input
          type="checkbox"
          v-model="todo.completed"
          @change="handleCheckboxChange(todo)"
        />
        <span :class="{ 'completed': todo.completed }">{{ todo.text }}</span>
        <button @click="deleteTodo(index)">삭제</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'ToDoList',
  data () {
    return {
      newTodo: '',
      todos: []
    }
  },
  created () {
    // Retrieve todos from local storage
    const storedTodos = localStorage.getItem('todos')
    if (storedTodos) {
      this.todos = JSON.parse(storedTodos)
    }
  },
  methods: {
    addTodo () {
      if (this.newTodo.trim()) {
        this.todos.push({
          text: this.newTodo,
          completed: false
        })
        this.newTodo = ''
        this.saveTodos()
      }
    },
    deleteTodo (index) {
      this.todos.splice(index, 1)
      this.saveTodos()
    },
    handleCheckboxChange (todo) {
      if (todo.completed) {
        this.todos = this.todos.filter((item) => item !== todo)
        this.saveTodos()
      }
    },
    saveTodos () {
      // Save todos to local storage
      localStorage.setItem('todos', JSON.stringify(this.todos))
    }
  }
}
</script>

<style scoped>
body, html {
  height: 100%;
  width: 100%;
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0;
  background: #f2f2f2;
}

.todo-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 50px;
}

.todo-header {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
}

.todo-input {
  margin-top: 10px;
}

.todo-list {
  margin-top: 20px;
  list-style: none;
}

.todo-list li {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
  padding: 15px;
  background-color: #fff;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.todo-list li:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.todo-list li.completed {
  opacity: 0.7;
  text-decoration: line-through;
}

.todo-list li span {
  flex-grow: 1;
  font-size: 18px;
  font-weight: bold;
  color: #333;
}

.todo-list li button {
  margin-left: 10px;
  padding: 8px 12px;
  background-color: #d62828;
  color: #fff;
  border: none;
  border-radius: 3px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.3s ease;
}

.todo-list li button:hover {
  background-color: #b71c1c;
}
</style>
