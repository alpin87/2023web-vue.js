<template>
  <div class="container">
    <div class="card">
      <h2 class="card-header">Login</h2>
      <form @submit.prevent="login" class="form">
        <div class="form-group">
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="username" class="form-control" required>
        </div>
        <div class="form-group">
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" class="form-control" required>
        </div>
        <div class="btn-group">
          <button type="submit" class="btn">Login</button>
          <router-link to="/signup" class="btn btn-secondary">Sign Up</router-link>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    login () {
      if (!this.username) {
        alert('아이디를 입력해주세요')
        this.username = ''
        return
      }

      if (!this.password) {
        alert('비밀번호를 입력해주세요')
        this.password = ''
        return
      }

      alert('로그인 성공!')
      this.$router.push({ name: 'home' })
    }
  }
}
</script>

<style scoped>
body, html {
  width: 1000px;
  height: 100%;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: flex-start; /* change start to flex-start */
  background: #f2f2f2;
}

.container {
  width: 1000px;
  display: flex;
  justify-content: center;
  align-items: flex-start; /* change start to flex-start */
  min-height: 100vh;
  padding: 0 20px;
  background-color: #f4f4f4;
}
.form {
  padding: 50px 20px; /* Increase the top and bottom padding */
}
.card {
  width: 100%;
  max-width: 500px;
  margin: auto; /* Center the card */
  background-color: #fff;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  overflow: hidden;
}

.card-header {
  background-color: #42b983;
  color: #fff;
  padding: 20px;
  font-size: 1.5rem;
}

.form {
  padding: 20px;
}

.form-group {
  margin-bottom: 10px;
}

.form-control {
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ddd;
  font-size: 1rem;
}

.btn-group {
  display: flex;
  justify-content: space-between;
}

.btn {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  color: #fff;
  background-color: #42b983;
  cursor: pointer;
  font-size: 1rem;
}

.btn-secondary {
  background-color: #ddd;
  color: #333;
}
</style>
