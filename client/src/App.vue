<template>
  <div id="app">
    <Navigation />
    <router-view></router-view>
    <AppForm
      @form-submitted="handleFormSubmit"
      @cancel-edit="cancelEditStatus"
    />
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
import axios from './axios';

import Navigation from './components/Navigation';
import AppForm from './components/AppForm';
import Card from './components/Card';

export default {
  name: 'App',

  data() {
    return {
      title: 'Status App',
    }
  },

  components: {
    Navigation,
    AppForm,
    Card
  },

  computed: {
    statuses() {
      return this.$store.state.statuses;
    }
  },

  created() {
    this.$store.dispatch('fetchAllStatuses')
  },

  methods: {
    handleFormSubmit(status) {
      if (!this.statusOnEdit) {
        this.postStatus(status)
      } else {
        this.updateStatus(status)
      }
    },

    startEditStatus(id) {
      this.$store.commit('getStatusById', id);
    },

    cancelEditStatus() {
      this.$store.commit('cancelStatusOnEdit');
    },

    postStatus(status) {
      status = JSON.stringify(status)
      axios.post('/status', status)
        .then(res => {
          if (res.status === 201) {
            alert('Status successfully stored.');
            this.getAllStatuses();
          }
        })
        .catch(err => { console.log(err); });
    },

    updateStatus(status) {
      status = JSON.stringify(status)
      axios.put('/status', status)
        .then(res => {
          this.statusOnEdit = undefined;
          if (res.status === 200) {
            alert('Status successfully updated.');
            this.getAllStatuses();
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
              this.$store.commit('removeStatus', id)
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
}
</style>
