<template>
  <div id="app">
    <h1>Status App</h1>
    <AppForm @form-submitted="postStatus" />
    <hr>
    <Card
      v-for="status in statuses"
      :key="status._id"
      :status="status"
      @ondelete="deleteStatus($event)"
    />
  </div>
</template>

<script>
import AppForm from './components/AppForm';
import Card from './components/Card';
import axios from './axios';

export default {
  name: 'App',

  data() {
    return {
      title: 'Status App',
      statuses: []
    }
  },

  components: {
    AppForm,
    Card
  },

  created() {
    this.getAllStatuses()
  },

  methods: {
    getAllStatuses() {
      axios.get('/statuses')
        .then(res => { this.statuses = res.data })
        .catch(err => { console.log(err); });
    },

    postStatus(status) {
      status = JSON.stringify(status)
      axios.post('/status', status)
        .then(res => {
          if (res.status === 201) {
            alert('Status successfully stored.');
            this.getAllStatuses()
          }
        })
        .catch(err => { console.log(err); });
    },

    deleteStatus(id) {
      const confirmed = confirm('Are you sure?');
      if (confirmed) {
        axios.delete(`/status/${id}`)
          .then(res => {
            if (res.status === 200) {
              this.statuses = this.statuses.filter(item => item._id !== id)
              console.log(this.statuses);
            }
          })
          .catch(err => { console.log(err); });
      }
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
</style>
