<!-- SignUpPage.vue -->
<template>
  <div class="container">
    <div class="card">
      <h2 class="card-header">Sign Up</h2>
      <form @submit.prevent="signUp" class="form">
        <div class="form-group">
          <label for="new-username">아이디</label>
          <input type="text" id="new-username" v-model="username" class="form-control" required>
        </div>
        <div class="form-group">
          <label for="new-password">비밀번호</label>
          <input type="password" id="new-password" v-model="password" class="form-control" required>
        </div>
        <button type="submit" class="btn">Sign Up</button>
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
    signUp () {
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

      console.log('Signing up with', this.username, this.password)
      alert('생성 완료')
      this.$router.push('/login')
    }
  }
}
</script>

<style scoped>
body, html {
  width: 1800px;
  height: 100%;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #f2f2f2;
}

.container {
  width: 1800px; /* Updated width to 1800px */
  display: flex;
  justify-content: center;
  align-items: flex-start; /* Updated to align items to the start */
  min-height: 100vh;
  padding: 0 20px;
  background-color: #f4f4f4;
}

.form {
  padding: 50px 20px;
}

.card {
  width: 100%;
  max-width: 500px;
  background-color: #fff;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  overflow: hidden;
  margin-top:200px;
}

.card-header {
  background-color: #42b983;
  color: #fff;
  padding: 20px;
  font-size: 1.5rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  align-items: stretch;
  gap: 10px;
}

.form-control, .btn {
  padding: 15px;
  border-radius: 5px;
  border: 1px solid #ddd;
  font-size: 1.5rem;
  width: 95%; /* Set width to 100% */
}

.btn {
  margin-left: 10px;
  margin-top: 30px;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  color: #fff;
  background-color: #42b983;
  cursor: pointer;
  font-size: 1.1rem;
}
</style>
