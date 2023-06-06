<!-- SignUpPage.vue -->
<template>
  <div class="container">
    <h2>Sign Up</h2>
    <form @submit.prevent="signUp" class="form">
      <div class="form-group">
        <label for="new-username">Username:</label>
        <input type="text" id="new-username" v-model="username" placeholder="아이디를 입력해주세요" class="form-control" required>
      </div>
      <div class="form-group">
        <label for="new-password">Password:</label>
        <input type="password" id="new-password" v-model="password" class="form-control" required>
      </div>
      <button type="submit" class="btn">Sign Up</button>
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

<!-- 기존의 스타일링 코드는 생략했습니다 -->
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
