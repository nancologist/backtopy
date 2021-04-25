import Vue from 'vue';
import Vuex from 'vuex';
import axios from '../axios';

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    statuses: [],
    statusOnEdit: undefined,
  },

  mutations: {
    getStatuses(state, statuses) {
      state.statuses = statuses;
    },

    setStatusOnEdit(state, id) {
      state.statusOnEdit = state.statuses.find(item => item._id === id)
    }
  },

  actions: {
    fetchAllStatuses(ctx) {
      axios.get('/statuses')
        .then(res => {
          const statuses = res.data;
          ctx.commit('getStatuses', statuses)
        })
        .catch(err => { console.log(err); });
    }
  }
});