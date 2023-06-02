<!-- LoginPage.vue -->
<template>
  <div class="container">
    <h2>Login</h2>
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
        <router-link to="/signup" class="btn">Sign Up</router-link>
      </div>
    </form>
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
      this.$router.push('/HomeView')
    }
  }
}
</script>

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
