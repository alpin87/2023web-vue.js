<template>
  <PageHeader/>
  <div class="container">
    <PageMenu/>
    <router-view/>
  </div>
  <PageFooter/>
</template>

<script>
import PageHeader from '@/components/PageHeader.vue'
import PageFooter from '@/components/PageFooter.vue'
import PageMenu from '@/components/PageMenu.vue'

export default {
  name: 'App',
  components: {
    PageFooter,
    PageHeader,
    PageMenu
  },
  data () {
    return {
      userLoggedIn: false
    }
  }
}
</script>

<style>

@import '@/style.css';

.container{
  display: flex;
}
aside{
  width:20%;
  background-color: aqua;
}
</style>
