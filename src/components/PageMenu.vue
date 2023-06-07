<template>
  <aside class="menu-container">
    <nav>
        <li><router-link to="/test" class="menu-item">주식</router-link></li>
        <li><router-link to="/about" class="menu-item">주식상세</router-link></li>
        <li><router-link to="/search" class="menu-item">암호화폐</router-link></li>
    </nav>
  </aside>
</template>

<script>
</script>

<style scoped>
.menu-container {
  width: 200px;
  height: 100vh;
  background-color: #42b983; /* Dark green-blue */
  border-right: 1px solid #42B983; /* Vue.js green */
}

.menu-container nav {
  list-style: none;
  padding: 20px;
}

.menu-item {
  display: block;
  color: #white; /* White text */
  text-decoration: none;
  padding: 10px 0;
}

.menu-item:hover {
  color: #white; /* Vue.js green for hover state */
}
</style>
