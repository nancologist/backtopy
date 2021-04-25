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