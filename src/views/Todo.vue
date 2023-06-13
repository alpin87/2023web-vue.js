<template>
  <div class="app-container">
    <div class="todo-container">
      <div class="todo-header">
        <h1>체크리스트</h1>
        <div class="todo-input">
          <input v-model="newTodo" placeholder="할 일을 입력하세요" />
          <button @click="addTodo">추가</button>
        </div>
      </div>
      <div class="todo-list-container">
        <div class="todo-list-row" v-for="(row, i) in todoRows" :key="'row-' + i">
          <div class="todo-item" v-for="(todo, index) in row" :key="'todo-' + index">
            <input
              type="checkbox"
              v-model="todo.completed"
              @change="handleCheckboxChange(todo)"
            />
            <span :class="{ 'completed': todo.completed }">{{ todo.text }}</span>
            <button @click="deleteTodo(index + i * 4)">삭제</button>
          </div>
        </div>
      </div>
    </div>
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
  computed: {
    todoRows () {
      const rows = []
      for (let i = 0; i < this.todos.length; i += 4) {
        rows.push(this.todos.slice(i, i + 4))
      }
      return rows
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
.app-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  padding: 20px;
  box-sizing: border-box;
  background-color: #f0f0f0;
}

.todo-container {
  max-width: 800px;
  width: 100%;
  background-color: #ffffff;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
  border-radius: 10px;
}

.todo-header {
  text-align: center;
}

.todo-header h1 {
  color: #333333;
  font-size: 2.5em;
  margin-bottom: 10px;
}

.todo-input {
  margin-top: 10px;
}

.todo-list-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.todo-list-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  padding: 10px 0;
}

.todo-item {
  width: calc(25% - 10px);
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
  padding: 15px;
  background: linear-gradient(to right, #f5f5f5, #fff);
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.todo-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
}

.todo-item.completed {
  opacity: 0.7;
  text-decoration: line-through;
}

.todo-item span {
  flex-grow: 1;
  font-size: 18px;
  font-weight: bold;
  color: #333;
}

.todo-item button {
  margin-left: 10px;
  padding: 8px 12px;
  background-color: #f54242;
  color: #fff;
  border: none;
  border-radius: 3px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.3s ease;
}

.todo-item button:hover {
  background-color: #d12323;
}
</style>
