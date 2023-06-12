<template>
  <div class="container">
    <div class="card">
      <h2 class="card-header">Login</h2>
      <form @submit.prevent="login" class="form">
        <div class="form-group">
          <label for="username">아이디</label>
          <input type="text" id="username" v-model="username" class="form-control" required>
          <label for="password">비밀번호</label>
          <input type="password" id="password" v-model="password" class="form-control" required>
          <button type="submit" class="btn">{{ loginText }}</button> <!-- using loginText here -->
          <router-link to="/signup" custom>
            <template v-slot:default="{ navigate }">
              <button class="btn" @click="navigate">Sign Up</button>
            </template>
          </router-link>
          <button class="btn">
          <div id="naver_id_login"></div>
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
// Assuming naver_id_login is globally available or imported
// const { naver_id_login } = globalThis; // Uncomment if needed

export default {
  data () {
    return {
      username: '',
      password: ''
    }
  },
  computed: {
    loginText () {
      return this.username && this.password ? 'Login' : '로그인'
    }
  },
  mounted () {
    if (window.naver) {
      this.initNaverLogin()
    } else {
      const naverScript = document.createElement('script')
      naverScript.src = 'https://static.nid.naver.com/js/naverLogin_implicit-1.0.3.js'
      document.head.appendChild(naverScript)

      naverScript.onload = this.initNaverLogin
    }
  },
  methods: {
    initNaverLogin () {
    /* eslint-disable new-cap */
      var naverLogin = new window.naver_id_login('m5npFmBjcdL8D4jVW6wx', 'http://localhost:8080/naverlogin')
      /* eslint-enable new-cap */
      var state = naverLogin.getUniqState()
      naverLogin.setButton('white', 2, 40)
      naverLogin.setDomain('http://localhost:8080/')
      naverLogin.setState(state)
      naverLogin.setPopup()
      naverLogin.init_naver_id_login()
    },
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
  width: 1800px;  /* Updated width to 1800px */
  height: 100%;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center; /* Updated to center */
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
  padding: 50px 20px; /* Increase the top and bottom padding */
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

.form {
  padding: 20px;
}

.form-group {
  display: flex;
  flex-direction: column; /* Stack the elements vertically */
  align-items: stretch; /* Stretch the elements to take up full width */
  gap: 10px; /* Space between the elements */
}

.form-control {
  padding: 15px;  /* Increased padding */
  border-radius: 5px;
  border: 1px solid #ddd;
  font-size: 1.5rem;  /* Increased font size */
  height: 1.5em;  /* Increased height */
  width: 93%;  /* Added to set the width of the input fields */
}

.btn,
.btn-secondary {
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
