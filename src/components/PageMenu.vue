<template>
  <aside class="menu-container" :style="menuOpen ? {'transform': 'translateY(0)', 'visibility': 'visible', 'opacity': '1'} : {'transform': 'translateY(-100%)', 'visibility': 'hidden', 'opacity': '0'}">
    <div class="menu-box">
      <nav>
          <li><router-link to="/test" class="menu-item">주식</router-link></li>
          <li><router-link to="/about" class="menu-item">주식차트</router-link></li>
          <li><router-link to="/search" class="menu-item">암호화폐</router-link></li>
      </nav>
    </div>
  </aside>
</template>

<script>
export default {
  props: {
    menuOpen: {
      type: Boolean,
      required: true
    }
  }
}
</script>

<style scoped>
.menu-container {
  position: absolute;
  top: 180px;
  left: 0;
  height: calc(100vh - 80px);
  width: 200px;
  transition: transform 0.7s ease-in-out, visibility 1.5s ease-in-out, opacity 1.5s ease-in-out;
  z-index: 1000;
  border-radius: 5px;
  margin-left:70px;
  transform: translateY(-100%);
  visibility: hidden; /* 초기에 메뉴를 안 보이게 설정 */
  opacity: 0;
  background-color:white;
}

.menu-box {
  position: sticky;
  top: 10%;
  width: 200px;
  height: 200px;
  z-index: 1000;
}

.menu-box nav {
  list-style: none;
  padding: 20px;
}

.menu-item {
  display: block;
  color: #fff;
  background-color: #42B983;
  text-decoration: none;
  font-size: 1.2em;
  padding: 10px 20px;
  border-radius: 10px;
  transition: all 0.3s ease;
  margin-bottom: 10px;
}

.menu-item {
  color: #000;
  background-color: #42b883;
}
</style>
