<template>
    <header>
      <nav>
        <router-link to="/">Home</router-link> |
        <router-link to="/login">Login</router-link>
        <BoardMenu />
      </nav>
      <hr>
    </header>
</template>

<script>
import BoardMenu from './BoardMenu.vue'

export default {
  name: 'PageHeader',
  components: {
    BoardMenu
  }
}
</script>

<style>

</style>
