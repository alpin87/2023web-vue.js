<template>
    <header class="header-container">
      <nav>
        <router-link to="/" class="nav-item">Home</router-link> |
        <router-link to="/login" class="nav-item">Login</router-link>
        <BoardMenu />
      </nav>
      <hr>
    </header>
</template>

<script>
import BoardMenu from './BoardMenu.vue'

export default {
  name: 'PageHeader',
  components: {
    BoardMenu
  }
}
</script>

<style scoped>
.header-container {
  background-color: #42b983; /* Dark green-blue */
  color: #fff; /* White text */
}

.nav-item {
  text-decoration: none;
  color: #fff; /* White text */
  font-size: 1.2em; /* Increased font size */
}

.nav-item:hover {
  color: #42B983; /* Vue.js green for hover state */
}

hr {
  border-top: 1px solid #42B983; /* Vue.js green for horizontal line */
}
</style>
