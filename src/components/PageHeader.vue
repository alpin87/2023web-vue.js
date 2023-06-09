<template>
  <header class="header-container">
    <div class="left-container">
      <div class="hamburger-menu" @click="menuOpen = !menuOpen">
        <div></div>
        <div></div>
        <div></div>
      </div>
      <div class="brand-name" @click="$router.push({ name: 'home' })">C-S Brand</div>
      <router-link to="/rate" class="nav-item">실시간 뉴스</router-link>
    </div>
    <div class="right-container">
      <div class="digital-clock">
        현재 시간: {{ currentTime }}
        <div>오전 9시까지: {{ timeTo9am }} 남았습니다.</div>
        <div>오후 3시 30분까지: {{ timeTo330pm }} 남았습니다.</div>
      </div>
      <nav class="nav">
        <router-link to="/" class="nav-item">메인</router-link>
        <router-link to="/login" class="nav-item">로그인</router-link>
      </nav>
    </div>
    <PageMenu :menuOpen="menuOpen"/>
  </header>
</template>

<script>
import moment from 'moment'
import PageMenu from './PageMenu.vue'

export default {
  name: 'PageHeader',
  components: {
    PageMenu
  },
  data () {
    return {
      now: moment(),
      menuOpen: false
    }
  },
  computed: {
    currentTime () {
      return this.now.format('HH:mm:ss')
    },
    timeTo9am () {
      const now = this.now
      const nineAm = now.clone().set({ hour: 9, minute: 0, second: 0 })
      if (now.isAfter(nineAm)) nineAm.add(1, 'day')
      const diff = nineAm.diff(now)
      const duration = moment.duration(diff)
      return `${duration.hours()}시간 ${duration.minutes()}분`
    },
    timeTo330pm () {
      const now = this.now
      const threeThirtyPm = now.clone().set({ hour: 15, minute: 30, second: 0 })
      if (now.isAfter(threeThirtyPm)) threeThirtyPm.add(1, 'day')
      const diff = threeThirtyPm.diff(now)
      const duration = moment.duration(diff)
      return `${duration.hours()}시간 ${duration.minutes()}분`
    }
  },
  methods: {
    updateTime () {
      this.now = moment()
    }
  },
  created () {
    setInterval(this.updateTime, 1000)
  }
}
</script>

<style scoped>
.header-container {
  background-color: #ffffff;
  color: #000;
  padding: 20px;
  border-radius: 5px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 1001;  /* 헤더가 메뉴 위에 위치하도록 수정 */
  position: relative;  /* z-index를 적용하기 위한 position 설정 */
}

.left-container {
  display: flex;
  align-items: center;
  margin-left : 250px;
}

.brand-name {
  color: #000;
  font-size: 1.3em;
  margin-right: 20px;
  cursor: pointer;
  margin-left : 130px;
}

.nav-item {
  text-decoration: none;
  color: #000;
  font-size: 0.8em;
  padding: 5px 10px;
  border-radius: 5px;
  margin-left: 10px;
}

.right-container {
  display: flex;
  align-items: center;
  margin-right:400px;
}

.digital-clock {
  text-align: center;
  font-size: 0.8em;
  background: lightgray;
  color: black;
  padding: 5px;
  border-radius: 5px;
  border: 10px solid white;
}

.nav {
  display: flex;
  align-items: center;
}

.hamburger-menu {
  width: 2rem;
  height: 2rem;
  position: absolute;
  display: flex;
  flex-flow: column;
  justify-content: space-around;
  cursor: pointer;
  margin-left:-119px;
}

.hamburger-menu div {
  width: 2rem;
  height: 0.2rem;
  background-color: #000;
}
</style>
