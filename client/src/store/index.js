import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    statuses: [],
    statusOnEdit: undefined,
    test: 'Hallo Helmut'
  },

  mutations: {

  }
});