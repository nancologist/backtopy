<template>
  <div id="app">
    <HelloWorld :msg="title"/>
    <div>
      <p v-for="status in statuses" :key="status._id">{{ status._source.title }} : {{ status._source.text }}</p>
      
    </div>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';
import axios from 'axios';

export default {
  name: 'App',

  data: () => ({
    title: 'Status App',
    statuses: []
  }),
  components: {
    HelloWorld
  },

  created() {
    axios.get('http://127.0.0.1:8000/statuses')
      .then(res => { this.statuses = res.data })
      .catch(err => { console.log(err); });
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
