<template>
  <div>
    <BuzzerList />
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import BuzzerList from './components/BuzzerList.vue'

export default {
  name: 'App',
  components: {
    BuzzerList
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
