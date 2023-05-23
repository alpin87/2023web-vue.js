<!-- LoginPage.vue -->
<template>
  <div class="container">
    <h2>Login</h2>
    <form @submit.prevent="login" class="form">
      <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="username" class="form-control">
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" class="form-control">
      </div>
      <div class="btn-group">
        <button type="submit" class="btn">Login</button>
        <router-link to="/signup" class="btn">Sign Up</router-link>
      </div>
    </form>
  </div>
</template>

<!-- 기존의 script와 style 코드는 생략했습니다 -->

<style scoped>
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.btn-group {
  display: flex;
  justify-content: space-between;
}

.form-control, .btn {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.btn {
  cursor: pointer;
  background-color: #42b983;
  color: #fff;
}
</style>
