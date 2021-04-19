<template>
  <div id="app">
    <h1>Status App</h1>
    <AppForm @form-submitted="postStatus" />
    <hr>
    <div>
      <div class="card" v-for="status in statuses" :key="status._id">
        <h3>{{ status._source.title }}</h3>
        <span>{{ status._source.text }}</span>
      </div>
    </div>
  </div>
</template>

<script>
import AppForm from './components/AppForm';
import axios from 'axios';

export default {
  name: 'App',

  data() {
    return {
      title: 'Status App',
      statuses: []
    }
  },

  components: {
    AppForm
  },

  created() {
    this.getAllStatuses()
  },

  methods: {
    postStatus(status) {
      status = JSON.stringify(status)
      axios.post('http://127.0.0.1:8000/status', status)
        .then(res => {
          if (res.status === 201) {
            alert('Status successfully stored.');
            this.getAllStatuses()
          }
        })
        .catch(err => { console.log(err); });
    },

    getAllStatuses() {
      axios.get('http://127.0.0.1:8000/statuses')
        .then(res => { this.statuses = res.data })
        .catch(err => { console.log(err); });
    }
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

.card {
  border: 1px solid gray;
  border-radius: 5px;
  box-shadow: 1px 1px 1px gray;
  margin: 10px auto;
  padding: 10px;
  width: 600px;
}
</style>
