<template>
   <aside class="menu-container">
    <nav>
        <li><router-link to="/test" class="menu-item">메뉴1(test)</router-link></li>
        <li><router-link to="/about" class="menu-item">메뉴2(about)</router-link></li>
        <li><a href="#" class="menu-item">회사</a></li>
    </nav>
   </aside>
</template>

<script>
</script>

<style scoped>
.menu-container {
  width: 200px;
  height: 100vh;
  background-color: #f5f5f5;
  border-right: 1px solid #ddd;
}

.menu-container nav {
  list-style: none;
  padding: 20px;
}

.menu-item {
  display: block;
  color: #333;
  text-decoration: none;
  padding: 10px 0;
}

.menu-item:hover {
  color: #42b983;
}
</style>
