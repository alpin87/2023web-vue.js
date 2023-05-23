<template>
  <nav class="board-menu">
    <ul>
      <li><router-link to="/board/general">General</router-link></li>
      <li><router-link to="/board/news">News</router-link></li>
      <li><router-link to="/board/discussion">Discussion</router-link></li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'BoardMenu'
}
</script>

<style scoped>
.board-menu ul {
  list-style-type: none;
  padding: 0;
}

.board-menu li {
  display: inline-block;
  margin-right: 20px;
}

.board-menu li a {
  text-decoration: none;
  color: #333;
}

.board-menu li a:hover {
  color: #42b983;
}
</style>
