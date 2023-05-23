<!-- SignUpPage.vue -->
<template>
  <div class="container">
    <h2>Sign Up</h2>
    <form @submit.prevent="signUp" class="form">
      <div class="form-group">
        <label for="new-username">Username:</label>
        <input type="text" id="new-username" v-model="username" class="form-control">
      </div>
      <div class="form-group">
        <label for="new-password">Password:</label>
        <input type="password" id="new-password" v-model="password" class="form-control">
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
      console.log('Signing up with', this.username, this.password)
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
